# Phase 0 — Scope and Rules of Engagement

## Engagement Status

Status: APPROVED — AUTHORIZED FOR BOUNDED LOCAL SECURITY TESTING

## Verified Repository Baseline

Repository: https://github.com/amaw535353-ai/mydemo007.git
Local path: /home/ahmed/projects/mydemo007
Baseline branch: main
Security working branch: security/phase-0-scope
Baseline commit: 10835c149c730c4de4dbf379483bc00ec3ff914a
Initial working-tree state: clean

## Authorization

Authorization owner: amaw535353-ai — owner of the GitHub repository
Authorized tester: Ahmed — local lab operator
Authorized purpose: Security-learning, reverse-engineering, defensive testing, remediation, and evidence creation on the authorized local copy of mydemo007
Authorization period: Valid for this local training engagement until explicitly revoked.

## In-Scope Assets

Repositories: Local clone /home/ahmed/projects/mydemo007 from https://github.com/amaw535353-ai/mydemo007.git, baseline main at commit 10835c149c730c4de4dbf379483bc00ec3ff914a; security work performed on security/phase-0-scope
Services and endpoints: Local Docker Compose services in scope: api_server, background, web_server, inference_model_server, indexing_model_server, relational_db, opensearch, nginx, cache, minio, code-interpreter. Container-internal service-to-service traffic is in scope. Any host-published endpoint must remain bound to the approved local loopback boundary.
Networks: Local machine only. Host-published test services must bind to 127.0.0.1. LAN hosts, public IPs, Internet targets, and external services are outside the active-testing boundary.
Users and roles: Synthetic lab accounts only. Repository evidence shows permission-based authorization with scoped permissions for agents, connectors, LLMs, actions, user groups, and related resources. Exact runtime account-type mapping will be verified during the local baseline before authorization testing.
Data and datasets: Synthetic test data only. Real customer data, production database copies, personal documents, real logs containing personal data, and other production datasets are prohibited.
Models and providers: Repository supports configurable LLM and model providers including OpenAI, Azure, Anthropic, Google or Vertex, Bedrock, Ollama or local servers, and other provider abstractions. Active security testing is restricted to local or mock model endpoints; real external provider calls and credentials remain out of scope.
Agents: Onyx agent and persona functionality and its authorization boundaries are in scope for local synthetic testing. Only agents operating inside the approved local lab are in scope.
Tools and actions: Onyx custom tools and actions, including OpenAPI and MCP-associated actions, are in scope only when configured against approved local synthetic services. External actions and real third-party side effects are prohibited.
MCP clients and servers: Onyx MCP client and server code and locally controlled loopback or mock MCP services are in scope. Repository-configured remote MCP endpoints and package retrieval requiring Internet access are excluded from active testing.
Connectors: Onyx connector framework, mock connector, and federated-connector code are in scope for source review. Active connector testing is limited to local mock or synthetic connectors; real third-party connectors and accounts remain out of scope.

## Explicit Exclusions

Public deployments; LAN systems; public IPs; Internet targets; external APIs and services; real third-party accounts or connectors; real customer or production data; production database backups; real production credentials; billable cloud resources or paid SaaS; and any system, tenant, account, repository, service, model, agent, tool, MCP server, or connector not explicitly included in this local authorized lab scope.

## Permitted Techniques

Permitted techniques include read-only source-code and configuration review; architecture and data-flow analysis; threat modeling; local static analysis; dependency, SBOM, and secret-pattern scanning; and creation of defensive patches, tests, and documentation. After the Approval Gate is satisfied, bounded dynamic security testing is permitted only against approved local loopback services using synthetic identities, synthetic data, and fake or locally generated credentials.

## Prohibited Techniques

Prohibited techniques include testing public, LAN, production, third-party, or otherwise out-of-scope systems; use of real customer data or production credentials; intentional denial-of-service or unbounded resource exhaustion; destructive modification or deletion of non-synthetic data; persistence, malware deployment, or lateral movement outside the approved local lab; social engineering of real people; attempts to access real third-party accounts; uncontrolled credential attacks; bypassing the approved loopback network boundary; and any technique whose scope, impact, cost, or authorization is uncertain.

## Test Data and Identity Rules

Synthetic-data requirements: All test documents, prompts, records, conversations, files, and datasets must be synthetic.
Synthetic-identity requirements: All test users, tenants, organizations, email addresses, and identities must be synthetic lab identities.
Synthetic-credential requirements: Only fake or locally generated test passwords, tokens, API keys, secrets, and certificates may be used. Real production credentials are prohibited.

## Resource and Cost Limits

Test windows: Active security testing is permitted only during attended local-lab sessions under the authorized tester's supervision. Unattended or overnight active testing is prohibited unless separately reviewed and approved. Each individual active test remains subject to the documented 60-second maximum.

Rate limits: Maximum 100 requests per individual active security test unless a lower test-specific ceiling is defined.
Concurrency limits: Maximum 10 simultaneous requests during active security testing.
Token limits: No unbounded token-generation or agent loops. Test-specific token ceilings must be defined before model or agent stress testing.
Time limits: Maximum 60 seconds per individual active security test unless stopped earlier.
Memory limits: Intentional memory-exhaustion testing is prohibited. Stop immediately if testing creates host instability or abnormal memory pressure.
Storage limits: Maximum 1 MB per individual test file unless a smaller test-specific limit is defined. Unbounded disk writes are prohibited.
External-network restrictions: Active security testing is restricted to the local loopback lab. No active testing against LAN systems, public Internet targets, or external services.
Cost restrictions: No paid APIs, billable cloud resources, paid SaaS, metered external services, or other activity that can create an unapproved charge. Stop immediately if a test may create a charge.

## Stop Conditions

Stop immediately if a test reaches an external or out-of-scope service; encounters real customer data or a real production credential; exceeds approved request, concurrency, time, token, memory, storage, or network limits; may create an unapproved charge; causes unexpected instability; or if authorization or scope becomes uncertain.

Escalation contacts: Primary local escalation contact is Ahmed — repository owner and local lab operator. Testing must stop and be escalated to the authorization owner if scope, authorization, safety, data classification, network exposure, cost, or system stability becomes uncertain. Upstream or third-party security issues must be escalated through the project's verified official private security-reporting channel.

## Evidence Handling

Preserve reproducible commands, timestamps, relevant logs, synthetic identifiers, diffs, test outputs, and screenshots with sufficient context. Evidence must not contain real credentials, production secrets, real customer data, or unnecessary personal data. Sanitize sensitive values before sharing or publishing.

## Rollback and Teardown

Rollback procedure: Restore changed tracked files from Git or revert the security change commit; stop affected local services; remove temporary synthetic test artifacts only after required evidence is preserved; and verify the repository and lab return to the approved baseline.
Teardown procedure: Stop local test services and containers; remove temporary synthetic credentials and test data when no longer needed; verify no unintended listeners or external connections remain; preserve sanitized evidence and reports; and confirm the Git working state.

## Responsible Disclosure

Security findings that affect an upstream or third-party project must be reported privately through its official security or vulnerability-reporting channel after checking the applicable disclosure policy. Preserve a synthetic reproduction and evidence, avoid public exploit details during the private investigation window, coordinate remediation and retesting, and document residual risk. Findings confined to this authorized local learning copy may remain private portfolio evidence after sanitization.

Communication rules: Security findings and evidence are private by default. Share only the minimum necessary sanitized evidence with authorized recipients. Do not publish credentials, personal data, exploit details, or unresolved third-party vulnerabilities. Public portfolio material must be sanitized and must not violate an active disclosure investigation, embargo, or confidentiality requirement.

## Approval Gate

Security testing must not begin until this document has been reviewed and the required scope and authorization fields have been approved.

## Pre-Deployment Exposure Observation

The repository was inspected before launching any containers.

Default Docker Compose publishes:
- nginx: host 80 -> container 80
- nginx: host 3000 -> container 80

The development override additionally publishes:
- api_server: host 8080 -> container 8080
- relational_db: host 5432 -> container 5432
- opensearch: host 9200 -> container 9200
- inference_model_server: host 9000 -> container 9000
- cache: host 6379 -> container 6379
- minio API: host 9004 -> container 9000
- minio console: host 9005 -> container 9001
- code-interpreter: host 8000 -> container 8000

The development configuration contains an explicit security TODO noting that MinIO should be prefixed with 127.0.0.1 to avoid LAN exposure.

Security decision status: APPROVED — Option A, local-machine-only testing boundary
No deployment has been launched.

## Approval Record

Approval status: APPROVED
Approval date: 2026-09-13
Authorization owner approval: amaw535353-ai — repository owner
Authorized tester acknowledgement: Ahmed — local lab operator
Approved purpose: Security learning, reverse engineering, defensive testing, remediation, and evidence creation.
Approved baseline commit: 10835c149c730c4de4dbf379483bc00ec3ff914a
Approved working branch: security/phase-0-scope
Approval boundary: Local loopback lab only; synthetic identities, data, and credentials only; no real external providers, third-party accounts, public targets, paid services, or unapproved costs.
Approval limits: Maximum 100 requests per individual active test, maximum 10 concurrent requests, maximum 60 seconds per individual active test, maximum 1 MB individual test file, and no unbounded resource or agent loops.
Reapproval requirement: Any material change to scope, network boundary, targets, data classification, external integrations, cost exposure, or testing limits requires review before testing continues.

## Approval Amendment — Phase 0 Closure

Amendment status: APPROVED
Amendment date: 2026-09-13
Change: Added explicit test-window, escalation-contact, and communication-rule requirements required for Phase 0 closure.
Scope effect: No expansion of authorized targets, networks, data, identities, credentials, external integrations, cost exposure, or testing techniques.
Authorization owner approval: amaw535353-ai — repository owner
Authorized tester acknowledgement: Ahmed — local lab operator
Previous approved Phase 0 commit: 5c95ca3180ebb00ff760ecd3657ce39a75854e15

## Approval Amendment — Phase 25 offline image preparation

Approval status: APPROVED FOR IMAGE-ONLY PREPARATION.

Approval evidence: The user replied, "Approve the offline image-only
amendment," in the current conversation on 2026-09-26 at 19:18:43 UTC.
The conversation is the approval source. This document is a committed
record of that instruction, not a signed copy of the conversation.

This amendment applies only to the owned fork
`https://github.com/lahcennh3-jpg/mydemo007.git` in the attended Codespace
at `/workspaces/mydemo007`. The selected source commit is
`193c7c4b652fc3ae76256718f53d0a956e996b7f`.
The cached base image ID is
`sha256:fa570e141e39af5e1e48767fe14cbe227abe9a5ec0e3d08b9580c8bf60b35543`.

The authorized action is a local, six-file code-overlay image build.
Use only tracked files from the selected source commit.
Use the cached base image and the local Docker builder.
Run the build without network access or image pulls.
Stop the build after 60 seconds.
Keep each selected file at or below 1 MB.
Stop if available memory is below 1.5 GiB or disk is below 8 GiB.
Record the new image ID, Dockerfile hash, and six file hashes.

Do not restart the API, run migrations, connect to the database,
start a model, call an external service, or download packages.
Do not change the running Phase 24 baseline.
Stop if a guard fails or the build attempts external access.

The prepared image replaces six Python files in an older base image.
It is not a complete build from the current dependency locks.
It is not approved for API deployment or active security testing.
The source-to-runtime risk remains open.

Rollback: retain the evidence, then remove only the new local overlay
image tag and local base alias. Check that the original API image ID
and container ID remain unchanged.

This narrow approval does not retroactively update earlier Phase 0
repository and WSL identifiers. Reconcile those historical records
separately before any new runtime assessment.
