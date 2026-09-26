# Phase 23 — Security Change Trigger Register

## Trigger T23-001 — Security-standard change

Examples:

- new framework release;
- revised framework requirement;
- deprecated control;
- new AI/agent security guidance.

Required response:

1. identify delta;
2. determine applicability;
3. map affected controls;
4. update tests/evidence where required.

---

## Trigger T23-002 — Onyx architecture change

Examples:

- new service;
- removed service;
- changed trust boundary;
- changed authentication path;
- changed tenant boundary;
- changed retrieval flow;
- changed tool/agent flow.

Required response:

- architecture review;
- threat-model delta;
- authorization review;
- test-selection review.

---

## Trigger T23-003 — Onyx release change

Required response:

- identify changed security-relevant surfaces;
- inspect relevant release/code delta;
- select regression tests;
- preserve evidence.

---

## Trigger T23-004 — Dependency change

Required response:

- provenance;
- version change;
- advisory/risk review;
- integrity validation;
- regression decision.

---

## Trigger T23-005 — Model change

Required response:

- model/provider/version provenance;
- behavioral-security reassessment;
- evaluation refresh;
- privacy/security delta analysis.

---

## Trigger T23-006 — Dataset or retrieval-source change

Required response:

- source provenance;
- access-control review;
- poisoning risk review;
- tenant-isolation review;
- data-exposure review.

---

## Trigger T23-007 — Prompt change

Required response:

- prompt delta;
- trust/instruction-boundary review;
- prompt-injection regression;
- output/control review.

---

## Trigger T23-008 — Authorization or policy change

Required response:

- policy diff;
- subject/object/action mapping;
- tenant-boundary review;
- negative authorization tests;
- regression evidence.

---

## Trigger T23-009 — Agent/tool/MCP capability change

Required response:

- capability inventory;
- permission review;
- tool input validation review;
- human-approval review;
- abuse-case refresh;
- audit/rollback review.

---

## Trigger T23-010 — Security incident

Required response:

- evidence preservation;
- triage;
- scope;
- containment;
- recovery;
- root-cause analysis;
- remediation;
- regression;
- threat-model update;
- portfolio update only when disclosure is appropriate.

---

## Trigger T23-011 — New verified finding

Required response:

- finding evidence;
- remediation ownership;
- regression test;
- residual-risk decision;
- claim-ledger reassessment.

---

## Trigger T23-012 — Capstone promotion

Required response:

- manual evidence review;
- claim verification;
- sanitization;
- publication review;
- portfolio status change only after passing gates.

---

## Trigger T23-013 — Independent reproduction completed

Required response:

- independently generated evidence;
- provenance review;
- comparison with assisted implementation;
- independence claim review.

Phase 21 Action 21.17 remains BLOCKED_INDEPENDENT until separately
satisfied.
