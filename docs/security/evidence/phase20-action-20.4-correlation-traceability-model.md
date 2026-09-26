# Phase 20 — Correlation and Traceability Model

A security investigation should be able to correlate, where supported:

user
  -> session
  -> request
  -> authorization decision
  -> conversation/resource
  -> retrieval
  -> model operation
  -> agent
  -> tool/MCP call
  -> external-side-effect boundary
  -> response/result

Required correlation properties:

1. stable request/correlation identifier;
2. actor identity;
3. tenant/workspace identity;
4. target resource identity;
5. security decision/outcome;
6. component boundary;
7. timestamp;
8. error/failure class.

Security events must not rely on raw prompt or document contents as the
only means of correlation.

Missing correlation is treated as an observability gap, not silently
interpreted as proof that no security event occurred.

Production distributed-tracing completeness is not claimed.
