# Phase 21 — Independent Rebuild, Transfer, and Professional Practice

Parent Phase:

- Phase 20
- final SHA: `d7c999d353f087c58e52dc75c4787e812e730281`

Phase-21 branch:

`security/phase-21-independent-rebuild-transfer-professional-practice`

Assigned scope:

- Onyx;
- previously completed supporting projects;
- no new project required for Phase 21.

## Safety boundary

- authorized local/synthetic testing only;
- no production/customer data;
- no real credentials;
- no public-target testing;
- no real external AI APIs;
- bounded resource use;
- stop on scope uncertainty or unexpected external communication.

## Accelerated execution structure

- Batch A: Actions 21.1–21.7
- Batch B: Actions 21.8–21.14
- Batch C: Actions 21.15–21.17

## Action status

| Action | Requirement | Status |
| --- | --- | --- |
| 21.1 | Rebuild the lab from a clean environment | BLOCKED |
| 21.2 | Reproduce findings without copied commands | ASSISTED_PARTIAL |
| 21.3 | Explain command purpose, target, effect, evidence, failure signal, rollback | ASSISTED_PARTIAL |
| 21.4 | Transfer one method to an unfamiliar AI application | ASSISTED_PARTIAL |
| 21.5 | Perform security code review | ASSISTED_PARTIAL |
| 21.6 | Perform architecture review | ASSISTED_PARTIAL |
| 21.7 | Perform design review | ASSISTED_PARTIAL |
| 21.8 | Perform incident handoff | PENDING |
| 21.9 | Write technical findings | PENDING |
| 21.10 | Write executive summaries | PENDING |
| 21.11 | Prioritize remediation | PENDING |
| 21.12 | Defend trade-offs | PENDING |
| 21.13 | Review another safe change | PENDING |
| 21.14 | Respond to review comments | PENDING |
| 21.15 | Submit safe documentation/test/hardening/bug-fix contribution | PENDING |
| 21.16 | Follow upstream security policy for suspected vulnerabilities | PENDING |
| 21.17 | Independently reproducible assessment and reviewed contribution | PENDING |

PHASE21_STATUS=BATCH_A_BLOCKED_ASSISTED_SCOPE

NEXT=COMPLETE_LOCAL_REBUILD_AND_INDEPENDENT_ASSESSMENT

## Batch A checkpoint

See `docs/security/evidence/phase21-batch-a-assisted-assessment.md`.
The full rebuild and independent assessment remain open.

## Action 21.4 assisted verifier checkpoint

The Phase 17 synthetic pipeline verifier passed in an isolated export.
A changed policy approval flag was rejected with exit 1. See
`docs/security/evidence/phase21-action-21.4-verifier-transfer.txt`.
Action 21.4 remains assisted and partial pending independent assessment.

## Accelerated Batch B checkpoint

PHASE21_BATCH_B_ASSISTED_DRAFTS=RECORDED

Actions prepared/exercised:

- 21.4 transferred verifier: PASS_ASSISTED
- 21.8 engineering handoff: ASSISTED_DRAFT
- 21.9 technical finding: ASSISTED_DRAFT
- 21.10 executive summary: ASSISTED_DRAFT
- 21.11 remediation prioritization: ASSISTED_DRAFT
- 21.12 trade-off defense: ASSISTED_DRAFT
- 21.13 review: ASSISTED_DRAFT
- 21.14 review response: ASSISTED_DRAFT

The full clean-environment independent rebuild remains open.

BATCH_B_RESULT=ASSISTED_DRAFTS_READY
NEXT=PHASE21_INDEPENDENT_REBUILD_OR_BATCH_C_PREPARATION
