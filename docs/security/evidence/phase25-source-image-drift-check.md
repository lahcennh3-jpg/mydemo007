# Phase 25 source and running image check

The project owner ran a read-only comparison in the Codespace on
2026-09-26. The source commit was
`193c7c4b652fc3ae76256718f53d0a956e996b7f`.
The API used image ID
`sha256:fa570e141e39af5e1e48767fe14cbe227abe9a5ec0e3d08b9580c8bf60b35543`.
Its revision label was `01f746bc7d922ff53ffebbab1e68011a69bda4ae`.

The check hashed six source files and the corresponding files in
`onyx-api_server-1:/app`. This table records the project owner's output.
The source hashes were also checked against the repository checkout.

| File under `onyx/` | Source SHA-256 | Running SHA-256 | Result |
| --- | --- | --- | --- |
| `server/features/mcp/models.py` | `c5841337a7c4f3f314e25513054497e82c8c031a532da579987af044d06c7e1d` | `00636364570cf2c020fc9581598e3156c72bf9f7b0a787c333a67e3f5460dc69` | DIFF |
| `utils/redaction.py` | `74596da3146d95bb7983440d1b56cfaa47d931ab9f1acd81c5b41e23ef1c3b39` | `74596da3146d95bb7983440d1b56cfaa47d931ab9f1acd81c5b41e23ef1c3b39` | MATCH |
| `tools/tool_runner.py` | `6f59309ac41869331c14c86b25f058a4cb3f4ab87a5b8b6369b557c4d9c14067` | `6f2dcd56492315c1a11241e7c9958930bbb8d3839d9e21fe85b172aabb1d195d` | DIFF |
| `tools/models.py` | `14f6edd0455c9723cda77b6ff8886a29be62202ed1efa6b7b85a4ea24af5835f` | `14f6edd0455c9723cda77b6ff8886a29be62202ed1efa6b7b85a4ea24af5835f` | MATCH |
| `background/celery/tasks/user_file_processing/tasks.py` | `85440a3765014bf1641b6aae2c4320c2e35ed39e41bd8a32725209fb1fcabcd1` | `85440a3765014bf1641b6aae2c4320c2e35ed39e41bd8a32725209fb1fcabcd1` | MATCH |
| `configs/constants.py` | `7efb89f22ff6ed2e9ba75b8eee3961fdb15a4b11940250aecffdf0a6d6dc6c9c` | `e9ef540ea2263e8ad6e5f19101f0edd7e7fcbf593e18663d9ab3e824a2a0c704` | DIFF |

Three files match and three differ. The running image does not match the
reviewed source for these selected code paths. The earlier Batch C control
gate passed, but that result does not establish that the running API uses
the reviewed MCP or tool runner code.

The Phase 24 baseline records database revision `ad99acb9be41`.
Batch C checks that revision as part of EV012. The current source contains
a migration with `down_revision = "ad99acb9be41"`.
Do not start this source with the original Compose command against the
running database until an isolated migration test and rollback exist.

This selected-file check does not inventory all image files or dependencies.
It does not establish a reproducible build. R24-006 remains open.
