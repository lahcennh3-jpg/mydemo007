# Phase 21 — Assisted Independent-Style Rehearsal

Recorded: 2026-09-26T12:34:54Z

Source commit:

`4508214fa8a3f703ec63181cc02650028b641bbb`

## Classification

This rehearsal followed the independent-round objectives, but the commands,
analysis structure, and findings were supplied by the assistant.

Therefore:

ASSISTED_REHEARSAL=YES
INDEPENDENT_ASSESSMENT=NOT_CLAIMED
ACTION_21.17=BLOCKED_INDEPENDENT

## Clean rebuild

CLEAN_WORKTREE=PASS
FRESH_RUNTIME_NAMESPACE=PASS
LITE_TOPOLOGY=5_SERVICES
NETWORK_INTERNAL=true
HOST_PORT_EXPOSURE=NONE

```text
SERVICE=relational_db RUNNING=true HEALTH=healthy IMAGE=sha256:d9c304353c031b21e9a7e33dc4781e272a9fa802a2ab9703fe4199d72ba1422c
SERVICE=api_server RUNNING=true HEALTH=healthy IMAGE=sha256:fa570e141e39af5e1e48767fe14cbe227abe9a5ec0e3d08b9580c8bf60b35543
SERVICE=web_server RUNNING=true HEALTH=healthy IMAGE=sha256:c967449a9e099fbc67d8f26f94c6b57d9a558bafdc7467a49708847d09f6deea
SERVICE=code-interpreter RUNNING=true HEALTH=healthy IMAGE=sha256:e4d3e4d875309b90aaad810373dd8ea368e6692ffec6ac36b9eb2ea7f77f97f6
SERVICE=nginx RUNNING=true HEALTH=healthy IMAGE=sha256:516475cc129da42866742567714ddc681e5eed7b9ee0b9e9c015e464b4221a00

```

ALL_FIVE_SERVICES_HEALTHY=PASS

## Runtime verification

Database:

```text
/var/run/postgresql:5432 - accepting connections
```

DATABASE_READY=PASS

API:

```text
status_code=200
{"success":true,"message":"ok","data":null}
```

API_HEALTH=PASS

Code interpreter:

```text
{"message": null, "status": "ok", "version": "0.4.7"}
```

CODE_INTERPRETER_HEALTH=PASS

## Host exposure

```text
SERVICE=relational_db HOST_PORTS=NONE
SERVICE=api_server HOST_PORTS=NONE
SERVICE=web_server HOST_PORTS=NONE
SERVICE=code-interpreter HOST_PORTS=NONE
SERVICE=nginx HOST_PORTS=NONE

```

HOST_PORT_EXPOSURE=NONE

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

SECURITY_REPRODUCTION=PASS

## Source-review identities

matching SHA-256:

`643f1fe4d19668ef737041f6f7f713b77b0eea02ba01b8d8d11dca5c1e437fa9`

request evaluator SHA-256:

`87e923898ff2c76eca93fe6781b161d39314a9f13a7c264e14edcb07a834eab0`

gate SHA-256:

`d666ce28e46165c1d265f1ba563934308f34897aa2db275edf8fcbac1781b1ba`

## Findings

### Finding 1 — Restrictive policy precedence

The action-matching model sorts matched actions using policy severity and uses
the governing action as the decision-driving action.

Security implication:

mixed-action requests are designed to inherit the stricter applicable policy
rather than the least restrictive policy.

Classification:

positive security-control observation.

### Finding 2 — Tenant/user scoped MCP attribution

The MCP request evaluator obtains target candidates using tenant-scoped
database state and user-accessible MCP servers.

Unclassifiable attributed MCP requests are converted into explicit DENY
actions.

Security implication:

classification errors on an attributed MCP request are intended to fail
closed instead of silently becoming an authorized tool invocation.

Classification:

positive security-control observation.

### Finding 3 — In-band authority headers are stripped

The proxy gate removes Proxy-Authorization and the MCP session-tag header
before an outbound request reaches the origin.

Security implication:

internal authority metadata is not intentionally forwarded as ordinary
application request data.

Classification:

positive trust-boundary observation.

### Finding 4 — Internal destinations have multiple checks

The gate checks destination restrictions during request handling and again
near upstream connection establishment.

Security implication:

the later check reduces the time between destination validation and actual
connection.

Residual limitation:

source comments explicitly describe a remaining DNS re-resolution/rebinding
window. This rehearsal did not demonstrate exploitability.

Classification:

documented residual design risk, not a confirmed vulnerability.

### Finding 5 — Missing session fails closed for ASK actions

The ASK path attempts to resolve the originating session. Lookup errors or
absence of an active session produce a 403 path rather than proceeding with
the action.

Classification:

positive authorization-control observation.

### Finding 6 — Synthetic approval artifact mutation is rejected

The Phase 17 regression passes the known-good baseline and rejects the copied
policy when the production-approval state is deliberately changed.

Classification:

verified local synthetic regression behavior.

Scope:

This does not establish production Onyx security effectiveness.

## Safety

REAL_CUSTOMER_DATA_USED=NO
REAL_CREDENTIALS_USED=NO
REAL_EXTERNAL_AI_API_USED=NO
PUBLIC_TARGET_TESTING=NO

ROLLBACK=PASS

## Result

ASSISTED_REHEARSAL_RESULT=PASS
INDEPENDENT_ASSESSMENT=NOT_CLAIMED
ACTION_21.17=BLOCKED_INDEPENDENT
PHASE21_COMPLETE=NO
