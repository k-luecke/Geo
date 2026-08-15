# CLOSURE LEDGER

Program: zero-capital closure loop
Repository: k-luecke/Geo, branch claude/zero-capital-closure-xnfg72
Session date: 2026-08-15
Ledger created: 2026-08-15 (UTC)

## Path configuration audit

Recorded per Section 0 of the loop prompt. A path that does not exist is recorded as MISSING, not substituted.

| Key | Configured path | Status |
|---|---|---|
| MANUSCRIPT | ./manuscript_v11.tex | MISSING as .tex; author delivered ./manuscript_v11.pdf on 2026-08-15 (sha256 70abbfe5..., pdfTeX build of 2026-08-13), landed at repo root with a labelled pdftotext extraction at ./extraction/manuscript_v11_pdftotext.txt |
| MANUSCRIPT_MD | ./manuscript_v11.md | MISSING |
| ARTIFACTS | ./artifacts/ (o3_vault_run.py, o3_results.json, o3_recompile.ipynb) | MISSING |
| FIGS | ./figs/ | MISSING |
| REFS | ./refs/ | MISSING |
| REPORTS | ./reports/ | MISSING |
| LEDGER | ./CLOSURE_LEDGER.md | CREATED this session |
| ESCALATIONS | ./DECISIONS_FOR_KYLE.md | NOT CREATED, no escalations raised |
| STOPS | ./HARD_STOPS.md | NOT CREATED, no hard stop fired |
| VERIFY | ./VERIFICATION_LEDGER.md | NOT CREATED, blocked, see T0.3 |

Artifact deliveries, 2026-08-15 session continuation: the author uploaded manuscript_v11.pdf three times under the names manuscript_v11, manuscript_v111, manuscript_v112; all three are byte-identical (single sha256), so only one manuscript version exists in this session. A companion explainer page, silentshift.html, was landed at ./site/silentshift.html; it is outside the closure loop's scope. A zip of the eris staging repo (bibliography.md, literature-review.md, data-acquisition-manifest.md) was received but every project file in it is truncated at about 20 KB mid-sentence and its MANIFEST.sha256 was computed over the truncated bytes; it was NOT committed. Fresh hashes for the landed files are in ./MANIFEST.sha256.

Repository census at session start: the working tree contains exactly one file, LICENSE. Git history is a single commit (ac80e28, "Initial commit", LICENSE only). No other branch on the remote carries content (refs: main only). The home directory outside the repository contains no research artifacts.

## Task registry

| Item | Tier | Depends on | Status | Verdict |
|---|---|---|---|---|
| T0.1 Reproduction rerun and npz recovery | 0 | none | BLOCKED-EXTERNAL | see record |
| T0.2 Kappa provenance lookup | 0 | none | BLOCKED-EXTERNAL | see record |
| T0.3 Numeric inventory | 0 | none | BLOCKED-EXTERNAL | see record |
| T1.1 Section 4.1 mechanism decision | 1 | T0.1 | OPEN | dependency-locked, upstream item is BLOCKED-EXTERNAL |
| T1.2 Section 4.3 and 5.1 bracket resolution | 1 | T0.2 | OPEN | dependency-locked, upstream item is BLOCKED-EXTERNAL |
| T1.3 Appendix version identity | 1 | T0.1 | OPEN | dependency-locked, upstream item is BLOCKED-EXTERNAL |
| T2.1 Bibliography insertion | 2 | none | BLOCKED-EXTERNAL | see record |
| T2.2 Medium-confidence field resolution | 2 | T2.1 | OPEN | dependency-locked, upstream item is BLOCKED-EXTERNAL |
| T2.3 Unrecovered patent and dataset fields | 2 | T2.1 | OPEN | dependency-locked, upstream item is BLOCKED-EXTERNAL |
| T2.4 Data-source acknowledgment | 2 | none | BLOCKED-EXTERNAL | see record |
| T2.5 Coherence-value attribution | 2 | T0.3 | OPEN | dependency-locked, upstream item is BLOCKED-EXTERNAL |
| T2.6 Compile gate | 2 | rolling | BLOCKED-EXTERNAL | see record |
| T3.1 Pilot spectrum figure | 3 | T0.1 | OPEN | dependency-locked, upstream item is BLOCKED-EXTERNAL |
| T3.2 Null battery panel | 3 | T0.1 | OPEN | dependency-locked, upstream item is BLOCKED-EXTERNAL |
| T3.3 Offset bound versus integration time | 3 | T0.1 | OPEN | dependency-locked, upstream item is BLOCKED-EXTERNAL |
| T4.1 Route 2, source-geometry forward model | 4 | T0.1 | OPEN | dependency-locked, upstream item is BLOCKED-EXTERNAL |
| T4.2 Route 4, segment verification | 4 | none | BLOCKED-EXTERNAL | see record |
| T4.3 Route 5, sequential detection closure | 4 | none | BLOCKED-EXTERNAL | see record |
| T4.4 Route 8, multi-sensor bound | 4 | none | BLOCKED-EXTERNAL | see record |
| T4.5 Route 7, preregistration draft | 4 | none | BLOCKED-EXTERNAL | see record |
| T4.6 Route 1, source-longitude regression | 4 | T4.1, T4.5 | OPEN | dependency-locked, upstream item is BLOCKED-EXTERNAL |
| T4.7 Route 3, methodology validation only | 4 | T4.1 | OPEN | dependency-locked, upstream item is BLOCKED-EXTERNAL |

## Item records

Item records are appended below as the loop processes each item.

### T0.1 Reproduction rerun and npz recovery
Verdict: BLOCKED-EXTERNAL
Date: 2026-08-15
Definition of done: run o3_recompile.ipynb end to end, honor its gates, produce o3_spectra.npz, diff the verdict block against frozen o3_results.json, serialize null_mean and null_sd, write an output-hash manifest.
What was done: searched the working tree, the full git history (single commit, LICENSE only), all remote refs (main only), and the surrounding filesystem. The directory ./artifacts/ does not exist. None of o3_recompile.ipynb, o3_results.json, o3_vault_run.py are present anywhere on disk.
External action needed: commit or otherwise deliver the ./artifacts/ directory containing o3_recompile.ipynb, the frozen o3_results.json, and o3_vault_run.py, together with whatever input data the notebook reads. No substitute artifact was fabricated and no reproduction was simulated.
Evidence: repository census in the path configuration audit above.

### T0.2 Kappa provenance lookup
Verdict: BLOCKED-EXTERNAL
Date: 2026-08-15
Definition of done: determine, with a file path and line reference, whether the 27 ns and 240 ns detector-threshold figures are in-sample on the four-year calibration record.
What was done: the item calls for a search of the typeset LaTeX sources, the notebooks, and any derivation files. None of these exist in the repository or on disk, so the search itself cannot be run.
Why this is BLOCKED-EXTERNAL and not ESCALATED-AUTHOR-DECISION: the escalation path applies when artifacts exist but do not settle the question. Here the search corpus is absent entirely, so the finding "not determinable from available artifacts" would be vacuous, and the escalation format cannot be filled because it requires facts with file paths. Once the sources are delivered, this item should be re-opened and the three-way finding made against them.
External action needed: deliver the manuscript LaTeX sources, the analysis notebooks, and any threshold derivation files covering the four-year calibration record.
Evidence: repository census in the path configuration audit above.

### T0.3 Numeric inventory
Verdict: BLOCKED-EXTERNAL
Date: 2026-08-15
Definition of done: extract every numeric claim in the manuscript into VERIFICATION_LEDGER.md, one row per claim, with source artifact and field.
What was done: neither ./manuscript_v11.tex nor ./manuscript_v11.md exists, so there is no text to inventory. An empty verification ledger would pass the letter of the gate while recording nothing; it was not created, to avoid a misleading artifact.
External action needed: deliver manuscript_v11.tex or manuscript_v11.md, plus the source artifacts numeric claims trace to (at minimum ./artifacts/o3_results.json).
Evidence: repository census in the path configuration audit above.

### T2.1 Bibliography insertion
Verdict: BLOCKED-EXTERNAL
Date: 2026-08-15
Definition of done: insert the verified reference set into the manuscript bibliography with section mapping, then compile clean.
What was done: the verified reference set lives in ./refs/ (reference verification report and bibliography), and the insertion target is manuscript_v11.tex. Neither exists. Reconstructing the reference set from memory would violate standing order 1, so nothing was inserted.
External action needed: deliver ./refs/ (the reference verification report with the section mapping and full entry fields) and manuscript_v11.tex.
Evidence: repository census in the path configuration audit above.
Downstream effect: T2.2 and T2.3 depend on this item and remain OPEN, unselectable.

### T2.4 Data-source acknowledgment
Verdict: BLOCKED-EXTERNAL
Date: 2026-08-15
Definition of done: paste the required acknowledgment text verbatim into the manuscript acknowledgment section, byte-compared against the source in the reference report.
What was done: nothing was pasted. The reference report holding the canonical text is absent, and the manuscript that would receive it is absent. Verbatim means byte-identical to a source on disk; no such source exists, so any insertion would be reconstruction from memory, which standing order 1 forbids for exactly this kind of funding-body sentence.
External action needed: deliver ./refs/ containing the reference report with the canonical acknowledgment text, and manuscript_v11.tex.
Evidence: repository census in the path configuration audit above.

### T2.6 Compile gate
Verdict: BLOCKED-EXTERNAL
Date: 2026-08-15
Definition of done: compile after every Tier 2 edit with zero errors, zero overfull boxes, zero undefined references.
What was done: no Tier 2 edit was possible this session (T2.1 through T2.5 are blocked or dependency-locked) and there is no manuscript_v11.tex to compile, so the gate had nothing to run against.
External action needed: deliver manuscript_v11.tex; the gate becomes active as soon as any Tier 2 edit lands.
Evidence: repository census in the path configuration audit above.

### T4.2 Route 4, segment verification
Verdict: BLOCKED-EXTERNAL
Date: 2026-08-15
Definition of done: intersect the coincident analysis-ready segment lists, check documented gaps against the frozen window, freeze the boundaries in a file.
What was done: nothing could be intersected. The segment lists, the definition of the frozen window, and the gap documentation are not in the repository; the eight-route execution map in ./reports/ that specifies which detector segment databases apply is also absent.
External action needed: deliver the analysis-ready segment lists for both nodes, the frozen window definition (start and end times), and the documented gap list, or the ./reports/ execution map that points to them.
Evidence: repository census in the path configuration audit above.

### T4.3 Route 5, sequential detection closure
Verdict: BLOCKED-EXTERNAL
Date: 2026-08-15
Definition of done: write the close-by-citation paragraph for the whitened case, or state the residual open problem precisely, after checking it against the two most likely recent closures named in the literature memo.
What was done: nothing was written. The literature closure memo in ./reports/ that names the two candidate closures is absent, so the mandated closure check cannot be run as specified; the gate explicitly requires evidence that the check against those named works was performed. The manuscript section that would receive the paragraph is also absent. Substituting my own candidate literature for the memo's named candidates would silently change the preregistered check.
External action needed: deliver the literature closure memo (naming the two candidate closures for the whitened sequential detection case) and manuscript_v11.tex.
Evidence: repository census in the path configuration audit above.

### T4.4 Route 8, multi-sensor bound
Verdict: BLOCKED-EXTERNAL
Date: 2026-08-15
Definition of done: generalize the two-sensor delay-variance bound to M sensors via canonical coherence, with the M equals 2 reduction verified symbolically, or write a companion-paper problem statement with the reduction condition stated.
What was done: no derivation was attempted. The gate requires symbolic verification that the generalization reduces to the paper's own two-sensor bound at M equals 2, and that bound (its exact form, assumptions, and notation) exists only in the missing manuscript and derivation files. Deriving against a guessed form of the bound would make the reduction check meaningless.
External action needed: deliver the manuscript section or derivation file stating the two-sensor delay-variance bound, including its assumptions.
Evidence: repository census in the path configuration audit above.

### T4.5 Route 7, preregistration draft
Verdict: BLOCKED-EXTERNAL
Date: 2026-08-15
Definition of done: draft the confirmatory-run preregistration in the program's own three-way decision-rule format, with hypotheses, decision rules, and analysis plan fixed before any Route 1 or Route 3 confirmatory analysis.
What was done: no draft was written. The program's decision-rule format, the hypotheses for Routes 1 and 3, the published diurnal source-migration relation to be tested, and the stability criteria referenced by T4.1 and T4.6 all live in the missing manuscript and reports. Inventing hypotheses and thresholds would produce a preregistration that does not belong to this program, and downstream gates (T4.6 requires its criterion fixed here) would inherit fabricated rules.
External action needed: deliver manuscript_v11 and the eight-route execution map so the draft can quote the program's hypotheses and decision-rule format rather than reconstruct them.
Evidence: repository census in the path configuration audit above.
