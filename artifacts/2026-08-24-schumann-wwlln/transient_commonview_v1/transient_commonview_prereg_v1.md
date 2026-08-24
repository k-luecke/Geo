# Transient/Common-View Feasibility Preregistration v1

**Freeze date:** 2026-08-24  
**Status:** Prospective analysis specification. No transient/WWLLN event matches are to be inspected before this specification is frozen.  
**Parent work:** v11 integrity architecture; v12 six-hour WWLLN/coherency experiment.  
**Scientific boundary:** This is a new experiment. It does not reopen Chain7, the LOO audit, the radius sensitivity, or any v11/v12 statistic.

## 1. Question

Can independently detected magnetic transients at LIGO Hanford (H1) and Livingston (L1) be associated with the same named WWLLN stroke such that their geometry-corrected differential delays are more frequent and more physically consistent than chance associations?

For a common stroke k,

R_k = [t_H(k) - t_L(k)] - [r_kH - r_kL] / v_g.

This experiment tests named-transient common-view feasibility. It does not test the 30-minute WWLLN energy-map hypothesis reported in v12, and it does not attempt a position fix.

## 2. Hypotheses

**H0.** Applying the frozen detector and association rule to the real H1/L1 records and contemporaneous WWLLN catalog produces no excess of geometry-consistent common-view transient associations over the time-shifted-catalog null.

**HA.** The real contemporaneous WWLLN catalog produces an excess of geometry-consistent common-view transient associations over the time-shifted-catalog null.

The experiment does not accept H0 as true if HA is unsupported. Outcomes are reported as support for HA, no support for HA, or inconclusive.

## 3. Frozen inputs

### Magnetic record
Use only the preserved six-hour O3 capture:
- GPS 1264298000-1264319600
- UTC 2020-01-29 01:53:02-07:53:02
- sample rate 128 Hz
- H1 X/Y: `H1:PEM-VAULT_MAG_1030X195Y_COIL_X_DQ`, `..._Y_DQ`
- L1 X/Y: `L1:PEM-EY_VAULT_MAG_LEMI_X_DQ`, `..._Y_DQ`
- parent: `o3_capture_v1.npz`

No re-fetch, gap filling, resampling, or alternate O3 interval is permitted for the primary run.

### WWLLN catalog
Primary association uses AE rows inside the exact six-hour UTC interval with:
- parseable UTC timestamp
- finite latitude and longitude
- `nstn >= 5`
- `resid < 30 us`

Energy is **not** used to select primary candidates. A secondary sensitivity repeats the association using the v12 QC50 subset. It cannot change the primary verdict.

The AE-location caveat remains: if an authoritative A-file is later obtained and differs, that is a new analysis version.

Relative detection-efficiency maps are not used because this experiment does not infer stroke density or energy.

## 4. Geometry and propagation

Use:
- Earth sphere radius 6371 km
- same fixed H1/L1 coordinates as v12
- shortest great-circle source-to-site distance
- first-arrival path only
- primary group speed `v_g = 0.75 c`

`v_g` is not fit.

Diagnostic sensitivities only: `0.70 c` and `0.80 c`.

Long-path arrivals, second laps, and echo fitting are excluded from the primary experiment.

## 5. Independent transient detector

Detection is performed separately at H1 and L1 before WWLLN association.

1. Zero-phase fourth-order Butterworth SOS band-pass, 6-25 Hz, on each axis.
2. Hilbert analytic signal per axis.
3. Site envelope:
   `A(t) = sqrt(|X_a(t)|^2 + |Y_a(t)|^2)`.
4. Over the full six hours:
   `m = median(A)`, `s = 1.4826 * MAD(A)`.
5. Trigger: local envelope maximum above `m + 6s`.
6. Minimum peak separation: 0.5 s.
7. Onset: search backward at most 0.25 s; take the sample immediately after the most recent sample below `m + 3s`.
8. If no such crossing exists, discard that peak.
9. The onset sample time is the event timestamp.

No threshold may be lowered after inspection. If fewer than five detected events survive at either site, the experiment is **inconclusive**.

## 6. WWLLN association rule

For each stroke k and site i, predict first arrival:

`t_hat_ki = T_k + r_ki / v_g`.

For each independently detected site event at time `t_i`, candidate strokes satisfy:

`|t_i - t_hat_ki| <= 50 ms`.

A site event is associated only if **exactly one** WWLLN stroke satisfies the gate. Zero or multiple candidates means unassociated.

A common-view candidate exists only when the **same stroke** is uniquely associated at both H1 and L1.

If duplicate site events map to one stroke, retain the event with the smallest absolute site arrival residual and record the duplicate count.

The H1-L1 differential delay is not used to create the association.

## 7. Primary statistic

For each common-view candidate:

`R_k = (t_H - t_L) - (r_kH - r_kL)/v_g`.

At 128 Hz, one sample is 7.8125 ms.

A geometry-consistent event satisfies:

`|R_k| <= 15.625 ms`  (two samples).

Primary statistic:

`T_obs = number of geometry-consistent common-view events`.

The primary statistic is a count, not a fitted clock offset.

## 8. Primary null

Keep magnetic detections fixed.

Construct 1000 null catalogs by circularly shifting all WWLLN stroke timestamps together within the six-hour interval.

- NumPy PRNG seed: `20260824`
- absolute shift >= 60 s
- circular wrap within the six-hour interval
- locations and all non-time fields remain attached to the stroke

For each null, rerun the site-by-site association and compute `T_b`.

Empirical one-sided p-value:

`p_emp = (1 + number[T_b >= T_obs]) / 1001`.

## 9. Decision rule

Support HA only if:
1. `T_obs >= 5`
2. `p_emp <= 0.05`

If at least five geometry-consistent events are observed but `p_emp > 0.05`, report **no support for HA**.

If event yield is too small, report **inconclusive**.

Do not relax thresholds or expand the interval.

## 10. Secondary diagnostics — cannot alter the verdict

Report:
- H1 detected-event count
- L1 detected-event count
- uniquely associated H1/L1 counts
- common-view stroke count
- `T_obs`
- signed median of `R_k`
- MAD of `R_k`
- counts within one and two samples
- associated WWLLN energy/quality fields for description only
- QC50 sensitivity
- `v_g = 0.70c` and `0.80c` sensitivities

### Bearing diagnostic
Bearing is diagnostic only.
- rotate to the fixed geographic NE convention used in v12
- use a 0.25 s filtered snippet beginning at onset
- compute its 2x2 covariance
- principal eigenvector is an axial polarization direction modulo 180 degrees
- compare to the magnetic direction perpendicular to the source-to-site great-circle bearing
- report residual-angle distribution and fraction within 30 degrees
- do not remove events based on bearing

### Waveform diagnostic
Save a 0.5 s two-axis snippet from each site for every primary common-view event and report normalized cross-correlation after applying only the geometry-predicted differential lag rounded to the nearest sample.

Do not optimize an extra lag for the primary result.

## 11. Explicit exclusions

Not part of the primary experiment:
- 30-minute WWLLN source maps
- DE weighting
- source-energy forward modeling
- fitting a cavity kernel
- fitting `v_g`
- second-lap / around-the-world echo ranging
- post-hoc energy thresholds
- manual event selection
- changing the filter after inspection
- lowering trigger thresholds to obtain more events
- position inversion
- claims of GPS-, NTP-, or IEEE-1588-class precision

## 12. Interpretation boundaries

A positive result means that, on this six-hour interval, independently detected magnetic transients can be associated with contemporaneous named WWLLN strokes often enough, and with geometry-corrected H1-L1 differential delays consistent enough, to exceed a time-destroyed catalog null under this fixed 128 Hz protocol.

It does not establish a production time-transfer system, microsecond timing, a position fix, generalization beyond this interval, or recovery of the v12 source-map hypothesis.

A negative result means the frozen 128 Hz protocol did not demonstrate incremental association/timing structure on this interval. It does not prove a higher-bandwidth calibrated system would fail.

## 13. Required artifacts

The run must write:
- `transient_commonview_prereg_v1.md`
- `transient_commonview_prereg_v1.json`
- `transient_commonview_events_H1.csv`
- `transient_commonview_events_L1.csv`
- `transient_commonview_associations.csv`
- `transient_commonview_null_counts.npy`
- `transient_commonview_summary.json`
- `transient_commonview_manifest.json`
- exact analysis script
- SHA-256 hashes for local inputs/scripts/results

Raw WWLLN stroke data must not be redistributed. Association tables should use a local stroke index or irreversible identifier rather than reproducing the raw catalog.

## 14. Freeze rule

After this file is frozen, no primary threshold, passband, time gate, propagation speed, null construction, event-count minimum, or decision criterion may change based on observed transient/WWLLN matches.

Any such change creates a new explicitly labeled exploratory or v2 analysis and cannot replace this v1 result.
