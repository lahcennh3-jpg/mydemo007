# Phase 22 — Technical Demonstration Scripts

## Purpose

These scripts provide short technical walkthrough structures for
interviews, portfolio reviews and client calls.

They are demonstration structures.

They do not create new findings.

Before describing a specific technical result, open the original source
artifact and verify that the statement is directly supported.

---

# Demo 1 — AI Application Security Assessment

Target duration:

2–5 minutes.

## Opening

Explain:

- what system was under review;
- the authorized lab boundary;
- why AI application security extends beyond prompt testing;
- where identity, APIs, retrieval and tenant isolation enter the attack
  surface.

## Show

1. architecture or reverse-engineering evidence;
2. threat-model evidence;
3. authorization / API / RAG evidence;
4. one evidence-backed test;
5. remediation or defensive reasoning;
6. limitations.

## Say only when directly evidenced

- what was observed;
- whether the test passed or failed;
- whether remediation was actually verified.

## Do not say

- that a keyword-mapped candidate is automatically a vulnerability;
- that public Onyx infrastructure was tested;
- that assisted reproduction was independent.

---

# Demo 2 — Continuous AI Red Team and Release Gate

Target duration:

2–5 minutes.

## Opening

Explain the lifecycle:

threat hypothesis
→ bounded adversarial test
→ evidence
→ defensive change
→ regression check
→ release decision.

## Show

1. an adversarial scenario;
2. the safety boundary;
3. execution or test evidence;
4. defensive control;
5. regression evidence;
6. release-gate reasoning.

## Strong interview theme

Security testing should become a repeatable engineering control rather
than a one-time penetration-test document.

---

# Demo 3 — AI/ML Supply-Chain Security

Target duration:

2–5 minutes.

## Opening

Explain why AI systems inherit traditional software supply-chain risks
and add model/artifact provenance risks.

## Show

1. source or artifact provenance;
2. hash/integrity evidence;
3. dependency or build controls;
4. release verification;
5. rollback/reproducibility evidence.

## Required limitation

Do not imply cryptographic signing, SBOM coverage or model provenance
was implemented unless the referenced source explicitly proves it.

---

# Demo 4 — AI Detection and Incident Response

Target duration:

2–5 minutes.

## Opening

Describe the difference between:

- attack testing;
- detection;
- incident response.

## Walkthrough

signal
→ evidence collection
→ triage
→ scope
→ containment
→ recovery
→ remediation
→ lessons learned.

## Show

Only evidence-backed artifacts.

If the underlying event is synthetic, call it synthetic.

---

# Demo 5 — Adversarial ML and Privacy Benchmark

Target duration:

2–5 minutes.

## Opening

Explain that AI security conclusions should use measurements rather than
only anecdotes.

## Walkthrough

1. hypothesis;
2. benchmark definition;
3. metric;
4. bounded test;
5. result;
6. uncertainty;
7. security interpretation;
8. limitations.

## Required caution

Do not quote a numerical security result unless the original benchmark
artifact supports that exact result.

---

# Demo 6 — Secure Local AI / Model Serving

Target duration:

2–5 minutes.

## Opening

Explain why local model serving still has:

- network boundaries;
- configuration risk;
- authorization requirements;
- dependency risk;
- runtime risk;
- data exposure risk.

## Show

1. bounded deployment context;
2. service architecture;
3. network or service boundary;
4. configuration/security control;
5. validation evidence;
6. rollback or cleanup.

---

# Universal demo rule

Use this sequence:

WHAT
→ WHERE
→ WHY
→ THREAT
→ TEST
→ EVIDENCE
→ INTERPRETATION
→ DEFENSE
→ VERIFICATION
→ LIMITATION.

Never strengthen a claim merely because it sounds better in an
interview.

---

## Independence status

Independent project completion: NO

Phase 21 Action 21.17: BLOCKED_INDEPENDENT

Assisted work must not be represented as independently reproduced work.
