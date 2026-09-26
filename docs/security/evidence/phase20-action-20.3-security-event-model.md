# Phase 20 — Security Event Model

## Required event families

### Identity

- authentication success/failure;
- session creation/termination;
- privilege or role changes;
- service/workload identity events.

### Authorization

- authorization allow;
- authorization deny;
- ownership violation attempt;
- cross-user access attempt;
- cross-tenant access attempt.

### AI application

- prompt-processing security event;
- retrieval authorization decision;
- document/resource access decision;
- memory access;
- agent invocation;
- tool invocation;
- MCP invocation;
- code/execution boundary event.

### Data security

- sensitive-data policy decision;
- redaction decision;
- export/download;
- destructive data action;
- unusual bulk access.

### Abuse and availability

- rate-limit event;
- resource-limit event;
- repeated failure;
- abnormal request volume;
- expensive-operation signal.

### Infrastructure

- privileged workload attempt;
- unexpected network path;
- identity failure;
- policy failure;
- integrity/provenance failure.

## Required distinction

The telemetry model must distinguish:

ATTEMPTED -> ALLOWED -> EXECUTED -> FAILED -> DENIED

where the application architecture makes those states observable.

## Evidence boundary

This action defines the required detection/event model.

It does not claim production telemetry completeness.
