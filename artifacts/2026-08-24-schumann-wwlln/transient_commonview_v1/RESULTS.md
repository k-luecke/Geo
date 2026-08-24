# Transient/common-view v1 result

This experiment was prospectively frozen before event-match inspection. It tests whether independently detected H1/L1 magnetic transients can be associated with the same named WWLLN stroke strongly enough that geometry-corrected differential delays exceed a time-destroyed catalog null.

## Primary result

- H1 detected transients: **4,431**
- L1 detected transients: **861**
- primary WWLLN location/timing-QC strokes: **149,433**
- same-stroke common-view candidates: **30**
- geometry-consistent within 15.625 ms: **18**
- within one 128 Hz sample: **10**
- median geometry residual: **-11.63 ms**
- residual MAD: **7.79 ms**
- null mean T: **16.854**
- null median T: **17**
- null maximum T: **30**
- empirical one-sided p: **0.4216**
- preregistered verdict: **no support for HA**

The event count itself is not evidence because the circularly shifted WWLLN null produces essentially the same number of geometry-consistent associations. The primary bottleneck exposed by v1 is therefore event identity/association, not simply time resolution.

## Secondary diagnostics

These cannot change the v1 verdict:

- QC50-only catalog: 53 common-view candidates, 30 within two samples.
- v_g = 0.70c: 32 candidates, 19 within two samples.
- v_g = 0.80c: 30 candidates, 18 within two samples.
- bearing diagnostic: 34/60 site-event axes (56.7%) within 30 degrees of the expected magnetic axis.

The bearing result is diagnostic only; no bearing-null test was preregistered.

## Next scientific question

V12 closed the 30-minute source-map ephemeris branch. Transient v1 closes **time-only association** under the frozen 128 Hz protocol. The next open question is whether an independently specified combination of transient polarization/bearing and fixed-lag waveform morphology can provide enough event identity to suppress the time-shift null.
