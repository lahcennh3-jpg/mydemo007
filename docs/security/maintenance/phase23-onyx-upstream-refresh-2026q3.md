# Phase 23 — 2026 Q3 Onyx Upstream Technical Refresh

Review timestamp UTC:

`2026-09-26T13:41:31Z`

## Protected project baseline

Original verified Onyx source baseline:

`160f9b143605ca45a85bd387b5bd173840bab15d`

The baseline has not been modified by this maintenance action.

LAB_BASELINE_CHANGED=NO

UPGRADE_AUTHORIZED=NO

## Current upstream release

Repository:

`onyx-dot-app/onyx`

Latest release tag returned by the official GitHub API:

`v4.8.1`

Release name:

`v4.8.1`

Published:

`2026-09-24T17:49:19Z`

Release page:

https://github.com/onyx-dot-app/onyx/releases/tag/v4.8.1

## Baseline-to-current comparison

GitHub comparison status:

`ahead`

Ahead by:

`53`

Behind by:

`0`

Total commits reported:

`53`

Commit objects returned by the comparison API:

`53`

File objects returned by the comparison API:

`300`

Security-interest file paths identified by bounded keyword triage:

`194`

Release-note security-interest terms:

`connector,deployment,mcp,oauth,tool`

## Security-interest path sample

The following is a bounded triage list, not a complete security assessment.

```text
.github/workflows/pr-external-dependency-unit-tests.yml
.github/workflows/release-devtools.yml
backend/alembic/versions/47a07e1a38f1_fix_invalid_model_configurations_state.py
backend/alembic/versions/7a70b7664e37_add_model_configuration_table.py
backend/ee/onyx/access/access.py
backend/ee/onyx/background/celery/tasks/doc_permission_syncing/tasks.py
backend/ee/onyx/background/celery/tasks/external_group_syncing/tasks.py
backend/ee/onyx/connectors/capability_checks.py
backend/ee/onyx/db/user_group.py
backend/ee/onyx/external_permissions/github/doc_sync.py
backend/ee/onyx/external_permissions/github/group_sync.py
backend/ee/onyx/external_permissions/github/utils.py
backend/ee/onyx/external_permissions/outlook/doc_sync.py
backend/ee/onyx/external_permissions/sharepoint/permission_utils.py
backend/ee/onyx/external_permissions/sync_params.py
backend/model_server/main.py
backend/onyx/access/access.py
backend/onyx/access/models.py
backend/onyx/auth/api_key.py
backend/onyx/auth/captcha.py
backend/onyx/auth/invited_users.py
backend/onyx/auth/login_claims_capture.py
backend/onyx/auth/users.py
backend/onyx/cache/locks.py
backend/onyx/chat/llm_loop.py
backend/onyx/chat/llm_step.py
backend/onyx/chat/models.py
backend/onyx/chat/prompt_utils.py
backend/onyx/connectors/axero/connector.py
backend/onyx/connectors/bitbucket/utils.py
backend/onyx/connectors/blob/connector.py
backend/onyx/connectors/braintrust/connector.py
backend/onyx/connectors/canvas/client.py
backend/onyx/connectors/canvas/connector.py
backend/onyx/connectors/capability_checks/registry.py
backend/onyx/connectors/clickup/connector.py
backend/onyx/connectors/confluence/connector.py
backend/onyx/connectors/discord/connector.py
backend/onyx/connectors/drupal_wiki/connector.py
backend/onyx/connectors/freshdesk/connector.py
backend/onyx/connectors/gitlab/connector.py
backend/onyx/connectors/gmail/connector.py
backend/onyx/connectors/google_drive/doc_conversion.py
backend/onyx/connectors/highspot/connector.py
backend/onyx/connectors/hubspot/connector.py
backend/onyx/connectors/interfaces.py
backend/onyx/connectors/lumapps/connector.py
backend/onyx/connectors/microsoft_utils/drive_items.py
backend/onyx/connectors/microsoft_utils/graph_client.py
backend/onyx/connectors/notion/connector.py
backend/onyx/connectors/outlook/__init__.py
backend/onyx/connectors/outlook/capability_checks.py
backend/onyx/connectors/outlook/connector.py
backend/onyx/connectors/outlook/errors.py
backend/onyx/connectors/outlook/mailboxes.py
backend/onyx/connectors/outlook/models.py
backend/onyx/connectors/outlook/source_operations.py
backend/onyx/connectors/registry.py
backend/onyx/connectors/salesforce/blacklist.py
backend/onyx/connectors/salesforce/shelve_stuff/old_test_salesforce_shelves.py
backend/onyx/connectors/salesforce/shelve_stuff/test_salesforce_shelves.py
backend/onyx/connectors/sharepoint/connector.py
backend/onyx/connectors/sharepoint/connector_utils.py
backend/onyx/connectors/slack/connector.py
backend/onyx/connectors/teams/connector.py
backend/onyx/connectors/zoom/client.py
backend/onyx/connectors/zoom/connector.py
backend/onyx/connectors/zoom/endpoints.py
backend/onyx/connectors/zoom/models.py
backend/onyx/connectors/zoom/rate_limit.py
backend/onyx/connectors/zoom/recordings/access.py
backend/onyx/connectors/zoom/recordings/discovery.py
backend/onyx/connectors/zoom/recordings/models.py
backend/onyx/connectors/zoom/recordings/processing.py
backend/onyx/connectors/zoom/recordings/session_types.py
backend/onyx/context/search/models.py
backend/onyx/context/search/retrieval/search_runner.py
backend/onyx/db/connector_credential_pair.py
backend/onyx/db/llm.py
backend/onyx/db/models.py
backend/onyx/document_index/vespa/chunk_retrieval.py
backend/onyx/file_store/models.py
backend/onyx/llm/constants.py
backend/onyx/llm/factory.py
backend/onyx/llm/litellm_singleton/config.py
backend/onyx/llm/litellm_singleton/monkey_patches.py
backend/onyx/llm/model_capabilities.py
backend/onyx/llm/model_response.py
backend/onyx/llm/multi_llm.py
backend/onyx/llm/utils.py
backend/onyx/prompts/search_prompts.py
backend/onyx/redis/redis_connector_delete.py
backend/onyx/redis/redis_connector_prune.py
backend/onyx/redis/redis_usergroup.py
backend/onyx/secondary_llm_flows/document_filter.py
backend/onyx/server/documents/connector.py
backend/onyx/server/features/build/db/sandbox.py
backend/onyx/server/features/build/sandbox/kubernetes/kubernetes_sandbox_manager.py
backend/onyx/server/features/build/sandbox/user_library.py
backend/onyx/server/features/build/session/md_to_docx.py
backend/onyx/server/features/mcp/api.py
backend/onyx/server/features/mcp/credentials.py
backend/onyx/server/features/mcp/oauth.py
backend/onyx/server/manage/voice/models.py
backend/onyx/server/models.py
backend/onyx/server/query_and_chat/session_loading.py
backend/onyx/server/security/store.py
backend/onyx/tools/fake_tools/research_agent.py
backend/onyx/tools/tool_constructor.py
backend/onyx/tools/tool_implementations/custom/custom_tool.py
backend/onyx/tools/tool_implementations/search/search_tool.py
backend/onyx/tools/tool_implementations/search/search_utils.py
backend/onyx/tools/tool_implementations/web_search/clients/google_pse_client.py
backend/requirements/default.txt
backend/requirements/dev.txt
backend/requirements/ee.txt
backend/requirements/model_server.txt
backend/scripts/debugging/opensearch/embedding_io.py
backend/scripts/reencrypt_secrets.py
backend/scripts/tenant_cleanup/activity_utils.py
```

## Interpretation boundary

The GitHub comparison metadata is evidence for selecting maintenance work.

It is not itself proof that all security-relevant changes have been reviewed.

A keyword match is also not a vulnerability finding.

The following still require engineering review when applicable:

- authentication and OAuth;
- tenant isolation;
- authorization and permissions;
- MCP;
- agents and tools;
- connectors;
- RAG and retrieval;
- prompts;
- model-provider behavior;
- dependency and deployment changes;
- audit and telemetry changes.

## Upgrade rule

This action performs upstream surveillance only.

It does not:

- checkout the new release;
- replace the verified baseline;
- rebuild the runtime;
- migrate data;
- change deployment configuration;
- claim regression compatibility.

Any future baseline upgrade requires a separate authorization, test plan,
rollback plan and evidence package.

## Result

ACTION_23.8=PASS_ONYX_UPSTREAM_TECHNICAL_REFRESH
