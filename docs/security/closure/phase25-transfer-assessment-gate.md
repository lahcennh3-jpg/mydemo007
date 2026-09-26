# Phase 25 — Transfer Assessment Gate

Timestamp UTC:

`2026-09-26T17:16:13Z`

## Target

TRANSFER_TARGET=OpenHands

TRANSFER_PURPOSE=SECOND_PRODUCT_METHOD_TRANSFER

## Current state

OPENHANDS_SOURCE_PINNED=NO

OPENHANDS_SOURCE_PRESENT_IN_EVIDENCE_REPO=NO

OPENHANDS_RUNTIME_BASELINE_ESTABLISHED=NO

OPENHANDS_AUTHORIZATION_SCOPE_ESTABLISHED=NO

OPENHANDS_THREAT_MODEL_TRANSFER_EXECUTED=NO

OPENHANDS_SECURITY_ASSESSMENT_EXECUTED=NO

OPENHANDS_COMPARATIVE_CONTROL_GAP_ANALYSIS_EXECUTED=NO

## Safety gate

Before OpenHands transfer work begins, Phase 25 must establish:

1. exact upstream repository;
2. immutable commit SHA;
3. edition/deployment mode;
4. authorized local/synthetic scope;
5. outbound-network policy;
6. synthetic identities/data;
7. bounded resource ceilings;
8. stop conditions;
9. evidence paths;
10. rollback;
11. comparison rubric against Onyx;
12. no production or third-party active testing.

AUTOMATIC_CLONE=NO

AUTOMATIC_UPGRADE=NO

PUBLIC_TARGET_TESTING=NO

REAL_CREDENTIALS_ALLOWED=NO

REAL_CUSTOMER_DATA_ALLOWED=NO

## Transfer rubric

The future assessment must compare at least:

- architecture/trust boundaries;
- authentication/session model;
- authorization/ownership model;
- tenant/workspace isolation;
- prompt/context boundaries;
- retrieval/memory behavior where applicable;
- agents/tools/actions;
- MCP/integrations where applicable;
- code execution/sandbox boundaries;
- secret handling;
- outbound network/SSRF;
- supply-chain provenance;
- abuse/resource controls;
- observability/detection;
- incident response;
- release/rollback controls;
- residual risk;
- product-specific control gaps.

TRANSFER_GATE=READY_FOR_PINNED_SOURCE_SELECTION

TRANSFER_ASSESSMENT_COMPLETE=NO
