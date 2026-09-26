# Phase 25 — OpenHands Static Security Transfer Assessment

Timestamp UTC: 2026-09-26T17:27:43Z

## Provenance

OPENHANDS_REPOSITORY=https://github.com/OpenHands/OpenHands.git

OPENHANDS_SOURCE_SHA=47a10808d78561546a02555d0d2c7fa96fa96300

OPENHANDS_PACKAGE_VERSION=1.24.0

OPENHANDS_SOURCE_PINNED=YES

## Scope

ASSESSMENT_TYPE=STATIC_SOURCE_TRANSFER

OPENHANDS_RUNTIME_BASELINE_ESTABLISHED=NO

OPENHANDS_ACTIVE_SECURITY_TESTING_EXECUTED=NO

OPENHANDS_TEST_SUITE_EXECUTED=NO

OPENHANDS_MODEL_PROVIDER_USED=NO

PUBLIC_TARGET_ACTIVE_TESTING=NO

REAL_CREDENTIALS_USED=NO

## Architectural transfer

The Onyx security method transfers, but the product architecture changes the
highest-priority trust boundaries.

Onyx centered strongly on:

- application/API authorization;
- conversation/object ownership;
- tenant isolation;
- retrieval/RAG authorization;
- memory and indexed data;
- agents/tools/MCP.

The selected OpenHands Agent Canvas source adds or emphasizes:

- direct command execution;
- local/remote/cloud agent-server backends;
- host filesystem access;
- optional Docker sandboxing;
- workspace file operations;
- per-backend/session API keys;
- cloud/runtime proxying;
- MCP credentials;
- long-lived automations/integrations;
- desktop/Electron URL boundaries.

## OpenHands-specific threat-model deltas

### OH-T01 — Host command execution

The selected source documentation explicitly states that an agent may execute
shell commands and, in direct-host configurations, can have broad filesystem
and network access.

Security consequence:

The sandbox/runtime boundary becomes a primary security boundary rather than
an auxiliary feature.

TRANSFER_PRIORITY=CRITICAL

### OH-T02 — Filesystem/workspace scope

OpenHands can operate on project directories and runtime workspaces.

The selected upload-path implementation reduces supplied file names to a leaf
name and includes traversal-oriented tests.

This is useful static evidence, but it does not establish complete runtime
filesystem confinement.

TRANSFER_PRIORITY=HIGH

### OH-T03 — Session/API-key trust

The selected self-hosting documentation describes LOCAL_BACKEND_API_KEY and
X-Session-API-Key protection for exposed agent-server APIs.

Static source also distinguishes local and cloud authentication behavior.

No live authentication bypass assessment was executed.

TRANSFER_PRIORITY=HIGH

### OH-T04 — Multi-backend / proxy trust

The selected Canvas source supports local, remote and cloud backends.

Its cloud proxy surface includes dynamic request path/header handling,
hostOverride and multiple authentication modes.

These are high-value trust boundaries for a future runtime assessment.

TRANSFER_PRIORITY=HIGH

### OH-T05 — MCP credential propagation

The selected source contains:

- stored/redacted MCP credential substitution;
- MCP secret-redaction logic;
- MCP-oriented unit-test sources.

This is evidence of implemented control surfaces.

It is not a live MCP authorization or SSRF assessment.

TRANSFER_PRIORITY=HIGH

### OH-T06 — Tool/command confirmation

The selected source exposes a confirmation-mode state.

This transfer does not establish where every confirmation decision is enforced
or whether every dangerous action is mediated.

TRANSFER_PRIORITY=HIGH

### OH-T07 — Same-origin credential exposure boundary

The selected self-hosting documentation explicitly records that the bundled
editor shares the Canvas browser origin and that script executing on that
origin can access localStorage containing backend session API keys.

This is treated here as a source-documented product risk/boundary, not as a
new vulnerability independently discovered by this project.

TRANSFER_PRIORITY=HIGH

### OH-T08 — Desktop URL handling

The selected Electron source parses URLs and restricts:

- internal app-window URLs to loopback HTTP(S);
- OS external browsing to an explicit protocol allowlist.

This is static control evidence only.

TRANSFER_PRIORITY=MEDIUM

## Transfer conclusion

The security-engineering method transfers strongly from Onyx to OpenHands:

authorization

→ architecture/trust boundaries

→ threat modeling

→ high-risk capability inventory

→ secret/identity analysis

→ agent/tool/MCP analysis

→ sandbox/code-execution analysis

→ bounded negative testing

→ regression

→ residual risk

→ release/incident handling.

However, the product-specific test plan must change substantially because
OpenHands places command execution, filesystem access, remote backends,
session API keys, sandboxing and automation near the center of its trust
model.

TRANSFER_METHOD_REUSABLE=YES_WITH_PRODUCT_SPECIFIC_ADAPTATION

OPENHANDS_RUNTIME_SECURITY_COMPLETE=NO

OPENHANDS_SECURITY_ASSESSMENT_EXECUTED=STATIC_ONLY

ACTION_25.19=PASS_STATIC_TRANSFER_THREAT_CONTROL_ASSESSMENT
