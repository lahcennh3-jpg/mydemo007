# Phase 25 — Continuous Improvement and Maintenance Handoff

Timestamp UTC: 2026-09-26T17:27:43Z

## Flagship state

FLAGSHIP_PRODUCT=Onyx

FLAGSHIP_ENGAGEMENT_STATUS=CLOSED_WITH_LIMITATIONS

PHASE24_PASS_FAMILIES=9

PHASE24_BLOCKED_FAMILIES=5

CARRIED_RESIDUAL_RISKS=12

## Transfer state

SECOND_PRODUCT=OpenHands

OPENHANDS_SOURCE_SHA=47a10808d78561546a02555d0d2c7fa96fa96300

OPENHANDS_TRANSFER_STATE=STATIC_COMPLETE_WITH_LIMITATIONS

OPENHANDS_RUNTIME_ASSESSMENT=NOT_EXECUTED

## Maintenance model

The mandatory roadmap ends at Phase 25.

Future work is continuous maintenance or optional new project rounds rather
than Phase 26.

Recommended review triggers:

- Onyx pinned baseline changes;
- OpenHands pinned baseline changes;
- authentication/session architecture changes;
- authorization/tenant/workspace model changes;
- RAG/retrieval architecture changes;
- agent/tool/MCP capability changes;
- code-execution or sandbox architecture changes;
- outbound-network/proxy behavior changes;
- secret-storage/credential-flow changes;
- material dependency/security advisory;
- new release/deployment architecture;
- incident or disclosure;
- portfolio/publication decision;
- independent-verification availability.

## Unclosed Onyx gates

The twelve Phase 24 residual risks remain owned and deadline-bound.

They must not disappear merely because the mandatory roadmap is complete.

## OpenHands follow-up priorities

If OpenHands becomes a full Deep Project rather than a transfer exercise, the
next engagement should begin with a fresh authorization/scope gate and should
prioritize:

1. agent-server authentication and authorization;
2. direct-host versus Docker sandbox boundary;
3. filesystem/workspace confinement;
4. command/tool confirmation enforcement;
5. remote/cloud backend trust;
6. session API-key storage and propagation;
7. cloud proxy/host override/SSRF behavior;
8. MCP credential lifecycle and server trust;
9. automation/webhook capability security;
10. outbound-network controls;
11. observability/detection;
12. release/rollback and incident response.

## Portfolio truthfulness

PRIVATE_EMPLOYER_REVIEW_READY=YES_WITH_LIMITATIONS

PRIVATE_CLIENT_REVIEW_READY=YES_WITH_LIMITATIONS

PUBLICATION_APPROVED=NO

INDEPENDENT_PROJECT_COMPLETION=NO

ACTION_21.17=BLOCKED_INDEPENDENT

NEXT_SCHEDULED_RISK_REVIEW=2026-10-31

EVENT_DRIVEN_REVIEW=ENABLED

NEXT=CONTINUOUS_QUARTERLY_OR_EVENT_DRIVEN_MAINTENANCE

ACTION_25.22=PASS_CONTINUOUS_IMPROVEMENT_HANDOFF
