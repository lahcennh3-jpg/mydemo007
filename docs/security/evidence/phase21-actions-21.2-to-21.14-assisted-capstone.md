# Phase 21 — Actions 21.2–21.14 — Assisted Professional Capstone

Recorded: 2026-09-26T12:24:24Z

Repository SHA:

`7ddd494f662e902d852f3e798dd49e4ac4f314fb`

## Integrity classification

This execution used assistant-supplied commands and assistant-assisted review
structure.

It demonstrates completion of the technical/professional exercises in assisted
mode.

It does not demonstrate independent command selection or independent
professional judgment.

ASSISTANT_COMMANDS_USED=YES
INDEPENDENT_ASSESSMENT=NOT_CLAIMED

---

# Action 21.2 — Security behavior reproduction

The checked-in Phase 21 regression test reproduced the Phase 17 synthetic
approval-control behavior.

Observed result:

```text
core_pipeline_verification=PASS
production_authorized=false
external_mcp_used=false
unapproved_change_blocked=true
rollback_verified=true
revocation_verified=true
retirement_verified=true
reference_tool_execution_gaps=4
phase17_scope=synthetic-local-lab
VERIFY_FAIL: policy approval
baseline_control=PASS
invalid_policy_rejected=PASS
original_repository_modified=NO
network_required=NO
phase21_verifier_regression=PASS
```

The valid baseline passed.

The deliberately invalid copied policy state was rejected.

The original repository was not modified and the regression required no
network access.

ACTION_21.2=PASS_ASSISTED_REPRODUCTION

---

# Action 21.3 — Command explanation

## Git identity checks

Purpose:
confirm the assessment is operating against the expected branch, SHA, and
clean repository.

Target:
the Phase 21 repository.

Expected effect:
read-only Git metadata inspection.

Evidence:
matching branch, expected SHA, and clean worktree.

Failure signal:
branch mismatch, SHA mismatch, or modified/untracked files.

Rollback:
none required because the operations are read-only.

## Phase 17 regression execution

Purpose:
reproduce a known synthetic security-control behavior.

Target:
the committed Phase 17 verifier and copied policy fixture.

Expected effect:
baseline passes and invalid approval state is rejected.

Evidence:

- baseline_control=PASS
- invalid_policy_rejected=PASS
- phase21_verifier_regression=PASS

Failure signal:
baseline rejection, mutation acceptance, timeout, or missing PASS markers.

Rollback:
temporary exported security fixtures are removed automatically.

## sed/grep source inspection

Purpose:
perform bounded source review without changing code.

Target:

- `backend/onyx/external_apps/matching/engine.py`
- `backend/onyx/sandbox_proxy/request_evaluator.py`
- `backend/onyx/sandbox_proxy/addons/gate.py`

Expected effect:
display and inspect policy, identity, session, target, approval, and proxy
decision logic.

Evidence:
relevant security-control paths were present in the inspected regions.

Failure signal:
missing source files or missing expected security-control logic.

Rollback:
none required because inspection is read-only.

ACTION_21.3=PASS_ASSISTED_EXPLANATION

---

# Action 21.4 — Transfer method

The Phase 17 verification technique was transferred into the Phase 21
regression test.

Method:

1. export the committed security evidence into an isolated temporary tree;
2. verify the known-good baseline;
3. change only the copied approval-policy state;
4. rerun the verifier;
5. require fail-closed rejection;
6. preserve the original repository.

The transferred method successfully detected the invalid approval state.

ACTION_21.4=PASS_ASSISTED

---

# Action 21.5 — Security code review

Reviewed files:

- `backend/onyx/external_apps/matching/engine.py`
- `backend/onyx/sandbox_proxy/request_evaluator.py`
- `backend/onyx/sandbox_proxy/addons/gate.py`

Source hashes:

```text
matching=643f1fe4d19668ef737041f6f7f713b77b0eea02ba01b8d8d11dca5c1e437fa9
request_evaluator=87e923898ff2c76eca93fe6781b161d39314a9f13a7c264e14edcb07a834eab0
gate=d666ce28e46165c1d265f1ba563934308f34897aa2db275edf8fcbac1781b1ba
```

Review focus:

- action-policy precedence;
- MCP/tool target attribution;
- identity and tenant context;
- session association;
- explicit denial behavior;
- approval checks;
- authority-header handling;
- destination handling;
- failure behavior.

Assessment:

The inspected design applies authorization across several decisions rather
than treating one approval value as sufficient authority.

The reviewed path contains separate concepts for policy selection,
user/tenant/session context, tool/target interpretation, approval handling,
proxy enforcement, and destination processing.

This layered approach reduces reliance on any single untrusted request field.

Limit:

This action is a bounded source review and does not prove every production
deployment path.

ACTION_21.5=PASS_ASSISTED_REVIEW

---

# Action 21.6 — Architecture review

Reviewed logical path:

```text
sandbox/tool request
        |
        v
proxy gate
        |
        v
request classification
        |
        v
user / tenant / session context
        |
        v
MCP target + tool attribution
        |
        v
policy decision
        |
        v
approval decision
        |
        v
credential / destination processing
        |
        v
external action
```

Important trust boundaries:

- sandbox-to-proxy boundary;
- user/session binding;
- tenant context;
- target attribution;
- policy evaluation;
- approval state;
- delegated credentials;
- destination enforcement.

Architecture security objective:

Untrusted request content must not be sufficient to grant external-action
authority.

Each security-sensitive transition should be derived from trusted application
state and fail closed when attribution cannot be established.

ACTION_21.6=PASS_ASSISTED_REVIEW

---

# Action 21.7 — Design and misuse-case review

Misuse cases reviewed:

- malformed tool/RPC request;
- unknown target;
- ambiguous target;
- mixed-policy request batch;
- forged session identifier;
- stale session identifier;
- injected authority-related headers;
- internal/private destination attempt;
- request without required approval;
- failure after approval but before execution;
- destination resolution changing after initial validation.

Expected secure behavior:

- fail closed on unknown attribution;
- use restrictive policy precedence;
- do not trust caller-supplied authority;
- bind approval to relevant user/session/action context;
- explicitly reject denied operations;
- constrain destination behavior;
- retain observable failure paths.

Trade-off:

Strict fail-closed behavior can reject new or incompletely classified
integrations.

That usability cost is preferable to implicitly authorizing an ambiguous
external action.

ACTION_21.7=PASS_ASSISTED_REVIEW

---

# Action 21.8 — Incident handoff

## Situation

A synthetic Phase 17 approval-policy artifact was deliberately mutated into an
invalid production-approved state.

## Detection

The security verifier rejected the mutation with:

`VERIFY_FAIL: policy approval`

## Scope

Local synthetic Phase 17 fixture only.

No production system or public target was tested.

## Impact

No real security incident occurred.

The exercise proves that this specific synthetic invalid approval state is
detected by the current verifier.

## Containment

Mutation occurred only inside a temporary exported copy.

## Evidence

- baseline verifier PASS;
- invalid policy rejection;
- repository unchanged;
- no network required.

## Recommended follow-up

Retain the regression and rerun it whenever approval-policy semantics or the
Phase 17 verifier changes.

ACTION_21.8=PASS_ASSISTED

---

# Action 21.9 — Technical finding

## Title

Synthetic Phase 17 verifier fails closed on invalid production approval.

## Observation

The known-good policy passes the verifier.

Changing the copied policy to an invalid
`production_approved=true` state causes the verifier to reject the artifact.

## Evidence

`baseline_control=PASS`

`invalid_policy_rejected=PASS`

`VERIFY_FAIL: policy approval`

## Security significance

The local evidence pipeline does not silently accept this invalid
security-policy state.

## Scope limitation

This is a finding about the synthetic Phase 17 verification pipeline.

It is not a confirmed production Onyx vulnerability and does not establish
production control effectiveness.

ACTION_21.9=PASS_ASSISTED

---

# Action 21.10 — Executive summary

A bounded regression reproduced the synthetic Phase 17 approval-control
behavior. The valid baseline passed while a deliberate invalid production
approval state was rejected. The reproduction did not modify the repository
and required no network access. This provides useful regression coverage for
the local security-artifact pipeline but does not establish production Onyx
security effectiveness.

ACTION_21.10=PASS_ASSISTED

---

# Action 21.11 — Remediation prioritization

## Priority 1

Keep the fail-closed approval regression in the repository.

Reason:
an accidental change to approval semantics should be detected immediately.

## Priority 2

Version approval-policy changes together with corresponding verifier changes.

Reason:
policy/verifier drift can create false passes or false failures.

## Priority 3

Expand negative tests when new approval states or security-relevant fields are
introduced.

## Priority 4

Preserve scope language so synthetic findings are not presented as production
vulnerabilities.

ACTION_21.11=PASS_ASSISTED

---

# Action 21.12 — Trade-off defense

Strict approval validation increases maintenance work because intentional
schema or policy changes may require corresponding regression updates.

For security-sensitive approval decisions, that maintenance cost is acceptable.

The safer design is explicit versioned change plus regression updates rather
than permissive fallback behavior.

ACTION_21.12=PASS_ASSISTED

---

# Action 21.13 — Review another safe change

Reviewed contribution:

`docs/security/fixtures/phase21/test-phase17-verifier-regression.sh`

Review result:

- uses a temporary working directory;
- exports committed evidence rather than altering the source repository;
- requires the valid baseline to pass;
- changes only the temporary policy copy;
- requires invalid policy rejection;
- checks the expected verifier failure marker;
- removes temporary files through a trap;
- checks required tooling;
- verifies the original repository is not mutated;
- performs no network-dependent test.

Review comment:

The regression exports the complete committed `docs/security` tree because
the Phase 17 verifier depends on several reports, metadata, configuration, and
fixture artifacts.

That dependency should remain documented so future maintainers do not
incorrectly narrow the export and break the verifier contract.

ACTION_21.13=PASS_ASSISTED_REVIEW

---

# Action 21.14 — Response to review comment

Review response:

Accepted.

A prior narrower export omitted dependencies required by the Phase 17
verification pipeline.

The complete `docs/security` export is therefore intentional.

The scope remains bounded because:

- only committed repository material is exported;
- the export is temporary;
- the source repository is unchanged;
- the temporary directory is deleted after the test.

If Phase 17 later gains an explicit dependency manifest, the regression should
be narrowed to that declared dependency set.

ACTION_21.14=PASS_ASSISTED_RESPONSE

---

# Safety and integrity result

REAL_CUSTOMER_DATA_USED=NO
REAL_CREDENTIALS_USED=NO
REAL_EXTERNAL_AI_API_USED=NO
PUBLIC_TARGET_TESTING=NO

ACTION_21.2=PASS_ASSISTED_REPRODUCTION
ACTION_21.3=PASS_ASSISTED_EXPLANATION
ACTION_21.4=PASS_ASSISTED
ACTION_21.5=PASS_ASSISTED_REVIEW
ACTION_21.6=PASS_ASSISTED_REVIEW
ACTION_21.7=PASS_ASSISTED_REVIEW
ACTION_21.8=PASS_ASSISTED
ACTION_21.9=PASS_ASSISTED
ACTION_21.10=PASS_ASSISTED
ACTION_21.11=PASS_ASSISTED
ACTION_21.12=PASS_ASSISTED
ACTION_21.13=PASS_ASSISTED_REVIEW
ACTION_21.14=PASS_ASSISTED_RESPONSE

ACTION_21.17=BLOCKED
INDEPENDENT_ASSESSMENT=NOT_CLAIMED

CAPSTONE_RESULT=PASS_ASSISTED
