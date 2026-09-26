# Phase 20 Security Event Schema

Every security-relevant event should support, where applicable:

- event timestamp;
- event type;
- event outcome;
- severity;
- actor/user identifier;
- tenant/workspace identifier;
- session/request identifier;
- correlation/trace identifier;
- resource identifier;
- action;
- authorization decision;
- policy/control identifier;
- source component;
- destination component;
- tool/agent identity;
- data classification;
- error/failure class;
- sanitized security context.

## Security properties

Events must:

1. distinguish authentication from authorization;
2. preserve tenant context;
3. preserve request/correlation context;
4. distinguish attempted from successful actions;
5. distinguish policy denial from system failure;
6. avoid raw secrets;
7. avoid unnecessary sensitive content;
8. support investigation without requiring production payload capture.

## Boundary

This is a security telemetry contract.

It is not evidence that every Onyx component currently emits every field.
