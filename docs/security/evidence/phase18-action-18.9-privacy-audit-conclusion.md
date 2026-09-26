# Phase 18 Action 18.9 — Quantitative privacy audit

The controlled membership-inference experiment used:

- 6 synthetic members
- 6 synthetic nonmembers
- score threshold: 4

Observed confusion matrix:

- TP: 5
- FN: 1
- FP: 0
- TN: 6

Observed metrics:

- attack accuracy: 0.916667
- TPR: 0.833333
- FPR: 0.000000
- precision: 1.000000
- attack advantage: 0.833333

The result demonstrates measurable distinguishability in this deliberately
constructed tiny-model laboratory.

It does not quantify privacy risk for Onyx, an LLM, a production model,
or a naturally sampled population.

Confidence intervals and broader uncertainty analysis remain for
Action 18.13.

Result: PASS WITH EXPLICIT LIMITATIONS.
