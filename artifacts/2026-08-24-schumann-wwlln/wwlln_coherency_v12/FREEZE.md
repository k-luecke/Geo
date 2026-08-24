# V12 WWLLN/coherency freeze record

## Methodological hierarchy

- **Chain7** = experiment actually run.
- **LOO + radius table** = post-result audit sensitivities only.
- No further tuning or recomputation is authorized for the closed 30-minute WWLLN/coherency branch.

## Primary ordering

\[
L_{\rm equal}=0.390
< L_{\rm frozen}=0.613
< L_{\rm mean}=0.887
< L_{\rm contemporaneous}=0.986.
\]

Contemporaneous beats the same-morning mean in **3/12** windows.

## LOO audit

\[
L_{\rm LOO}=0.888,
\]

with contemporaneous still winning **3/12** windows. This audit does not become part of Chain7 retroactively.

## Radius sensitivity

| R (km) | within H1 | within L1 | within both |
|---:|---:|---:|---:|
| 300 | 1 | 241 | 0 |
| 500 | 1 | 890 | 0 |
| 1000 | 1 | 14,354 | 0 |
| 1500 | 4 | 14,376 | 0 |
| 2000 | 5 | 14,378 | 1 |
| 2500 | 24 | 14,523 | 9 |
| 3000 | 458 | 15,359 | 395 |

No stroke lies simultaneously within R <= 1500 km of both receivers; the first shared stroke appears at the tested radius R = 2000 km. Every tested finite-radius union was a worse predictor of C_HL(f) than the global contemporaneous map.

## Claim boundary

The closed result is a **predictive failure**, not proof that H0 is true: on this interval, the contemporaneous 30-minute DE-corrected WWLLN VLF-energy description did not improve prediction of H1-L1 complex coherency relative to deliberately less informative stationary descriptions.

The scored object is **complex coherency**, not raw S_HL.
