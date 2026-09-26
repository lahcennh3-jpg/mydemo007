# Phase 23 — 2026 Q3 Maintenance Incident-Response Tabletop

Timestamp UTC:

`2026-09-26T13:48:40Z`

## Exercise boundary

This is a synthetic tabletop exercise.

TABLETOP_TYPE=SYNTHETIC

REAL_PRODUCTION_INCIDENT=NO

PRODUCTION_DETECTION_VALIDATED=NO

PRODUCTION_CONTAINMENT_VALIDATED=NO

## Purpose

Exercise the maintenance process against representative AI-application
security incidents without claiming real production operational evidence.

## Scenario 1 — Cross-tenant retrieval

Synthetic event:

A Tenant Alpha user appears to receive a retrieved document associated with
Tenant Beta.

Required response:

1. preserve request/retrieval evidence;
2. identify subject, tenant and object identifiers;
3. stop affected retrieval path if necessary;
4. determine whether authorization was enforced before retrieval;
5. determine scope;
6. identify affected data;
7. remediate authorization failure;
8. execute cross-tenant regression;
9. update threat model;
10. document residual risk.

Decision:

`TABLETOP_RESPONSE_DEFINED`

## Scenario 2 — Indirect prompt injection to tool execution

Synthetic event:

A retrieved document contains instructions attempting to cause an agent to
invoke a privileged tool.

Required response:

1. preserve retrieved content and tool-selection evidence;
2. identify the instruction trust boundary;
3. determine whether tool authorization was independently enforced;
4. inspect approval requirements;
5. prevent unauthorized execution;
6. test equivalent malicious inputs;
7. update prompt/agent/tool controls;
8. update evaluation cases.

Decision:

`TABLETOP_RESPONSE_DEFINED`

## Scenario 3 — MCP/OAuth credential propagation

Synthetic event:

An MCP integration appears to reuse or expose a token outside the intended
authorization boundary.

Required response:

1. preserve token-flow metadata without committing secrets;
2. revoke synthetic/affected credentials where appropriate;
3. identify credential owner and intended audience;
4. inspect OAuth lifecycle;
5. inspect MCP server identity;
6. inspect least privilege;
7. execute negative authorization tests;
8. update threat and control mappings.

Decision:

`TABLETOP_RESPONSE_DEFINED`

## Scenario 4 — Supply-chain change

Synthetic event:

A security-relevant dependency or container artifact changes unexpectedly.

Required response:

1. preserve artifact provenance;
2. identify old/new version or digest;
3. identify build origin;
4. review advisories;
5. validate integrity;
6. assess affected services;
7. decide containment/rollback;
8. execute selected regression tests;
9. update supply-chain evidence.

Decision:

`TABLETOP_RESPONSE_DEFINED`

## Scenario 5 — Model/provider behavioral change

Synthetic event:

A model/provider update changes behavior relevant to prompt injection,
structured output or tool selection.

Required response:

1. preserve exact model/provider/version identity;
2. freeze comparison inputs;
3. rerun relevant security evaluations;
4. compare expected versus actual behavior;
5. identify affected controls;
6. update residual risk;
7. roll back or compensate when necessary.

Decision:

`TABLETOP_RESPONSE_DEFINED`

## Tabletop completion criteria

- five scenario families reviewed;
- evidence preservation addressed;
- containment addressed;
- remediation addressed;
- regression addressed;
- threat-model update addressed;
- residual-risk decision addressed.

TABLETOP_SCENARIOS=5

TABLETOP_SIMULATION_COMPLETE=YES

TABLETOP_RESULT=PASS_FOR_PROCESS_EXERCISE

PRODUCTION_OPERATIONAL_EFFECTIVENESS_CLAIM=NO

## Result

ACTION_23.18=PASS_SYNTHETIC_INCIDENT_TABLETOP
