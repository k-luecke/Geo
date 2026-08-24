#!/usr/bin/env python3
from __future__ import annotations

import csv
import hashlib
import json
import math
from pathlib import Path
from datetime import datetime, timezone

import numpy as np
from scipy.signal import butter, sosfiltfilt, hilbert, find_peaks

RUN = Path("/mnt/data/transient_commonview_run")
CAPTURE = Path("/mnt/data/o3_capture_v1.npz")
CATALOG = RUN / "AE20200129_01_to_08UTC.loc.txt"
PREREG = RUN / "transient_commonview_prereg_v1.md"

FS = 128.0
GPS_START = 1264298000
DURATION = 21600.0
UTC_START = datetime(2020, 1, 29, 1, 53, 2, tzinfo=timezone.utc)
UTC_END = datetime(2020, 1, 29, 7, 53, 2, tzinfo=timezone.utc)

EARTH_KM = 6371.0
C_KM_S = 299792.458
VG_FRAC_PRIMARY = 0.75
VG_SENS = [0.70, 0.80]

# Same coordinates as v12.
H1 = (46.455147, -119.407657)
L1 = (30.562894, -90.774240)

# Published IFO arm azimuths used by v12 (clockwise from north).
H1_AZ_X = 324.0
H1_AZ_Y = 234.0
L1_AZ_X = 252.3
L1_AZ_Y = 162.3

BAND = (6.0, 25.0)
PEAK_SIGMA = 6.0
ONSET_SIGMA = 3.0
LOOKBACK_S = 0.25
MIN_SEP_S = 0.5
ASSOC_GATE_S = 0.050
PRIMARY_RESID_GATE_S = 2.0 / FS
N_NULL = 1000
NULL_SEED = 20260824
MIN_NULL_SHIFT_S = 60.0
MIN_EVENTS = 5

def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

def parse_time(date_s: str, time_s: str) -> datetime:
    # Handles microseconds exactly as text provides them.
    y, m, d = [int(x) for x in date_s.strip().split("/")]
    hh, mm, ssfrac = time_s.strip().split(":")
    sec = float(ssfrac)
    s_int = int(math.floor(sec))
    micros = int(round((sec - s_int) * 1_000_000))
    if micros >= 1_000_000:
        s_int += 1
        micros -= 1_000_000
    return datetime(y, m, d, int(hh), int(mm), s_int, micros, tzinfo=timezone.utc)

def haversine_km(lat1, lon1, lat2, lon2):
    lat1 = np.deg2rad(lat1)
    lon1 = np.deg2rad(lon1)
    lat2 = np.deg2rad(lat2)
    lon2 = np.deg2rad(lon2)
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = np.sin(dlat/2.0)**2 + np.cos(lat1)*np.cos(lat2)*np.sin(dlon/2.0)**2
    return 2.0 * EARTH_KM * np.arcsin(np.minimum(1.0, np.sqrt(a)))

def initial_bearing_deg(lat1, lon1, lat2, lon2):
    # From point 1 to point 2, clockwise from geographic north.
    p1 = np.deg2rad(lat1)
    p2 = np.deg2rad(lat2)
    dl = np.deg2rad(lon2 - lon1)
    y = np.sin(dl) * np.cos(p2)
    x = np.cos(p1) * np.sin(p2) - np.sin(p1) * np.cos(p2) * np.cos(dl)
    return (np.rad2deg(np.arctan2(y, x)) + 360.0) % 360.0

def rotate_ifo_to_ne(x, y, azx, azy):
    ax = np.deg2rad(azx)
    ay = np.deg2rad(azy)
    n = x * np.cos(ax) + y * np.cos(ay)
    e = x * np.sin(ax) + y * np.sin(ay)
    return n, e

def axial_diff_deg(a, b):
    # Difference between two axial directions modulo 180 degrees.
    d = (a - b) % 180.0
    return np.minimum(d, 180.0 - d)

def load_catalog():
    rows = []
    with CATALOG.open("r", encoding="utf-8", errors="strict") as f:
        reader = csv.reader(f)
        for idx, r in enumerate(reader):
            if len(r) < 9:
                continue
            try:
                dt = parse_time(r[0], r[1])
                lat = float(r[2])
                lon = float(r[3])
                resid = float(r[4])
                nstn = int(r[5])
                energy = float(r[6])
                energy_unc = float(r[7])
                nstn_energy = int(r[8])
            except Exception:
                continue
            if not (UTC_START <= dt < UTC_END):
                continue
            if not (np.isfinite(lat) and np.isfinite(lon)):
                continue
            # Primary location/timing QC from the frozen preregistration.
            if nstn < 5 or not (resid < 30.0):
                continue

            rel_s = (dt - UTC_START).total_seconds()
            q50 = (
                energy > 0.0
                and energy < 1e8
                and nstn_energy >= 2
                and energy_unc > 0.0
                and energy_unc < 0.5 * energy
            )
            raw_identity = f"{idx}|{r[0].strip()}|{r[1].strip()}|{lat:.6f}|{lon:.6f}"
            stroke_hash = hashlib.sha256(raw_identity.encode("utf-8")).hexdigest()[:20]
            rows.append(
                (idx, rel_s, lat, lon, resid, nstn, energy, energy_unc, nstn_energy, q50, stroke_hash)
            )
    dtype = [
        ("raw_index", "i8"), ("t_s", "f8"), ("lat", "f8"), ("lon", "f8"),
        ("resid_us", "f8"), ("nstn", "i4"), ("energy_j", "f8"),
        ("energy_unc_j", "f8"), ("nstn_energy", "i4"), ("qc50", "?"),
        ("stroke_hash", "U20"),
    ]
    return np.array(rows, dtype=dtype)

def filter_and_detect(x, y):
    sos = butter(4, BAND, btype="bandpass", fs=FS, output="sos")
    xf = sosfiltfilt(sos, x)
    yf = sosfiltfilt(sos, y)

    xa = hilbert(xf)
    ya = hilbert(yf)
    env = np.sqrt(np.abs(xa)**2 + np.abs(ya)**2)
    med = float(np.median(env))
    mad = float(np.median(np.abs(env - med)))
    scale = 1.4826 * mad
    if scale <= 0 or not np.isfinite(scale):
        raise RuntimeError("Non-positive robust envelope scale")

    peaks, _ = find_peaks(
        env,
        height=med + PEAK_SIGMA * scale,
        distance=max(1, int(round(MIN_SEP_S * FS))),
    )

    lookback_n = int(round(LOOKBACK_S * FS))
    low = med + ONSET_SIGMA * scale
    events = []
    for pk in peaks:
        start = max(0, pk - lookback_n)
        seg = env[start:pk+1]
        below = np.flatnonzero(seg < low)
        if len(below) == 0:
            continue
        crossing = start + int(below[-1]) + 1
        if crossing > pk:
            continue
        events.append(
            {
                "event_index": len(events),
                "onset_sample": int(crossing),
                "peak_sample": int(pk),
                "onset_s": float(crossing / FS),
                "peak_s": float(pk / FS),
                "peak_envelope": float(env[pk]),
                "robust_z_peak": float((env[pk] - med) / scale),
            }
        )
    return xf, yf, env, med, scale, events

def geometry_arrays(cat, site, vg_frac):
    lat, lon = site
    d = haversine_km(lat, lon, cat["lat"], cat["lon"])
    prop = d / (vg_frac * C_KM_S)
    arrival = cat["t_s"] + prop
    bearing = initial_bearing_deg(lat, lon, cat["lat"], cat["lon"])
    return d, prop, arrival, bearing

def associate_site(events, arrivals):
    if not events:
        return {}
    order = np.argsort(arrivals)
    sa = arrivals[order]
    out = {}
    for e in events:
        t = e["onset_s"]
        lo = np.searchsorted(sa, t - ASSOC_GATE_S, side="left")
        hi = np.searchsorted(sa, t + ASSOC_GATE_S, side="right")
        if hi - lo == 1:
            stroke_idx = int(order[lo])
            resid = float(t - arrivals[stroke_idx])
            prev = out.get(stroke_idx)
            rec = {
                "event_index": int(e["event_index"]),
                "onset_s": float(t),
                "site_arrival_resid_s": resid,
            }
            if prev is None or abs(resid) < abs(prev["site_arrival_resid_s"]):
                out[stroke_idx] = rec
    return out

def common_view(cat, ev_h, ev_l, vg_frac):
    dH, pH, aH, bH = geometry_arrays(cat, H1, vg_frac)
    dL, pL, aL, bL = geometry_arrays(cat, L1, vg_frac)
    ah = associate_site(ev_h, aH)
    al = associate_site(ev_l, aL)
    common = sorted(set(ah).intersection(al))
    records = []
    for k in common:
        th = ah[k]["onset_s"]
        tl = al[k]["onset_s"]
        pred_diff = pH[k] - pL[k]
        resid = (th - tl) - pred_diff
        records.append(
            {
                "cat_index": int(k),
                "stroke_hash": str(cat["stroke_hash"][k]),
                "H_event_index": int(ah[k]["event_index"]),
                "L_event_index": int(al[k]["event_index"]),
                "H_onset_s": float(th),
                "L_onset_s": float(tl),
                "H_site_arrival_resid_ms": float(1e3 * ah[k]["site_arrival_resid_s"]),
                "L_site_arrival_resid_ms": float(1e3 * al[k]["site_arrival_resid_s"]),
                "predicted_diff_ms": float(1e3 * pred_diff),
                "geometry_residual_ms": float(1e3 * resid),
                "abs_geometry_residual_ms": float(1e3 * abs(resid)),
                "within_1_sample": bool(abs(resid) <= 1.0 / FS),
                "within_2_samples": bool(abs(resid) <= 2.0 / FS),
                "source_bearing_H_deg": float(bH[k]),
                "source_bearing_L_deg": float(bL[k]),
                "energy_j": float(cat["energy_j"][k]),
                "energy_unc_j": float(cat["energy_unc_j"][k]),
                "nstn": int(cat["nstn"][k]),
                "resid_us": float(cat["resid_us"][k]),
                "nstn_energy": int(cat["nstn_energy"][k]),
                "qc50": bool(cat["qc50"][k]),
            }
        )
    return records, (aH, aL)

def common_view_shifted(cat, ev_h, ev_l, vg_frac, shift_s):
    # Circularly shift source timestamps, preserving source geometry.
    shifted_t = np.mod(cat["t_s"] + shift_s, DURATION)
    dH = haversine_km(H1[0], H1[1], cat["lat"], cat["lon"])
    dL = haversine_km(L1[0], L1[1], cat["lat"], cat["lon"])
    aH = shifted_t + dH / (vg_frac * C_KM_S)
    aL = shifted_t + dL / (vg_frac * C_KM_S)
    ah = associate_site(ev_h, aH)
    al = associate_site(ev_l, aL)
    common = set(ah).intersection(al)
    count = 0
    for k in common:
        th = ah[k]["onset_s"]
        tl = al[k]["onset_s"]
        pred_diff = (dH[k] - dL[k]) / (vg_frac * C_KM_S)
        resid = (th - tl) - pred_diff
        if abs(resid) <= PRIMARY_RESID_GATE_S:
            count += 1
    return count

def event_rows(site, events):
    return [
        {
            "site": site,
            "event_index": e["event_index"],
            "onset_sample": e["onset_sample"],
            "peak_sample": e["peak_sample"],
            "onset_s_from_start": e["onset_s"],
            "peak_s_from_start": e["peak_s"],
            "peak_envelope": e["peak_envelope"],
            "robust_z_peak": e["robust_z_peak"],
        }
        for e in events
    ]

def write_csv(path, rows):
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

def bearing_and_waveform_diagnostics(records, cat, xfH, yfH, xfL, yfL):
    # Diagnostics only; never used for association or verdict.
    Hn, He = rotate_ifo_to_ne(xfH, yfH, H1_AZ_X, H1_AZ_Y)
    Ln, Le = rotate_ifo_to_ne(xfL, yfL, L1_AZ_X, L1_AZ_Y)
    diag = []
    n_bear_within = 0
    n_bear_total = 0

    for r in records:
        k = r["cat_index"]
        eh = int(round(r["H_onset_s"] * FS))
        el = int(round(r["L_onset_s"] * FS))
        n025 = int(round(0.25 * FS))
        n05 = int(round(0.5 * FS))

        def principal_axis(nsig, esig, s0, n):
            s1 = min(len(nsig), s0 + n)
            if s1 - s0 < 4:
                return float("nan")
            X = np.vstack([nsig[s0:s1], esig[s0:s1]])
            cov = np.cov(X)
            vals, vecs = np.linalg.eigh(cov)
            v = vecs[:, int(np.argmax(vals))]
            return float((np.rad2deg(np.arctan2(v[1], v[0])) + 360.0) % 180.0)

        axH = principal_axis(Hn, He, eh, n025)
        axL = principal_axis(Ln, Le, el, n025)
        expectedH = (r["source_bearing_H_deg"] + 90.0) % 180.0
        expectedL = (r["source_bearing_L_deg"] + 90.0) % 180.0
        dH = float(axial_diff_deg(axH, expectedH)) if np.isfinite(axH) else float("nan")
        dL = float(axial_diff_deg(axL, expectedL)) if np.isfinite(axL) else float("nan")

        for d in [dH, dL]:
            if np.isfinite(d):
                n_bear_total += 1
                if d <= 30.0:
                    n_bear_within += 1

        # Waveform diagnostic: envelope cosine similarity after only the predicted
        # geometry lag rounded to nearest sample. No extra lag optimization.
        pred_samples = int(round((r["predicted_diff_ms"] / 1000.0) * FS))
        # H - L = predicted diff. Align by comparing H(t) to L(t - pred_diff).
        h0 = eh
        l0 = eh - pred_samples
        # use H onset as anchor in record time; ensure valid ranges
        h1 = h0 + n05
        l1 = l0 + n05
        corr = float("nan")
        if h0 >= 0 and l0 >= 0 and h1 <= len(Hn) and l1 <= len(Ln):
            henv = np.sqrt(Hn[h0:h1]**2 + He[h0:h1]**2)
            lenv = np.sqrt(Ln[l0:l1]**2 + Le[l0:l1]**2)
            henv = henv - np.mean(henv)
            lenv = lenv - np.mean(lenv)
            denom = np.linalg.norm(henv) * np.linalg.norm(lenv)
            if denom > 0:
                corr = float(np.dot(henv, lenv) / denom)

        diag.append(
            {
                "stroke_hash": r["stroke_hash"],
                "H_axis_deg_mod180": axH,
                "L_axis_deg_mod180": axL,
                "H_expected_mag_axis_deg_mod180": expectedH,
                "L_expected_mag_axis_deg_mod180": expectedL,
                "H_axial_residual_deg": dH,
                "L_axial_residual_deg": dL,
                "waveform_envelope_corr_fixed_geometry_lag": corr,
            }
        )

    return diag, {
        "bearing_axis_count": n_bear_total,
        "bearing_within_30deg_count": n_bear_within,
        "bearing_within_30deg_fraction": (
            n_bear_within / n_bear_total if n_bear_total else None
        ),
    }

def run_association_variant(cat, evH, evL, vg):
    recs, _ = common_view(cat, evH, evL, vg)
    t = sum(bool(r["within_2_samples"]) for r in recs)
    return {
        "vg_fraction_c": vg,
        "catalog_rows": int(len(cat)),
        "common_view_count": int(len(recs)),
        "geometry_consistent_2sample_count": int(t),
        "median_residual_ms": (
            float(np.median([r["geometry_residual_ms"] for r in recs])) if recs else None
        ),
    }

def main():
    z = np.load(CAPTURE, allow_pickle=False)
    if int(z["gps_start"]) != GPS_START or int(z["duration_s"]) != int(DURATION):
        raise RuntimeError("Capture metadata does not match frozen interval")
    if abs(float(z["fs"]) - FS) > 1e-12:
        raise RuntimeError("Capture sample rate does not match freeze")

    H1X = z["H1X"].astype(float, copy=False)
    H1Y = z["H1Y"].astype(float, copy=False)
    L1X = z["L1X"].astype(float, copy=False)
    L1Y = z["L1Y"].astype(float, copy=False)

    cat = load_catalog()

    xfH, yfH, envH, medH, scaleH, evH = filter_and_detect(H1X, H1Y)
    xfL, yfL, envL, medL, scaleL, evL = filter_and_detect(L1X, L1Y)

    write_csv(RUN / "transient_commonview_events_H1.csv", event_rows("H1", evH))
    write_csv(RUN / "transient_commonview_events_L1.csv", event_rows("L1", evL))

    primary_records, _ = common_view(cat, evH, evL, VG_FRAC_PRIMARY)
    diag_rows, diag_summary = bearing_and_waveform_diagnostics(
        primary_records, cat, xfH, yfH, xfL, yfL
    )
    diag_by_hash = {d["stroke_hash"]: d for d in diag_rows}

    # Do not expose raw WWLLN row, timestamp, lat, or lon in output associations.
    assoc_rows = []
    for r in primary_records:
        keep = {k: v for k, v in r.items() if k != "cat_index"}
        keep.update(diag_by_hash.get(r["stroke_hash"], {}))
        assoc_rows.append(keep)
    write_csv(RUN / "transient_commonview_associations.csv", assoc_rows)

    T_obs = int(sum(bool(r["within_2_samples"]) for r in primary_records))

    rng = np.random.default_rng(NULL_SEED)
    # Generate continuous circular shifts, rejecting |shift| < 60 s relative to zero.
    shifts = []
    while len(shifts) < N_NULL:
        s = float(rng.uniform(0.0, DURATION))
        circular_abs = min(s, DURATION - s)
        if circular_abs >= MIN_NULL_SHIFT_S:
            shifts.append(s)

    null_counts = np.empty(N_NULL, dtype=np.int32)
    for i, s in enumerate(shifts):
        null_counts[i] = common_view_shifted(cat, evH, evL, VG_FRAC_PRIMARY, s)
    np.save(RUN / "transient_commonview_null_counts.npy", null_counts)

    p_emp = float((1 + np.count_nonzero(null_counts >= T_obs)) / (N_NULL + 1))

    if len(evH) < MIN_EVENTS or len(evL) < MIN_EVENTS:
        verdict = "inconclusive"
        verdict_reason = "fewer than five detected events at one or both sites"
    elif T_obs >= 5 and p_emp <= 0.05:
        verdict = "supports_HA"
        verdict_reason = "T_obs >= 5 and empirical p <= 0.05"
    elif T_obs >= 5 and p_emp > 0.05:
        verdict = "no_support_for_HA"
        verdict_reason = "minimum event count met but empirical p > 0.05"
    else:
        verdict = "inconclusive"
        verdict_reason = "fewer than five geometry-consistent common-view events"

    residuals = [r["geometry_residual_ms"] for r in primary_records]
    qc50 = cat[cat["qc50"]]
    secondary = {
        "qc50_subset": run_association_variant(qc50, evH, evL, VG_FRAC_PRIMARY),
        "vg_sensitivities": [
            run_association_variant(cat, evH, evL, vg) for vg in VG_SENS
        ],
    }

    summary = {
        "experiment": "transient_commonview_v1",
        "preregistered_before_event_match_inspection": True,
        "interval": {
            "gps_start": GPS_START,
            "duration_s": DURATION,
            "fs_hz": FS,
        },
        "inputs": {
            "capture_sha256": sha256(CAPTURE),
            "catalog_sha256": sha256(CATALOG),
            "prereg_sha256": sha256(PREREG),
            "primary_catalog_rows": int(len(cat)),
            "qc50_rows_secondary": int(np.count_nonzero(cat["qc50"])),
        },
        "detector": {
            "H1_event_count": int(len(evH)),
            "L1_event_count": int(len(evL)),
            "H1_envelope_median": medH,
            "L1_envelope_median": medL,
            "H1_envelope_robust_scale": scaleH,
            "L1_envelope_robust_scale": scaleL,
        },
        "primary": {
            "vg_fraction_c": VG_FRAC_PRIMARY,
            "association_gate_ms": 1000 * ASSOC_GATE_S,
            "geometry_gate_ms": 1000 * PRIMARY_RESID_GATE_S,
            "common_view_count": int(len(primary_records)),
            "T_obs_geometry_consistent": T_obs,
            "within_1_sample_count": int(sum(bool(r["within_1_sample"]) for r in primary_records)),
            "median_residual_ms": float(np.median(residuals)) if residuals else None,
            "mad_residual_ms": (
                float(np.median(np.abs(np.array(residuals) - np.median(residuals))))
                if residuals else None
            ),
            "null_n": N_NULL,
            "null_seed": NULL_SEED,
            "null_mean_T": float(np.mean(null_counts)),
            "null_median_T": float(np.median(null_counts)),
            "null_max_T": int(np.max(null_counts)),
            "empirical_p": p_emp,
            "verdict": verdict,
            "verdict_reason": verdict_reason,
        },
        "diagnostics": diag_summary,
        "secondary": secondary,
        "interpretation_boundary": (
            "128 Hz common-view feasibility only; no precision timing or position claim."
        ),
    }

    (RUN / "transient_commonview_summary.json").write_text(
        json.dumps(summary, indent=2), encoding="utf-8"
    )

    # Manifest after all primary outputs are written.
    script_path = RUN / "transient_commonview_analysis_v1.py"
    artifact_names = [
        "transient_commonview_prereg_v1.md",
        "transient_commonview_prereg_v1.json",
        "transient_commonview_prereg_v1_manifest.json",
        "transient_commonview_analysis_v1.py",
        "transient_commonview_events_H1.csv",
        "transient_commonview_events_L1.csv",
        "transient_commonview_associations.csv",
        "transient_commonview_null_counts.npy",
        "transient_commonview_summary.json",
    ]
    manifest = {
        "experiment": "transient_commonview_v1",
        "inputs": {
            "o3_capture_v1.npz": sha256(CAPTURE),
            "AE_catalog_private_not_redistributed": sha256(CATALOG),
        },
        "artifacts": {},
    }
    for name in artifact_names:
        p = RUN / name
        if p.exists():
            manifest["artifacts"][name] = sha256(p)
    (RUN / "transient_commonview_manifest.json").write_text(
        json.dumps(manifest, indent=2), encoding="utf-8"
    )

    print(json.dumps(summary, indent=2))

if __name__ == "__main__":
    main()
