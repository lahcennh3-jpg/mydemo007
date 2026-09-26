# AI Security Engineering Portfolio — Evidence Index

## Purpose

This index presents the security-engineering work in a format suitable
for technical reviewers, hiring teams and prospective clients.

It is an evidence index, not a substitute for the underlying technical
reports.

## Current verification state

Phase 22 Batch A: PASS

Phase 22 Batch B: PASS

Phase 22 Batch C: IN_PROGRESS

Phase 22 complete: NO

Independent Phase 21 completion: NO

Phase 21 Action 21.17:

`BLOCKED_INDEPENDENT`

## Evidence scale

Tracked Phase 0–21 source files scanned:

`643`

Automated evidence-candidate mappings:

`1995`

Important:

An evidence-candidate mapping is not automatically a verified
vulnerability, finding, remediation result or independent reproduction.

## Portfolio principles

This portfolio prioritizes:

- authorization and scope;
- reproducibility;
- evidence preservation;
- attack/defense reasoning;
- remediation verification;
- provenance;
- rollback;
- explicit limitations;
- separation of observation from interpretation;
- separation of assisted work from independent work.

---

# Capstone 1 — Onyx AI Application Security Assessment

Candidate evidence mappings:

`379`

Portfolio package:

`docs/security/portfolio/capstones/01-onyx-ai-application-security-assessment.md`

Focus:

- AI application attack surface;
- APIs and business logic;
- identity and authorization;
- tenant isolation;
- retrieval and RAG security;
- threat modeling;
- remediation and regression reasoning.

Current status:

`DRAFT_EVIDENCE_MAPPED`

---

# Capstone 2 — Continuous Onyx Red-Team and Release Gate

Candidate evidence mappings:

`368`

Portfolio package:

`docs/security/portfolio/capstones/02-continuous-onyx-red-team-release-gate.md`

Focus:

- adversarial AI testing;
- prompt injection;
- RAG abuse;
- agents, tools and MCP;
- regression testing;
- security/release gates;
- evidence and rollback.

Current status:

`DRAFT_EVIDENCE_MAPPED`

---

# Capstone 3 — Secure AI/ML Supply-Chain Pipeline

Candidate evidence mappings:

`352`

Portfolio package:

`docs/security/portfolio/capstones/03-secure-ai-ml-supply-chain-pipeline.md`

Focus:

- dependency provenance;
- artifact provenance;
- model provenance;
- integrity verification;
- build/release controls;
- reproducibility.

Current status:

`DRAFT_EVIDENCE_MAPPED`

---

# Capstone 4 — AI Detection and Incident-Response Lab

Candidate evidence mappings:

`342`

Portfolio package:

`docs/security/portfolio/capstones/04-ai-detection-incident-response-lab.md`

Focus:

- evidence collection;
- detection;
- triage;
- incident reconstruction;
- containment;
- recovery;
- remediation;
- technical and executive communication.

Current status:

`DRAFT_EVIDENCE_MAPPED`

---

# Capstone 5 — Adversarial ML and Privacy Benchmark

Candidate evidence mappings:

`189`

Portfolio package:

`docs/security/portfolio/capstones/05-adversarial-ml-privacy-benchmark.md`

Focus:

- adversarial ML;
- quantitative security evaluation;
- privacy;
- measurement;
- uncertainty;
- reproducibility.

Current status:

`DRAFT_EVIDENCE_MAPPED`

---

# Capstone 6 — Secure Local AI/Model-Serving Platform

Candidate evidence mappings:

`365`

Portfolio package:

`docs/security/portfolio/capstones/06-secure-local-ai-model-serving-platform.md`

Focus:

- bounded local deployment;
- model-serving security;
- service isolation;
- network controls;
- configuration security;
- runtime controls;
- authorization boundaries.

Current status:

`DRAFT_EVIDENCE_MAPPED`

---

# How a technical reviewer should evaluate this portfolio

Recommended review order:

1. authorization and rules of engagement;
2. architecture / reverse engineering;
3. threat model;
4. test methodology;
5. raw evidence;
6. findings or security conclusions;
7. remediation;
8. regression evidence;
9. limitations;
10. provenance.

Do not infer independent reproduction from assisted evidence.

Do not infer public-publication approval from the presence of a
portfolio artifact.
