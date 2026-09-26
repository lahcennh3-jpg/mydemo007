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
| 21.1 | Rebuild the lab from a clean environment | PASS_ASSISTED_REBUILD |
| 21.2 | Reproduce findings without copied commands | PASS_ASSISTED_REPRODUCTION |
| 21.3 | Explain command purpose, target, effect, evidence, failure signal, rollback | PASS_ASSISTED_EXPLANATION |
| 21.4 | Transfer one method to an unfamiliar AI application | PASS_ASSISTED |
| 21.5 | Perform security code review | PASS_ASSISTED_REVIEW |
| 21.6 | Perform architecture review | PASS_ASSISTED_REVIEW |
| 21.7 | Perform design review | PASS_ASSISTED_REVIEW |
| 21.8 | Perform incident handoff | PASS_ASSISTED |
| 21.9 | Write technical findings | PASS_ASSISTED |
| 21.10 | Write executive summaries | PASS_ASSISTED |
| 21.11 | Prioritize remediation | PASS_ASSISTED |
| 21.12 | Defend trade-offs | PASS_ASSISTED |
| 21.13 | Review another safe change | PASS_ASSISTED_REVIEW |
| 21.14 | Respond to review comments | PASS_ASSISTED_RESPONSE |
| 21.15 | Submit safe documentation/test/hardening/bug-fix contribution | PASS_SAFE_TEST_CONTRIBUTION |
| 21.16 | Follow upstream security policy for suspected vulnerabilities | PASS_POLICY_HANDLING |
| 21.17 | Independently reproducible assessment and reviewed contribution | BLOCKED |

PHASE21_STATUS=ASSISTED_CAPSTONE_COMPLETE_INDEPENDENT_GATE_BLOCKED

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

## Accelerated Batch C checkpoint

PHASE21_BATCH_C_CHECKPOINT=RECORDED

- 21.15 safe regression/test contribution: PASS
- 21.16 upstream security-policy handling: PASS
- 21.17 independently reproducible assessment: BLOCKED

The Action 21.15 regression contribution required two implementation repairs:

1. exporting the complete committed docs/security dependency tree;
2. replacing an unavailable Python mutation helper with jq.

The resulting contribution successfully verifies both the valid baseline and
the fail-closed invalid approval condition.

The remaining Phase 21 blocker is the clean-environment reconstruction
required by Action 21.1.

BATCH_C_RESULT=PARTIAL_PASS_INDEPENDENT_GATE_BLOCKED
PHASE21_COMPLETE=NO
NEXT=RESTORE_ACTION_21_1_THEN_REPEAT_21_17

## Action 21.1 assisted clean-rebuild checkpoint

PHASE21_ACTION_21_1_ASSISTED_CHECKPOINT=RECORDED

Technical rebuild evidence:

- clean detached source worktree: PASS
- fresh Compose runtime: PASS
- fresh PostgreSQL volume: PASS
- five Lite services healthy: PASS
- PostgreSQL readiness: PASS
- Onyx API health: PASS
- code-interpreter health: PASS
- internal Compose network: PASS
- no host-published ports: PASS
- digest-pinned executor: PASS
- rollback: PASS

This was an assisted execution.

ACTION_21_1=PASS_ASSISTED_REBUILD
INDEPENDENT_REBUILD=NOT_CLAIMED
PHASE21_COMPLETE=NO
NEXT=INDEPENDENT_REPRODUCTION_ROUND

## Assisted Actions 21.2–21.14 completion checkpoint

PHASE21_ASSISTED_PROFESSIONAL_CAPSTONE=PASS

Actions 21.2–21.14 now have complete assisted professional-practice evidence.

Demonstrated:

- synthetic security-behavior reproduction;
- command-purpose and rollback explanation;
- method transfer;
- security code review;
- architecture review;
- design/misuse-case review;
- incident handoff;
- technical finding;
- executive summary;
- remediation prioritization;
- trade-off defense;
- safe-change review;
- review response.

Assistant-supplied commands and analysis structure were used.

The independent gate is therefore intentionally unchanged.

ACTION_21.17=BLOCKED_ASSISTED_CAPSTONE
INDEPENDENT_ASSESSMENT=NOT_CLAIMED
PHASE21_COMPLETE=NO
NEXT=INDEPENDENT_REPRODUCTION_ROUND
