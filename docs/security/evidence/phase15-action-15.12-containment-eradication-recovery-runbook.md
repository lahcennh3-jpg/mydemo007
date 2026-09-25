# Phase 15 — Containment, Eradication, and Recovery Runbook

## Purpose

Response procedure for the synthetic Phase 15 AI application security incident.

No commands in this runbook are authorized against production systems as part
of this exercise.

## Incident

`INC-P15-001`

## Immediate containment

1. Preserve relevant event and alert evidence.
2. Preserve hashes before modifying affected components.
3. Stop the affected synthetic agent execution.
4. Block the modeled unapproved tool call.
5. Maintain denial of the cross-tenant request.
6. Maintain denial of the unapproved runtime destination.
7. Disable or roll back the modeled unapproved prompt-policy revision.
8. Apply resource cancellation / quota controls to the modeled runaway request.
9. Do not delete forensic evidence during containment.

## Identity and authorization containment

Review:

- actor identity;
- tenant identity;
- role;
- service identity;
- approval state;
- authorization decision;
- associated trace identifiers.

For a real incident, credential revocation requires authorization and confirmed
scope. No real credentials exist in this exercise.

## Agent / tool / MCP containment

For a real incident:

- stop affected agent execution;
- disable the affected action or tool;
- revoke untrusted MCP connectivity;
- require explicit approval for sensitive tools;
- preserve tool-call identifiers and approval evidence.

This synthetic exercise performs no real MCP or remote tool action.

## Retrieval containment

For a real incident:

- deny cross-tenant retrieval;
- quarantine suspect source mappings;
- invalidate affected indexes or caches only when authorized;
- preserve source identifiers, hashes and provenance evidence.

## Configuration containment

For a real incident:

- compare approved and observed configuration hashes;
- restore the last approved configuration;
- invalidate unapproved deployment state;
- document owner and approval chain.

## Eradication

Eradication criteria:

- unauthorized configuration removed;
- prohibited destination unavailable;
- tenant authorization boundary restored;
- unsafe tool path disabled or approval-gated;
- poisoned or invalid retrieval source removed from trusted scope;
- resource controls active.

## Recovery

Recovery requires:

1. approved configuration restored;
2. authorization regression passing;
3. retrieval isolation regression passing;
4. agent/tool security regression passing;
5. resource-limit regression passing;
6. detection regression passing;
7. evidence preserved;
8. incident owner approval.

## Rollback trigger

Rollback is required if any security regression fails during recovery.

## Exercise result

`SYNTHETIC_RESPONSE_RUNBOOK_PREPARED`
