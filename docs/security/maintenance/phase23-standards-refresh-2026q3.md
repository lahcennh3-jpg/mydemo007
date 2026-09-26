# Phase 23 — 2026 Q3 Security-Standards Refresh

Review timestamp UTC:

`2026-09-26T13:41:31Z`

## Purpose

Reassess the project's security-framework baseline using current official
sources rather than assuming that earlier framework references remain current.

## Sources reviewed

### NIST AI Risk Management Framework

Official source:

https://www.nist.gov/itl/ai-risk-management-framework

Relevant project baseline:

- NIST AI RMF;
- NIST AI 600-1 Generative Artificial Intelligence Profile.

Status:

`REVIEWED_CURRENT_OFFICIAL_SOURCE`

### NIST SP 800-218A

Official source:

https://csrc.nist.gov/pubs/sp/800/218/a/final

Relevant project baseline:

- Secure Software Development Framework;
- GenAI / dual-use foundation-model community profile.

Status:

`REVIEWED_CURRENT_OFFICIAL_SOURCE`

### OWASP Top 10 for LLM Applications 2026

Official source:

https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/

Status:

`REVIEWED_2026_EDITION`

### OWASP Top 10 for Agentic Applications 2026

Official source:

https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/

Status:

`REVIEWED_2026_EDITION`

### OWASP Agent Control Standard

Official source:

https://genai.owasp.org/resource/agent-control-standard-acs/

Status:

`REVIEWED_CURRENT_OFFICIAL_SOURCE`

### OWASP ASVS

Official source:

https://owasp.org/projects/asvs

Expected project reference family:

`ASVS_5.x`

Status:

`REVIEWED_CURRENT_OFFICIAL_SOURCE`

## Security-engineering decision

The project must not assume that historical mappings remain sufficient after
framework revisions.

Framework changes are treated as inputs to:

1. control mapping;
2. threat-model maintenance;
3. evaluation-set maintenance;
4. agent/tool/MCP control maintenance;
5. web/API security control maintenance;
6. evidence and claim-ledger maintenance.

## Evidence integrity

The retrieved source bodies are not committed wholesale.

Instead, retrieval provenance, timestamps, byte sizes and SHA-256 fingerprints
are preserved in:

`docs/security/evidence/phase23-batch-b-source-fingerprints.tsv`

This provides evidence of what was reviewed without copying entire external
documents into the repository.

## Result

ACTION_23.7=PASS_CURRENT_STANDARDS_REFRESH
