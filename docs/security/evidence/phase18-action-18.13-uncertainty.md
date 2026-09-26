# Phase 18 Action 18.13 — Uncertainty

Wilson 95% confidence intervals were calculated for the bounded binary
experiments.

Membership attack accuracy:

- estimate: 0.916667
- 95% Wilson interval: [0.646114, 0.985135]

Important uncertainty sources:

- membership sample size is only 12
- only 6 members and 6 nonmembers are included
- holdout records were deliberately constructed
- membership threshold was lab-calibrated
- clean-model evaluation has only 6 cases
- defense evaluation has only 6 cases
- deterministic training does not represent training-run variability
- DP demonstration uses AWK pseudo-randomness
- local latency measurement is environment-specific
- no LLM or Onyx quantitative transfer is assumed

These intervals apply only to the controlled synthetic experiment.

They are not production risk bounds.

Result: PASS WITH EXPLICIT UNCERTAINTY.
