# Phase 22 — AI Security Interview Scenario Bank

## Response framework

For technical interview scenarios answer in this order:

1. scope and authorization;
2. system / asset;
3. trust boundary;
4. threat;
5. hypothesis;
6. safe test;
7. expected result;
8. actual evidence;
9. interpretation;
10. remediation;
11. regression;
12. residual risk;
13. limitation.

---

# Scenario 1 — Cross-Tenant AI Conversation Access

An AI SaaS product has multiple organizations.

A user supplies a conversation identifier belonging to another tenant.

## Discuss

- object ownership;
- authentication versus authorization;
- server-side authorization;
- tenant-scoped queries;
- direct-object-reference risk;
- negative tests;
- audit logging;
- regression tests.

## Evidence discipline

Do not claim the project found this defect unless an original source
artifact explicitly records it.

---

# Scenario 2 — Prompt Injection Through Retrieved Content

A trusted user asks an AI assistant to summarize an indexed document.
The document contains adversarial instructions.

## Discuss

- data/instruction boundary;
- untrusted retrieval;
- prompt hierarchy;
- tool permissions;
- output controls;
- document provenance;
- detection;
- regression tests.

---

# Scenario 3 — Agent Requests a Dangerous Tool Action

An AI agent receives text instructing it to invoke a privileged tool.

## Discuss

- model output versus authorization;
- capability design;
- tool allowlists;
- argument validation;
- least privilege;
- human approval;
- idempotency;
- audit evidence;
- rollback.

---

# Scenario 4 — Compromised AI Dependency or Artifact

A model-serving pipeline downloads a changed dependency or artifact.

## Discuss

- provenance;
- trusted source;
- pinned versions;
- digests;
- signatures where available;
- reproducible build/deployment;
- quarantine;
- rollback;
- incident investigation.

---

# Scenario 5 — Suspected AI Data Exposure Incident

Sensitive synthetic information appears in a generated response.

## Discuss

- preserve evidence;
- identify request/session/user scope;
- establish data lineage;
- determine whether retrieval, memory, prompt or model behavior was
  involved;
- contain exposure;
- revoke access if relevant;
- remediate;
- regression test;
- communicate impact with uncertainty.

---

# Scenario 6 — Adversarial ML Benchmark

A stakeholder asks:

"Is the model secure?"

## Discuss

Why a single yes/no answer is weak.

Define:

- attack hypothesis;
- dataset;
- baseline;
- metric;
- sample size;
- defensive condition;
- uncertainty;
- limitations;
- reproduction conditions.

---

# Scenario 7 — Secure Local Model Server

A local model server is reachable by multiple internal services.

## Discuss

- authentication;
- authorization;
- network exposure;
- tenant/data separation;
- secrets;
- configuration;
- logs;
- dependency security;
- resource exhaustion;
- model/artifact provenance.

---

# Scenario 8 — Security Finding Under Release Pressure

A release is approaching and a security issue remains unresolved.

## Discuss

- evidence quality;
- exploit preconditions;
- affected assets;
- severity inputs;
- compensating controls;
- regression coverage;
- ownership;
- deadline;
- risk acceptance authority;
- rollback;
- documented residual risk.

Do not invent organizational authority that you do not have.

---

# Scenario 9 — Explain a Failed Security Test

A test produces an unexpected result.

## Good response pattern

1. preserve raw evidence;
2. avoid immediately labeling it a vulnerability;
3. reproduce;
4. verify fixtures;
5. verify authorization state;
6. check environmental differences;
7. isolate the cause;
8. document actual versus expected;
9. update the hypothesis;
10. only then classify the result.

---

# Scenario 10 — Explain Your Role

Use evidence-specific language.

Prefer:

- designed;
- tested;
- reproduced;
- documented;
- mapped;
- reviewed;
- implemented;
- verified;

only when the source evidence supports the verb.

Where assistance materially contributed, state that assistance clearly.

Do not claim independent reproduction while the independent gate
remains blocked.

---

## Independence status

Independent project completion: NO

Phase 21 Action 21.17: BLOCKED_INDEPENDENT

Interview answers must not represent assisted work as independently
reproduced work.
