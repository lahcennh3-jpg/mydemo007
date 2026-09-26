# Phase 18 — Adversarial ML and Quantitative Model Privacy

## Status

Accelerated execution.

## Safety boundary

- separate synthetic small-model laboratory
- synthetic data only
- local files and local computation only
- no production model
- no Onyx runtime modification
- no customer data
- no real credentials
- no external model/API calls
- no third-party targeting
- no automatic dependency installation

## Batch A — Actions 18.1–18.6

### Action 18.1 — Separate synthetic small-model laboratory

Result: PASS.

A dedicated local synthetic adversarial-ML laboratory was established.

The laboratory is intentionally separate from the Onyx runtime.

### Action 18.2 — Reproducible training and evaluation

Result: PASS.

A deterministic tiny perceptron was trained twice from identical
synthetic data.

The resulting model files were byte-identical.

Baseline evaluation:

6 / 6 correct classifications.

No external ML framework was required.

### Action 18.3 — Attacker knowledge, access, capability, and goal

Result: PASS.

The attacker model explicitly records:

- knowledge
- access
- capabilities
- goals
- prohibited activities

All attack activity remains local and synthetic.

### Action 18.4 — White-box, gray-box, and black-box assumptions

Result: PASS.

Separate assumptions were established for:

- white-box access
- gray-box access
- black-box access

These are explicit threat-model assumptions rather than implicit
claims.

### Action 18.5 — Evasion attack

Result: PASS.

A bounded L-infinity perturbation of:

0.5

on one synthetic input feature changed the classifier decision for the
controlled laboratory point.

This demonstrates only a small-model synthetic evasion example.

It does not establish transferability to Onyx, LLMs, embeddings,
rerankers, or production AI systems.

### Action 18.6 — Poisoning and backdoor attack

Result: PASS.

Controlled poisoned training rows introduced a synthetic trigger using
feature x3.

The resulting model retained:

6 / 6

correct classifications on the clean evaluation fixture while the
controlled trigger changed the selected target prediction.

This demonstrates the security concept in a deterministic laboratory.

It is not evidence of a production-grade backdoor assessment.

## Phase-18 progress

Completed:

18.1–18.6

Remaining:

18.7 model extraction

18.8 membership inference

18.9 privacy auditing

18.10 differential privacy

18.11 robustness and privacy defenses

18.12 utility, robustness, privacy, compute, and latency trade-offs

18.13 confidence intervals and uncertainty

18.14 transferability limits between small models, LLMs, and Onyx

18.15 reference-tool integration status

18.16 adversarial-ML robustness and privacy benchmark closeout

Progress:

6 / 16 = 37.5%

PHASE_18_BATCH_A_COMPLETE

---

# Batch B — Model Extraction and Quantitative Privacy

## Action 18.7 — Model extraction

Result: PASS.

A synthetic gray-box score interface was queried four times.

For the tiny linear model, those four score observations were sufficient
to recover:

- w1 = 3
- w2 = -4
- w3 = 0
- bias = -1

The recovered parameters exactly matched the synthetic target.

This is a controlled model-extraction demonstration and does not imply
that label-only or production models are equally extractable.

## Action 18.8 — Membership inference

Result: PASS WITH EXPLICIT LIMITATIONS.

A score-threshold membership-inference experiment was executed over:

- 6 synthetic members
- 6 synthetic nonmembers

Observed:

- TP = 5
- FN = 1
- FP = 0
- TN = 6
- attack accuracy = 0.916667
- TPR = 0.833333
- FPR = 0.000000
- attack advantage = 0.833333

The experiment demonstrates a privacy signal in this deliberately
constructed tiny-model fixture.

It is not a production privacy-risk estimate.

## Action 18.9 — Privacy auditing

Result: PASS WITH EXPLICIT LIMITATIONS.

The membership-inference experiment was converted into a quantitative
privacy audit recording:

- audit population
- attack observable
- threshold
- confusion matrix
- attack accuracy
- TPR
- FPR
- precision
- attack advantage
- methodological limitations

The sample is intentionally tiny and synthetic.

Confidence intervals and uncertainty remain for Action 18.13.

## Action 18.10 — Differential privacy

Result: PASS WITH IMPLEMENTATION LIMITATION.

A synthetic neighboring-dataset experiment established a count-query
global sensitivity of 1.

A Laplace-mechanism demonstration evaluated epsilon values:

- 0.5
- 1
- 2

with corresponding theoretical noise scales:

- 2
- 1
- 0.5

The implementation uses AWK pseudo-randomness and is not a production
differential-privacy library.

No DP-SGD training or TensorFlow Privacy execution is claimed.

## Phase-18 progress after Batch B

Completed:

18.1–18.10

Remaining:

18.11 robustness and privacy defenses

18.12 utility, robustness, privacy, compute, and latency trade-offs

18.13 confidence intervals and uncertainty

18.14 transferability limits between small models, LLMs, and Onyx

18.15 reference-tool integration status

18.16 adversarial-ML robustness and privacy benchmark closeout

Progress:

10 / 16 = 62.5%

PHASE_18_BATCH_B_COMPLETE

---

# Batch C — Defenses, Trade-offs, Uncertainty, Transferability, and Closeout

## Action 18.11 — Robustness and privacy defenses

Result: PASS WITH BOUNDED CLAIMS.

- margin threshold: 1
- clean cases: 6
- accepted: 5
- abstained: 1
- coverage: 0.833333
- accepted accuracy: 1.000000

The controlled Action-18.5 adversarial case was neutralized by
abstention.

The label-only interface blocks the exact score-leakage paths used by
the Phase-18 extraction and membership demonstrations.

No claim of general resistance is made.

## Action 18.12 — Trade-offs

Result: PASS.

- baseline coverage: 1.000000
- defended coverage: 0.833333
- defended accepted accuracy: 1.000000
- baseline compute proxy: 7
- defended compute proxy: 9
- latency measurement available: true
- baseline average ns: 35560629
- defended average ns: 41914077
- defended/baseline ratio: 1.178665

The latency result is a local Codespace microbenchmark only.

## Action 18.13 — Confidence intervals and uncertainty

Result: PASS WITH EXPLICIT UNCERTAINTY.

Membership attack accuracy:

- estimate: 0.916667
- 95% Wilson interval: [0.646114, 0.985135]

No production risk bound is claimed.

## Action 18.14 — Transferability limits

Result: PASS.

Quantitative Phase-18 results are not directly transferred to:

- LLMs
- RAG systems
- Onyx
- production AI systems

## Action 18.15 — Reference-tool status

Result: PASS WITH DOCUMENTED GAPS.

- Adversarial Robustness Toolbox executed: FALSE
- Privacy Meter executed: FALSE
- TensorFlow Privacy executed: FALSE

Host discovery:

- Python binary: NOT_AVAILABLE
- Python version: NOT_AVAILABLE
- ART importable: false
- Privacy Meter importable: false
- TensorFlow Privacy importable: false

No package was automatically installed.

## Action 18.16 — Final benchmark

Result: PASS.

Phase 18 now contains evidence for all 16 planned actions.

## Final Phase-18 status

Actions:

16 / 16

Progress:

100%

Core synthetic/local objectives:

VERIFIED

Reference-tool execution gaps:

1. Adversarial Robustness Toolbox
2. Privacy Meter
3. TensorFlow Privacy

Full reference-tool execution:

FALSE

Production assessment:

FALSE

Quantitative transfer to LLMs:

FALSE

Quantitative transfer to Onyx:

FALSE

Accurate status:

COMPLETE_WITH_DOCUMENTED_REFERENCE_TOOL_GAPS

PHASE_18_COMPLETE_WITH_DOCUMENTED_REFERENCE_TOOL_GAPS
