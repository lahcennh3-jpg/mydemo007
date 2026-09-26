# Phase 20 — Synthetic Incident Correlation Exercise

## Scenario

A synthetic actor generates a sequence of authentication, authorization,
retrieval, tool, MCP, and sensitive-data policy signals.

## Correlation chain

1. repeated authentication failures;
2. cross-user access attempt;
3. unauthorized RAG retrieval;
4. unauthorized privileged-tool invocation;
5. unauthorized MCP invocation;
6. sensitive export attempt.

The fixture contains **8** ordered synthetic events.

## Investigation requirement

An investigator should be able to reconstruct:

actor → tenant → request/resource → authorization/policy decision → AI/action
boundary → outcome.

## Finding

Individual alerts are less useful when actor, tenant, resource and request
context cannot be correlated.

Missing correlation must therefore be recorded as an observability weakness,
not interpreted as absence of malicious or suspicious behavior.

## Boundary

This is a deterministic synthetic incident reconstruction.

No production incident is claimed.
