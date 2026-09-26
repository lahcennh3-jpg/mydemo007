# Phase 24 — Batch C Security-Control Regression Evidence

Timestamp UTC: 2026-09-26T17:09:29Z

SOURCE_HEAD=fcc7baee23707eea256bfd3ac20615d99d3c7830

RUNNER_SHA256=a3b445b743a096bdad43f4b3e0cac71cb2bfe8664038d2cd397a8940032c8ad9

CONTROL_LOG_SHA256=9eb40edfdcbc5253115fc6e7a2343da9a2cf7dbc83d3d57a0ba68d83dd497d27

NETWORK_BOUNDARY=OFFLINE_OR_INTERNAL_ONLY

REAL_CUSTOMER_DATA_USED=NO

REAL_CREDENTIALS_USED=NO

## Evaluation results

EV23-005=BLOCKED

EV23-006=BLOCKED

EV23-007=PASS

EV23-008=PASS

EV23-009=PASS

EV23-010=BLOCKED

EV23-011=PASS

EV23-012=PASS

EV23-013=PASS

## Scope boundaries

EV23-005 requires controlled synthetic indexing and retrieval poisoning runtime.

EV23-006 requires controlled model-generation behavior.

EV23-007 validates current tool-authority code boundaries. Live autonomous
agent behavior is not claimed.

EV23-008 validates MCP authentication/header/authority boundaries with network
disabled. Live external MCP-server behavior is not claimed.

EV23-009 combines current redaction/trace controls with local runtime checks
that the synthetic USER_AUTH_SECRET is absent from tested public/error
responses and API logs.

EV23-010 requires a controlled model/provider runtime.

EV23-011 validates bounded resource, queue, duplicate-work and concurrency
controls. Production-scale availability is not claimed.

EV23-012 validates the current API image identity, schema revision, health,
internal-only network boundary and ignored local secret configuration against
the frozen Batch A baseline. It is not a vulnerability/CVE scan.

EV23-013 re-executes the synthetic detection-control gate and its adversarial
benign-noise variant. Production detection effectiveness is not claimed.

## Batch counts

BATCH_C_EXECUTED_FAMILIES=6

BATCH_C_PASS_FAMILIES=6

BATCH_C_FAIL_FAMILIES=0

BATCH_C_INCONCLUSIVE_FAMILIES=0

BATCH_C_BLOCKED_FAMILIES=3

CURRENT_RUNTIME_REGRESSION_EXECUTED=8

TOTAL_PASS_FAMILIES=8

TOTAL_FAIL_FAMILIES=0

TOTAL_INCONCLUSIVE_FAMILIES=0

TOTAL_BLOCKED_FAMILIES=5

TOTAL_NOT_EXECUTED_FAMILIES=1

PHASE24_BATCH_C=COMPLETE_WITH_BLOCKED_DEPENDENCIES

CURRENT_RUNTIME_REGRESSION_COMPLETE=NO

ACTION_24.19=PASS_BATCH_C_EVIDENCE_CHECKPOINT

NEXT=BATCH_D_IR_FINDINGS_REMEDIATION_RELEASE_ASSURANCE
