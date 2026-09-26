# Onyx AI Application & Product Security Assessment

## Portfolio classification

PRIVATE_TECHNICAL_REVIEW_READY=YES_WITH_LIMITATIONS

PUBLICATION_APPROVED=NO

INDEPENDENT_PROJECT_COMPLETION=NO

ACTION_21.17=BLOCKED_INDEPENDENT

## 1. Engagement objective

The project applied an evidence-driven security-engineering workflow to an
authorized local Onyx environment.

The work covered application/API security, identity and authorization,
retrieval and RAG boundaries, agents/tools/MCP, privacy, abuse resistance,
software and AI supply chain, runtime security, detection, incident response,
release assurance and residual-risk management.

It used synthetic data and bounded local test conditions.

No public Onyx deployment or customer system was actively tested.

## 2. Engineering workflow

The engagement used the following lifecycle:

authorization and scope

→ architecture and reverse engineering

→ threat modeling

→ security requirements

→ bounded security testing

→ control implementation/review

→ regression/evaluation

→ findings and root-cause analysis

→ remediation or explicit residual-risk disposition

→ release assurance

→ incident-response/tabletop exercise

→ portfolio and transfer preparation.

## 3. Phase 24 runtime baseline

The final current-cycle runtime was reconstructed as an offline,
control-plane-focused environment.

Key boundary properties included:

- synthetic data and identities;
- internal-only API networking;
- no intentional external model-provider calls;
- PostgreSQL file-store mode for the control-plane baseline;
- model server disabled for that baseline;
- synthetic local tokenizer cache;
- bounded requests and resource use;
- stop-on-unexpected-outbound behavior.

This baseline was intentionally insufficient for model-dependent or genuine
cross-tenant claims.

## 4. Security evaluation cycle

Fourteen security-evaluation families were dispositioned.

Nine received PASS dispositions:

- authentication negative-path regression;
- cross-user object ownership / BOLA;
- agent/tool authority;
- MCP identity/authorization boundary controls;
- sensitive-data exposure controls;
- bounded abuse/availability controls;
- current runtime deployment integrity;
- synthetic detection/audit control regression;
- synthetic incident-response tabletop.

Five remained BLOCKED:

- cross-tenant isolation;
- RAG authorization/revocation;
- retrieval poisoning;
- prompt injection;
- model/provider behavior.

Blocked work was not relabeled as PASS.

## 5. Authentication and object-ownership evidence

Current-runtime tests exercised unauthenticated and invalid-session behavior.

A two-user synthetic object-ownership test exercised owner and non-owner
access to chat-session resources.

An ambiguous HTTP 400 result from one delete path was not treated as security
PASS or security FAIL.

A separate documented write-side ownership path was then retested with
positive and negative controls.

That retest passed all six cases.

This supports a cross-user ownership-control claim.

It does not establish cross-tenant isolation.

## 6. Agent, tool and MCP controls

Current-source security regressions exercised:

- rejection of unavailable/invented tool execution;
- tool execution limits;
- MCP header allowlisting;
- managed credential precedence;
- authentication-performer boundaries;
- MCP security-boundary logic.

These results support control-level evidence.

They do not constitute validation of every live external MCP integration.

## 7. Sensitive-data controls

The current cycle revalidated:

- redaction of synthetic sensitive values;
- avoidance of raw tool-argument tracing;
- avoidance of raw tool-output tracing;
- absence of the local synthetic authentication secret from selected API
  responses;
- absence of that synthetic secret from captured API logs.

No production secret-exposure claim is made.

## 8. Abuse and availability controls

Bounded tests exercised controls including:

- finite queue/resource limits;
- duplicate-work prevention;
- bounded lock/task timing;
- bounded concurrency;
- backpressure behavior.

This is evidence of security-control behavior in the controlled lab.

It is not production-scale resilience evidence.

## 9. Deployment and supply-chain assurance

The current runtime was checked against the frozen Phase 24 baseline for:

- API image identity;
- database migration revision;
- container health;
- internal-only network scope;
- ignored local secret configuration.

Automatic application upgrade was not used.

Full current-upstream equivalence was not established.

## 10. Detection and incident response

The project re-executed synthetic detection-control fixtures with expected
positive and benign-noise behavior.

A five-scenario synthetic incident-response tabletop covered:

- cross-tenant retrieval;
- indirect prompt/tool abuse;
- MCP/credential exposure;
- dependency/runtime drift;
- model/provider behavioral regression.

This validates a synthetic engineering process.

It does not validate production SOC effectiveness or production response
times.

## 11. Findings and remediation state

No confirmed security failure was produced by the Phase 24 evaluation
families that were executable.

Therefore no fabricated remediation PR was created.

A BOLA HTTP-response-code inconsistency remained a non-security observation.

Unavailable security-validation domains were converted into owned residual
risks and claim restrictions.

## 12. Release decision

The Phase 24 security decision was:

CONDITIONAL_GO_FOR_LOCAL_CONTROL_PLANE_SCOPE

This decision is limited to the validated local control-plane evidence.

It is not a production release approval.

## 13. Residual risk

Twelve residual risks remained open at Phase 24 closure.

Important remaining gates include:

- second synthetic tenant fixture;
- controlled RAG runtime;
- retrieval-poisoning runtime;
- controlled model-generation runtime;
- controlled provider/model runtime;
- stronger immutable source-to-runtime provenance;
- S3/MinIO path validation;
- production operational evidence;
- current-upstream comparison;
- portfolio publication approval;
- independent project reproduction;
- Phase 21 Action 21.17 independent gate.

## 14. What this project demonstrates

The evidence supports experience practicing:

- AI application security architecture;
- threat modeling;
- API and ownership testing;
- security-control regression engineering;
- agent/tool/MCP security reasoning;
- data-redaction controls;
- abuse/resource controls;
- runtime isolation;
- supply-chain/provenance thinking;
- security detection engineering;
- incident-response exercises;
- release assurance;
- evidence and residual-risk management.

## 15. What this project does not claim

The project does not claim:

- testing unauthorized production systems;
- discovering exploitable vulnerabilities in public Onyx deployments;
- production operational effectiveness;
- complete cross-tenant runtime validation;
- complete RAG security validation;
- complete prompt-injection validation in the final Phase 24 runtime;
- complete model/provider validation;
- unrestricted portfolio publication approval;
- independent complete-project reproduction.

## 16. Review state

EMPLOYER_CLIENT_PRIVATE_REVIEW=READY_WITH_LIMITATIONS

PUBLIC_PORTFOLIO_PUBLICATION=NOT_APPROVED

INDEPENDENT_REPRODUCTION=NOT_COMPLETE

PHASE25_FINAL_ONYX_CASE_STUDY=COMPLETE_WITH_LIMITATIONS
