# Phase 21 Batch A — Assisted Assessment

Baseline: `d7c999d353f087c58e52dc75c4787e812e730281`.
Evidence: the recorded Phase 21 session, its post-session record, and its SHA-256 file.

The assistant supplied the execution commands. These results do not prove
independent command selection or independent professional judgment.

## 21.1 — BLOCKED

The clean source checkout and SHA were verified. Docker ran one cached Python
image. The merged Lite Compose configuration listed five services, but their
application and database images were not cached. The deployment `.env` was
absent. No Onyx service or application health check ran. The Python image
smoke check does not count as a complete Onyx lab rebuild.

## 21.2 — ASSISTED REPRODUCTION

- RAG provenance: four offline `unittest` tests passed.
- Action approval: five offline `unittest` tests passed. The first attempt
  produced three file-path errors. Changing the working directory to
  `/src/backend` resolved them.
- Detection: the original 20-event synthetic corpus produced 12 expected
  detections and passed its gate. The 24-event corpus produced the same
  12 detections but failed the gate's exact 20-event count condition.
- Field quality: a separate temporary validator accepted both intact corpora.
  It rejected missing actor at EV005, resource at EV007, and tenant at EV006.

The checked-in detector accepts those three malformed rows when run alone.
The separate validator is a fixture test. No live telemetry or production
detection effectiveness was measured.

## 21.3 — ASSISTED COMMAND EXPLANATIONS

| Command | Purpose and target | Evidence | Failure signal | Rollback |
| --- | --- | --- | --- | --- |
| `git rev-parse` and `git status` | Verify clean source identity | Pinned SHA; clean checkout | Wrong SHA or changed files | Discard isolated clone |
| `docker compose config` | Inspect merged deployment | Five services and image names | Invalid configuration | None; read-only |
| Offline `docker run` | Run bounded source tests | Four RAG and five approval passes | Error, zero tests, or timeout | Remove named test container |
| `awk -f` | Replay synthetic detector events | Base passes; 24-event count gate fails | Unexpected output or exit | None; read-only |
| Temporary AWK validator | Test required fixture fields | Three missing fields rejected | Mutation accepted | Delete temporary validator |
| `sha256sum` and `cmp` | Compare artifact copies | Modified digest differs | Identical digest after change | Delete temporary copies |

The engineer has not independently explained these commands for assessment.

## 21.4 — ASSISTED VERIFIER TRANSFER

The Phase 17 pipeline verifier passed on an isolated export of
the committed synthetic lab. Changing `production_approved` to
`true` in a copy of `policy-config-v1.json` caused the verifier
to exit 1 with `VERIFY_FAIL: policy approval`.

Evidence: `docs/security/evidence/phase21-action-21.4-verifier-transfer.txt`.
The assistant supplied the commands. This checks one approval
rejection path; it does not establish independent assessment,
production approval, or live Onyx behavior.

## 21.5 — PARTIAL CODE REVIEW

Scope: MCP classification, approval policy, proxy gate, and fixture detector.

- `matching/engine.py:74-90` sorts actions by policy severity.
- `request_evaluator.py:170-194` obtains user-scoped MCP targets through a
  tenant-scoped database session.
- `request_evaluator.py:199-227,237-264` denies unclassifiable attributed
  MCP requests and applies per-tool policy.
- `sandbox_proxy/addons/gate.py:382-385` removes session authority headers.
- `gate.py:393-435,629-695` contains approval, DENY, and session-failure paths.

Finding, high confidence for the **lab detector**: its final condition fixes
the event count at 20, and it does not validate missing actor, tenant, or
resource fields. Direct synthetic replay demonstrated both properties.
This is not a confirmed Onyx application vulnerability.

Limit: three approval tests inspect source text. The complete live proxy,
credential resolver, tenant boundary, and MCP request path were not run.

## 21.6 — PARTIAL ARCHITECTURE REVIEW

Relevant path: sandbox request → proxy gate → MCP evaluator → tenant-scoped
database lookup → action policy and approval → credential resolution →
external destination. Trust decisions include target attribution, policy
precedence, originating session, destination checks, and credential injection.
Approval records and grants hold decision state. The inspected gate logs
allow and block paths. No complete runtime or recovery path was verified.

## 21.7 — PARTIAL DESIGN REVIEW

Workflow: a sandbox requests an MCP tool action. The objective is to prevent
unapproved egress. Misuse cases include malformed JSON-RPC, ambiguous targets,
mixed-policy batches, forged session tags, internal destinations, and errors
after approval. Source shows strictest-policy selection, DENY handling,
session checks for ASK, header removal, and explicit error responses.

A possible alternative is to deny every off-catalog request; its effect on
functionality was not evaluated. The source notes a residual DNS rebinding
window near upstream connection setup (`gate.py:314-332`). Exploitability was
not tested. A future change should retain the original version and regression
evidence so it can be rolled back.

## Decision

The full rebuild, actual Phase 17 verifier transfer, and independent
assessment remain open. No production or live Onyx security claim is made.

BATCH_A_RESULT=BLOCKED_ASSISTED_SCOPE
