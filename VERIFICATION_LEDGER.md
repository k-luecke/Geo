# VERIFICATION LEDGER

Built by closure item T0.3 on 2026-08-15 against the author-delivered manuscript_v11.pdf
(sha256 70abbfe5ad72058acb5ff9f24d93d25f6d445744faf338357ca572e8b2b3a7b1).
Locations cite ./extraction/manuscript_v11_pdftotext.txt line numbers (file committed; refs are stable).

Status vocabulary:
- VERIFIED: the value is an arithmetic or algebraic consequence of other quantities stated in the manuscript, recomputed this session and matching. The manuscript itself is the artifact; the source field names the inputs. This is internal consistency, not external sourcing.
- UNSOURCED: the value is a measurement or external fact whose source artifact is named but not on disk this session. Nothing was retrieved to confirm it.
- FLAG: the manuscript itself marks the value's provenance or citation as unresolved.

Artifacts the manuscript names but which are NOT on disk: the frozen O3 deposit and its results file (Appendix A, v4 hash f45dca61...), the pilot GW170814 analysis outputs, the four-year Sierra Nevada parameter-fit record, the servo innovation calibration record, and GWOSC source data. Every row pointing at one of these is UNSOURCED until it is delivered.

Arithmetic checks were machine-recomputed this session; "arith ok" in Notes means the recomputation matched to the stated precision (values the text labels "about" or "roughly" matched within that labelling).

| ID | Claim | Value | Location | Source artifact | Source field | Status | Notes |
|---|---|---|---|---|---|---|---|
| N01 | Analysis band | 6 to 25 Hz | Abstract L15; Sec 3.3 L380 | manuscript definition; refs [18],[19] | band selection | UNSOURCED | refs [18],[19] fields unverified, see T2.2 |
| N02 | Delay attack shifts offset estimate by half the inserted delay | δ/2 | Abstract L13; Sec 2.1 L94-107 | manuscript eq (1) | algebraic derivation | VERIFIED | follows from eq (1) |
| N03 | Parameter-domain integrity floor | 90 s | Abstract L19; Sec 4.1 L536 | four-year Sierra Nevada fit record | floor estimate | UNSOURCED | record not on disk |
| N04 | Waveform envelope at assumed unity coherence | 12 to 363 µs | Abstract L20; Sec 4.2 L553-556 | eq (4) evaluation outputs | bound values | UNSOURCED | consistent with N30-N32 |
| N05 | Observatory baseline | 3002 km | Abstract L22; Sec 3.6 L473 | H1/L1 site coordinates (public) | great-circle distance | UNSOURCED | not recomputed from coordinates this session |
| N06 | Pilot bound through facility sensor | 184 µs per day | Abstract L25; Sec 4.5 L599 | pilot analysis outputs | projected bound | UNSOURCED | arith ok: 903 µs/sqrt(24) = 184.3 |
| N07 | Preregistered coherence rise | fifty-fold (R = 50) | Abstract L28; Table III L691 | frozen O3 deposit results | R | UNSOURCED | arith ok: 0.2892/0.0058 = 49.9 |
| N08 | Preregistered forecast window | 30 to 100 | Abstract L28; Table III L634 | frozen O3 deposit | forecast bounds | UNSOURCED | threshold, needs frozen text |
| N09 | Measured bound at six hours | 76.6 µs (corrected; 45.7 raw) | Abstract L29; Table III L693 | frozen O3 deposit results | D1 bound | UNSOURCED | |
| N10 | Projected bound at one day | 38 µs (38.3; 22.8 raw) | Abstract L29; Table III L694 | frozen O3 deposit results | D1 projection | UNSOURCED | arith ok: 76.6/2 = 38.3, 45.7/2 = 22.85 |
| N11 | Pre-alarm bias law | θdet = (κσ√(3Δt))^(2/3) r^(1/3) | Abstract L36; eq (5) L416 | manuscript Prop 1 | derivation | VERIFIED | proof recomputed, large-N limit sound |
| N12 | Barreto delay box precision | a few microseconds | Sec 2.2 L125-126 | ref [3] | reported capability | UNSOURCED | citation not retrieved |
| N13 | Finkenzeller testbed precision | microsecond | Sec 2.2 L129-130 | ref [7] | reported capability | UNSOURCED | |
| N14 | Threshold equilibrium condition | 2εmax ≤ DRT ≤ ΔERR + 2εmin | Sec 2.3 L181-183 | ref [1] Mizrahi | theorem | UNSOURCED | |
| N15 | Path redundancy requirement | N > 3m | Sec 2.3 L187; Table I L244 | ref [2] Lamport and Melliar-Smith | theorem | UNSOURCED | |
| N16 | PTPsec detection latency | a few synchronization intervals | Sec 2.4 L144 | refs [8],[9] | reported result | UNSOURCED | |
| N17 | Bulk propagation term | 2.2 ms per 500 km | Table II L275; Sec 3.1 L311 | derived from v ≈ 0.77c | geometry | UNSOURCED | arith ok: 2.17 ms; v from ref [17], unverified |
| N18 | Source-location error per event (50 km) | 220 µs | Table II L276 | derived from v ≈ 0.77c | geometry | UNSOURCED | arith ok: 216.6 µs at 0.77c, stated as approximate |
| N19 | Source-location error after 1 h | 5 µs | Table II L276 | derived, N^(-1/2) averaging | statistics | UNSOURCED | arith ok: 220/sqrt(1800) = 5.19 |
| N20 | Dispersion residual | ≤ 163 µs per 500 km | Table II L281; Sec 3.1 L313 | propagation model, ref [17] | dispersion bound | UNSOURCED | |
| N21 | Assumed event rate | about 1800 events per hour | Table II L290 | lightning climatology, uncited | rate | UNSOURCED | no citation given in manuscript |
| N22 | Mode group velocity | 0.742 to 0.800 c | Sec 3.1 L310 | ref [17] | velocity range | FLAG | ref [17] marked "[Verify fields]" in manuscript |
| N23 | Cavity quality factor | Q ≈ 4 | Sec 3.1 L319 | literature, uncited at point of use | Q | UNSOURCED | |
| N24 | Natural field amplitude in band | 0.1 to 1 pT | Sec 3.1 L329; Sec 5.3 L834 | literature, uncited at point of use | amplitude | UNSOURCED | |
| N25 | Four-year record size | 201534 ten-minute records | Sec 3.2 L374 | ref [20] Granada repository | record count | FLAG | ref [20] marked "[Complete citation.]" |
| N26 | Archival cadence | ten minutes (600 s) | Sec 3.2 L375 | ref [20] dataset | cadence | UNSOURCED | |
| N27 | Process correlation scale | about fourteen minutes | Sec 3.2 L376; Sec 4.1 L537 | four-year fit record | correlation scale | UNSOURCED | |
| N28 | Effective bandwidth | β ≈ 13 Hz inside B = 19 Hz | Sec 3.3 L382 | four-year spectrum | effective bandwidth | UNSOURCED | B arith ok: 25 − 6 = 19 |
| N29 | Static first-crossing values | 171 to 420 ns | Sec 3.4 L404 | detection calibration record | first-crossing range | UNSOURCED | |
| N30 | Unity-coherence bound at one hour | 57 µs | Sec 4.2 L553 | eq (4) evaluation | bound | UNSOURCED | |
| N31 | Unity-coherence bound at one day | 12 µs | Sec 4.2 L554 | eq (4) evaluation | bound | UNSOURCED | arith ok: 57/sqrt(24) = 11.6, rounds to 12 |
| N32 | SNR-limited bound at one day | 363 µs | Sec 4.2 L554 | eq (4) evaluation | bound | UNSOURCED | |
| N33 | Halving attack rate shrinks pre-detection bias | 21 % | Sec 3.4 L450 | manuscript eq (5) | 1 − 2^(−1/3) | VERIFIED | arith ok: 0.2063 |
| N34 | Innovation spectral exponent | 0.107 | Sec 3.4 L454; Sec 5.1 L779 | four-year calibration record | spectral exponent | UNSOURCED | |
| N35 | Detection threshold constant | κ ≈ 3.7 | Sec 4.3 L561 | kappa calibration notebook | fitted κ | UNSOURCED | see D-1 |
| N36 | Predicted detection bias, two cadences | 20 and 202 ns | Sec 4.3 L561-562 | kappa calibration notebook | predicted θdet | UNSOURCED | see D-1 |
| N37 | Measured detection bias, two cadences | 27 and 240 ns | Sec 4.3 L562 | detection measurement record | measured θdet | FLAG | provenance bracketed in manuscript; escalated as D-1 |
| N38 | Pilot best-pair fundamental coherence | γ²(f1) = 0.0091 at z = 7.8 | Sec 4.4 L573-574 | pilot analysis outputs | best-pair MSC | UNSOURCED | |
| N39 | Stacked-station detection | z = 11 | Sec 4.4 L575 | pilot analysis outputs | stacked z | UNSOURCED | |
| N40 | Combined-record mode detections | z = 19.8, 4.8, 3.5 | Sec 4.4 L576-577 | pilot analysis outputs | per-mode z | UNSOURCED | mode-ordered as predicted |
| N41 | Phase-randomization collapse | to 0.0020 | Sec 4.4 L579-580 | pilot analysis outputs | null value | UNSOURCED | |
| N42 | Vertical-coil suppression | twentyfold | Sec 4.4 L580-582 | pilot analysis outputs | suppression ratio | UNSOURCED | |
| N43 | Disjoint-epoch replication | z = 14.2 | Sec 4.4 L583 | pilot analysis outputs | replication z | UNSOURCED | |
| N44 | 60 s shift collapse (reported, not scored) | to 0.0015 | Sec 4.4 L587-588 | pilot analysis outputs | shift value | UNSOURCED | |
| N45 | Pilot canonical coherence | 0.0103 raw | Sec 4.4 L590-591 | pilot analysis outputs | canonical MSC | UNSOURCED | |
| N46 | Pilot empirical null | 0.0045 ± 0.0006 | Sec 4.4 L592 | pilot analysis outputs | off-band null | UNSOURCED | |
| N47 | Pilot corrected coherence | 0.0058 at z = 9.7 | Sec 4.4 L592-593 | pilot analysis outputs | corrected MSC | UNSOURCED | arith ok: 0.0103 − 0.0045 = 0.0058; 0.0058/0.0006 = 9.67 |
| N48 | Station-by-epoch cells | nine cells, z = 3.3 to 16.5 | Sec 4.4 L594-595 | pilot analysis outputs | per-cell z | UNSOURCED | |
| N49 | Pilot measured bound at one hour | 903 µs | Sec 4.5 L599 | pilot analysis outputs | bound | UNSOURCED | |
| N50 | Pilot projected bound at thirty days | 34 µs | Sec 4.5 L600 | pilot analysis outputs | projection | UNSOURCED | arith ok: 903/sqrt(720) = 33.7 |
| N51 | O3 off-band null | 0.0399 ± 0.0118 over 2699 averages | Sec 4.6 L605 | frozen O3 deposit results | null mean and sd | UNSOURCED | null mean and sd not serialized in v4 results file per L1080-1083; see T0.1 |
| N52 | G0 gate | threshold ≥ 90 %; outcome 100 % retrieval | Table III L620-622 | frozen O3 deposit | G0 | UNSOURCED | |
| N53 | P1 gate | z ≥ 5; observed z = 24.5 | Table III L626, L642 | frozen O3 deposit results | P1 | UNSOURCED | arith ok: (0.3291 − 0.0399)/0.0118 = 24.51 |
| N54 | P1 observed coherence | 0.3291 raw | Table III L642 | frozen O3 deposit results | canonical MSC | UNSOURCED | |
| N55 | P1 surrogate maximum | 0.0065 over 20 surrogates | Table III L643; L1009-1010 | frozen O3 deposit results | surrogate max | UNSOURCED | p < 1/21 = 0.0476 |
| N56 | P1 phase-randomized value | 0.0014 | Table III L643 | frozen O3 deposit results | phase-rand null | UNSOURCED | |
| N57 | P2 gate | raw γ² ≥ 0.10; outcome UPHELD, corrected 0.2892 | Table III L631-632, L691 | frozen O3 deposit | P2 | UNSOURCED | arith ok: 0.3291 − 0.0399 = 0.2892 |
| N58 | P2 pilot baseline | 0.0058 | Table III L634 | pilot analysis outputs | baseline | UNSOURCED | matches N47 |
| N59 | D1 outcome | 45.7 µs raw, 76.6 µs corrected at T = 6 h | Table III L693 | frozen O3 deposit results | D1 | UNSOURCED | |
| N60 | D2b gate scatter criterion | ≤ max(3 × per-window bound, 0.3 ms) = 0.795 ms | Table III L639-640 | frozen O3 deposit | D2b threshold | UNSOURCED | arith ok: 3 × 0.265 = 0.795 |
| N61 | D2b lag-window criterion | median lag within 15 ms; majority of windows at p ≤ 0.05 vs 19 surrogates | Table III L637-639 | frozen O3 deposit | D2b threshold | UNSOURCED | |
| N62 | D2b outcome | not passed; 11 of 12 windows; median −3.85 ms; scatter 4.95 ms | Table III L695-696; Sec 4.6 L659-665 | frozen O3 deposit results | D2b | UNSOURCED | |
| N63 | O3 segment identity | GPS 1264298000 + 6 h, 2020-01-29, 100 % retrieval | Table III caption L613; L1048-1049 | frozen O3 deposit execution record | segment | UNSOURCED | GPS-to-date recomputed: 2020-01-29 ✓ |
| N64 | Pair-coherence matrix | H1Y×L1X 0.158, H1X×L1Y 0.148, diagonals 0.022 and 0.097 | Sec 4.6 L648-649 | frozen O3 deposit results | pair matrix | UNSOURCED | |
| N65 | Canonical vs best-pair recovery | 0.329 vs 0.158 | Sec 4.6 L651 | frozen O3 deposit results | comparison | UNSOURCED | |
| N66 | O3 mode ordering | 0.329, 0.108, 0.020 | Sec 4.6 L652 | frozen O3 deposit results | per-mode MSC | UNSOURCED | |
| N67 | Per-window estimation precision | 0.265 ms | Sec 4.6 L654; Fig 1 L734 | frozen O3 deposit results | per-window bound | UNSOURCED | |
| N68 | Lag median and range | −3.85 ms median, ±10 ms range | Sec 4.6 L655-656 | frozen O3 deposit results | lag track | UNSOURCED | inside ±13 ms envelope |
| N69 | Geometric lag envelope | ±13 ms at v ≈ 0.77c | Sec 4.6 L656-657; Fig 1 L735 | derived from N05, N22 | envelope | UNSOURCED | arith ok: 3002 km/0.77c = 13.0 ms |
| N70 | Scatter vs estimation noise | 18.7 times | Sec 4.6 L665; Fig 1 L738 | derived | ratio | UNSOURCED | arith ok: 4.95/0.265 = 18.68 |
| N71 | Morning coherence trend | r = 0.80 | Fig 1 L718, L732 | frozen O3 deposit results | trend statistic | UNSOURCED | |
| N72 | Spectral-matrix conditioning | condition number median 1.5, max 1.8; min eigenvalue positive | Sec 4.6 L676-678 | frozen O3 deposit results | conditioning | UNSOURCED | |
| N73 | Comparison anchor | PTP nominal target sub-microsecond | Sec 5.1 L682 | IEEE 1588 [10] | accuracy target | UNSOURCED | |
| N74 | Two precision quantities differ | three orders of magnitude (ns vs µs) | Sec 5.1 L763-764 | derived from N37, N06 | comparison | VERIFIED | 240 ns vs 184 µs ≈ 10³ |
| N75 | Vault-sited corrected coherence | γ²(f1) = 0.29 | Sec 5.3 L841 | frozen O3 deposit results | corrected MSC | UNSOURCED | rounds from 0.2892, consistent |
| N76 | Facility-sensor precision cost | roughly five times at one day | Sec 5.3 L844-845 | derived | ratio | UNSOURCED | arith ok: 184/38.3 = 4.80, stated "roughly" |
| N77 | Measurement campaign extent | one baseline, three epochs, under nine hours, two sensor classes | Sec 5.3 L819-821 | pilot + O3 records | campaign totals | UNSOURCED | arith ok: 2.63 + 6 = 8.63 h |
| N78 | Direct verification segment | 20 h coincident | Sec 5.3 L826-827; route 4 L890-891 | segment lists (route 4) | segment length | UNSOURCED | see T4.2 |
| N79 | Atlas baseline range | 500 to 10000 km | route 3 L887 | proposal, no artifact | range | UNSOURCED | forward-looking |
| N80 | Wander reduction target | 4.95 ms toward 0.265 ms | route 2 L883-884 | frozen O3 deposit results | targets | UNSOURCED | restates N62, N67 |
| N81 | Frozen deposit version hash | v4 = f45dca61... | Table IV L985-986 | public deposit | freeze hash | UNSOURCED | deposit not on disk; ties to T1.3 |
| N82 | Post-verdict fix version hash | v4.1 = 98a27d1b... | Table IV L987-988 | public deposit | version hash | FLAG | byte-exact recovery bracketed as author decision, L1033-1038; ties to T0.1/T1.3 |
| N83 | Execution environment | Python 3.11.15, NumPy 2.4.6, SciPy 1.17.1, nds2-client 0.16.12 | App A-E L1047-1048 | execution record | versions | UNSOURCED | |
| N84 | Analysis parameters | 128 Hz analysis rate, Welch 2048-sample segments, 1024 overlap, 2699 averages | App A-E L1050-1051 | execution record | parameters | UNSOURCED | 2699 arith ok from 21600 s at 128 Hz |
| N85 | Offline gate criteria | synthetic coherence 0.30 within 15 %; lag +31.250 ms within 0.5 ms; zero-lag centring 0.5 ms; 40° rotation test | App A-E L1052-1058 | frozen O3 deposit | offline gate | UNSOURCED | |
| N86 | D2b ambiguity readings | 11 of 12 vs 8 of 12, both majorities | App A-F L1074-1077 | frozen O3 deposit results | dual reading | UNSOURCED | disclosed defect, immaterial per manuscript |
| N87 | N1 surrogate construction | 64 s blocks, 20 surrogates, p < 1/21 | App A-B L1005-1010 | frozen O3 deposit | N1 | UNSOURCED | p arith ok |
| N88 | Granada dataset identifier | items 10481/71563 | ref [20] L1156 | Granada repository | handle | FLAG | citation marked "[Complete citation.]"; ties to T2.3 |
| N89 | Patent identifiers | US 8,954,608 B1; US 9,960,901 B2 | refs [21],[22] L1158-1159 | patent databases | patent numbers | UNSOURCED | inventors and assignee gap is T2.3 |
| N90 | O3 native rate | 4096 Hz via NDS2 | Sec 3.6 L482 | GWOSC O3 auxiliary release | sample rate | UNSOURCED | |

## Summary

90 rows. 4 VERIFIED (all internal derivations: N02, N11, N33, N74). 5 FLAG (N22, N25, N37, N82, N88), each already tracked by a ledger item or escalation (T2.2, T2.3, D-1, T1.3). 81 UNSOURCED, all tracing to five named artifact groups not on disk: the frozen O3 deposit and results file, the pilot GW170814 outputs, the four-year Sierra Nevada record, the kappa calibration record, and unretrieved citations. Delivering the frozen deposit and results file alone would move roughly 40 rows to checkable.

No numeric contradiction was found. Every recomputable internal relationship (18 machine-checked this session) matched its stated value to stated precision. Hard stop 5 was armed and did not fire.
