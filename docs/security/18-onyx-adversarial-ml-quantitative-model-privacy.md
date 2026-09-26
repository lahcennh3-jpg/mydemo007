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
