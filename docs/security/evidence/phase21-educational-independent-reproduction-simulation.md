# Phase 21 — Educational Independent-Reproduction Simulation

Recorded: 2026-09-26T12:45:08Z

Source commit:

`6eeae1bf61c75823a4eec6690ed1862184454e46`

## Classification

This document simulates the complete independent reproduction round for
educational purposes.

The assistant supplied the commands, analysis, findings, architecture review,
design review, handoff, prioritization, and conclusions.

Therefore this is not independent evidence.

EDUCATIONAL_SIMULATION=YES
ASSISTANT_PERFORMED_ASSESSMENT=YES
INDEPENDENT_ASSESSMENT=NOT_CLAIMED

## Technical results

CLEAN_ENVIRONMENT=PASS
FRESH_RUNTIME=PASS
ALL_FIVE_SERVICES_HEALTHY=PASS
DATABASE_READY=PASS
API_HEALTH=PASS
CODE_INTERPRETER_HEALTH=PASS
NETWORK_ISOLATION=PASS
HOST_PORT_EXPOSURE=NONE
SECURITY_REPRODUCTION=PASS
CODE_REVIEW=PASS_EDUCATIONAL
ARCHITECTURE_REVIEW=PASS_EDUCATIONAL
DESIGN_REVIEW=PASS_EDUCATIONAL
INCIDENT_HANDOFF=PASS_EDUCATIONAL
TECHNICAL_FINDING=PASS_EDUCATIONAL
EXECUTIVE_SUMMARY=PASS_EDUCATIONAL
REMEDIATION_PRIORITIZATION=PASS_EDUCATIONAL
TRADEOFF_ANALYSIS=PASS_EDUCATIONAL
SAFE_CHANGE_REVIEW=PASS_EDUCATIONAL
ROLLBACK=PASS

## Service evidence

```text
SERVICE=relational_db RUNNING=true HEALTH=healthy
SERVICE=api_server RUNNING=true HEALTH=healthy
SERVICE=web_server RUNNING=true HEALTH=healthy
SERVICE=code-interpreter RUNNING=true HEALTH=healthy
SERVICE=nginx RUNNING=true HEALTH=healthy

```

## Database evidence

```text
/var/run/postgresql:5432 - accepting connections
```

## API evidence

```text
status_code=200
{"success":true,"message":"ok","data":null}
```

## Code interpreter

```text
{"message": null, "status": "ok", "version": "0.4.7"}
```

## Security reproduction

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

## Security findings

```text
FINDING_1:
Matched actions are ordered by policy severity and the governing action
determines the decision-driving policy.

FINDING_2:
MCP request attribution uses tenant-scoped database context and user-accessible
MCP servers.

FINDING_3:
Unclassifiable attributed MCP requests become explicit DENY actions.

FINDING_4:
Proxy/session authority headers are stripped before forwarding.

FINDING_5:
Internal destination blocking occurs at multiple points, including near
connection establishment.

FINDING_6:
ASK requests without a resolvable active session fail with a denial path.

FINDING_7:
The Phase 17 synthetic approval verifier rejects the deliberately invalid
production approval state.

RESIDUAL_DESIGN_LIMITATION:
The source documents a residual DNS re-resolution/rebinding window. This
exercise does not demonstrate exploitability and therefore does not classify
it as a confirmed vulnerability.
```

## Architecture analysis

```text
Architecture path:

sandbox request
 -> proxy gate
 -> target/request classification
 -> user + tenant + session context
 -> tool/action policy
 -> approval state
 -> credential handling
 -> destination enforcement
 -> external action

Primary trust boundaries:

1. sandbox to proxy;
2. request to authenticated identity;
3. identity to tenant context;
4. request to target/tool attribution;
5. attribution to policy;
6. policy to approval;
7. approval to credential delegation;
8. credential-bearing request to destination.

Security goal:

No untrusted request field should independently grant external-action
authority.
```

## Design review

```text
Misuse cases:

- malformed RPC/tool call;
- unclassified tool call;
- ambiguous MCP target;
- mixed-policy action batch;
- forged session tag;
- stale session;
- internal destination request;
- user rejection;
- missing active session;
- approval dispatch failure;
- credential-resolution failure;
- destination re-resolution.

Desired response:

- fail closed;
- apply restrictive policy;
- bind decisions to trusted context;
- reject internal destinations;
- avoid forwarding internal authority metadata;
- preserve observable error paths.
```

## Incident handoff

```text
Situation:
A synthetic approval-policy artifact was deliberately changed to an invalid
production-approved state.

Detection:
The Phase 17 verifier rejected it with VERIFY_FAIL: policy approval.

Scope:
Local synthetic fixture only.

Impact:
No real incident or customer impact.

Containment:
Mutation occurred in temporary exported data.

Evidence:
baseline_control=PASS
invalid_policy_rejected=PASS

Recommended action:
Keep the regression test and rerun it whenever approval-policy semantics or
the verifier changes.
```

## Technical finding

```text
Title:
Synthetic approval verifier rejects invalid production approval.

Observation:
The known-good baseline passes. Changing production_approved to true in the
temporary policy copy causes the verifier to reject the artifact.

Security significance:
This demonstrates a fail-closed constraint in the synthetic Phase 17 evidence
pipeline.

Limitation:
This does not establish production Onyx control effectiveness.
```

## Executive summary

```text
The clean Onyx Lite lab was reconstructed successfully using a fresh runtime
namespace and locally cached immutable images. All five expected services
became healthy, PostgreSQL and application health probes passed, the Compose
network remained internal, and no host-facing service ports were exposed.

A synthetic approval-control regression also passed its valid baseline and
rejected an invalid approval-state mutation. Source review showed multiple
fail-closed authorization controls across MCP target attribution, policy
selection, session resolution, approval handling, and destination enforcement.

The results apply to the local educational security lab and must not be
interpreted as a production Onyx security certification.
```

## Remediation

```text
P1 — Preserve fail-closed approval regression.

P2 — Keep policy/verifier changes versioned together.

P3 — Expand negative tests for new approval states and MCP request forms.

P4 — Maintain explicit tenant/user/session attribution tests.

P5 — Continue testing destination-validation race/re-resolution assumptions.

P6 — Keep synthetic-lab findings clearly separated from production claims.
```

## Trade-off analysis

```text
Trade-off:

Strict fail-closed attribution and approval handling can reject legitimate new
or incompletely classified integrations.

Security benefit:

Ambiguous requests do not automatically inherit authority.

Decision:

For external tool execution, explicit classification and approval are safer
than permissive fallback. Usability cost should be handled through clearer
onboarding, observability, and policy configuration rather than weaker default
authorization.
```

## Educational decision

If these same actions, command choices, interpretations, and written
conclusions had been produced by the engineer without assistant execution or
analysis, they would represent the type of evidence required by the Phase 21
independence gate.

Because the assistant performed them here:

SIMULATED_INDEPENDENT_RESULT=PASS_EDUCATIONAL
REAL_INDEPENDENT_RESULT=NOT_DEMONSTRATED
ACTION_21.17=BLOCKED_INDEPENDENT
PHASE21_COMPLETE=NO
