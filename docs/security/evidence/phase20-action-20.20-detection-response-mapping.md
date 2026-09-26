# Phase 20 — Detection-to-Response Mapping

All **12** Phase-20 detection conditions have an explicit initial
response and evidence-preservation requirement.

Response design principles:

- preserve evidence before destructive remediation where practical;
- distinguish denial from execution;
- retain actor and tenant context;
- retain resource and policy/control identifiers;
- avoid copying unnecessary secrets or raw sensitive content;
- escalate cross-tenant and sensitive-export signals appropriately;
- fail closed for invalid workload identity where architecture supports it.

This mapping is an engineering response model.

It is not evidence of a production SOC process or response-time SLA.
