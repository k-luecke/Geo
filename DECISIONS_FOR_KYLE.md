# DECISIONS FOR KYLE

### D-1: Are the measured 27 ns and 240 ns detection-bias values in-sample on the four-year record used to fit kappa, or out-of-sample?
Manuscript location: Section 4.3 (extraction lines 560 to 570 of ./extraction/manuscript_v11_pdftotext.txt); contingent clause in Section 5.1 (extraction lines 785 to 795)
Blocking: T1.2 (Section 4.3 and Section 5.1 bracket resolution); the validation framing of kappa throughout Section 5.1

What the artifacts show:
  - The manuscript states that kappa of approximately 3.7, calibrated on the four-year record, predicts 20 and 202 ns for the two tested cadences, against 27 and 240 ns measured (./extraction/manuscript_v11_pdftotext.txt, lines 560 to 562).
  - The manuscript's own bracket in Section 4.3 asks for the provenance of the measured values and states that Section 5.1 depends on the answer (lines 564 to 570).
  - Section 5.1 carries the mirrored contingent bracket: the out-of-sample reading claims kappa accurate to within tens of percent with the residual in the direction that understates achievable bias; the in-sample reading forbids claiming a validated residual (lines 785 to 795).
  - The bracket also asks for the value of sigma used and both residuals as percentages; neither appears in the delivered PDF.

What the artifacts do not settle:
  - Whether the 27 and 240 ns measurements were taken on the same four-year record on which kappa was fitted. The calibration notebooks and derivation files that would show this are not on disk in this session; the only delivered artifact is the compiled PDF, which poses the question without answering it.

Option A: resolve as out-of-sample.
  Consequence: Section 4.3 labels the comparison a validation; Section 5.1 states kappa is accurate to within tens of percent, that the residual errs toward understating achievable pre-alarm bias, and that validation against an independent servo innovation trace remains outstanding. Materially stronger claim, only safe if the record truly was not used in fitting.
Option B: resolve as in-sample.
  Consequence: Section 4.3 labels the comparison an internal consistency check; Section 5.1 states that no out-of-sample validation of kappa has been performed. Weaker but review-proof; the manuscript bracket itself notes a labelled consistency check survives review while one presented as validation does not.

Recommended reading of the evidence: no lean. The delivered artifacts contain no evidence either way. Note that this decision can be converted back into an evidence question: delivering the kappa calibration notebook or derivation file would let the loop close T0.2 by evidence instead of by author decision, and would also supply the sigma value and residual percentages the bracket requests.
