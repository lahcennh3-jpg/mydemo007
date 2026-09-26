# Phase 25 — Final Technical Review Demo Guide

## 5-minute version

### Minute 1 — Scope and architecture

Explain:

- authorized local/synthetic assessment;
- Onyx as the flagship AI application;
- application/API/data/agent/tool/RAG boundaries;
- evidence-first workflow.

### Minute 2 — Threat and test design

Show:

- threat model;
- Phase 24 evaluation matrix;
- why PASS, BLOCKED and INCONCLUSIVE are treated differently.

### Minute 3 — Concrete security evidence

Demonstrate:

- authentication negative paths;
- cross-user BOLA retest;
- tool/MCP authority controls;
- sensitive-data controls.

### Minute 4 — Operations and release

Show:

- deployment-integrity regression;
- synthetic detection controls;
- incident-response tabletop;
- residual-risk register;
- conditional release decision.

### Minute 5 — Limitations and transfer

Explain:

- five blocked evaluation families;
- no production-effectiveness claim;
- no independent-completion claim;
- OpenHands transfer assessment is the next gate.

## Interview answer structure

For any technical question use:

WHAT

→ WHERE

→ WHY

→ THREAT

→ TEST

→ EXPECTED

→ ACTUAL

→ EVIDENCE

→ INTERPRETATION

→ CONTROL

→ RETEST

→ RESIDUAL RISK.

## Do not claim

- independent full reproduction;
- public-production exploitation;
- complete tenant-isolation validation;
- complete RAG/model/prompt validation;
- public-publication approval.

PHASE25_FINAL_DEMO_GUIDE=READY
