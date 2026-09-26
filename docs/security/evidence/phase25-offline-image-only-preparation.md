# Phase 25 — Offline image-only preparation result

## Source and status

The user supplied the Codespace terminal output on 2026-09-26.
The output shows a run on branch
`security/phase25-offline-image-only-amendment` at commit
`29821a80d2721c79ddbd0a6542507681b50f5943`.
The script reported `IMAGE_ONLY_PREPARATION=PASS`.
This record quotes that output. It is not independent access to the user's Docker daemon.

The generated context was `/tmp/phase25-overlay-context.UDQB6Z`.
The local run evidence was `/tmp/phase25-overlay-evidence.XtUpUD`.
These temporary paths belong to the user's Codespace.

## Image and file evidence

| Field | Reported value |
| --- | --- |
| Source commit | `193c7c4b652fc3ae76256718f53d0a956e996b7f` |
| Base image ID | `sha256:fa570e141e39af5e1e48767fe14cbe227abe9a5ec0e3d08b9580c8bf60b35543` |
| Overlay tag | `localhost/phase25-six-file-overlay:193c7c4b652f` |
| Overlay image ID | `sha256:d2ca7ce3605f475028b72ec0a2fd18489ab4cfcd696296c8e785a835e1ba2020` |
| Dockerfile SHA-256 | `8326632c4d67955728771ad5778632c4c3df3a7039f1ace91a55f576f826741e` |

| File under `backend/` | Reported source and image SHA-256 | Result |
| --- | --- | --- |
| `onyx/server/features/mcp/models.py` | `c5841337a7c4f3f314e25513054497e82c8c031a532da579987af044d06c7e1d` | MATCH |
| `onyx/utils/redaction.py` | `74596da3146d95bb7983440d1b56cfaa47d931ab9f1acd81c5b41e23ef1c3b39` | MATCH |
| `onyx/tools/tool_runner.py` | `6f59309ac41869331c14c86b25f058a4cb3f4ab87a5b8b6369b557c4d9c14067` | MATCH |
| `onyx/tools/models.py` | `14f6edd0455c9723cda77b6ff8886a29be62202ed1efa6b7b85a4ea24af5835f` | MATCH |
| `onyx/background/celery/tasks/user_file_processing/tasks.py` | `85440a3765014bf1641b6aae2c4320c2e35ed39e41bd8a32725209fb1fcabcd1` | MATCH |
| `onyx/configs/constants.py` | `7efb89f22ff6ed2e9ba75b8eee3961fdb15a4b11940250aecffdf0a6d6dc6c9c` | MATCH |

We independently calculated the six source hashes from Git commit
`193c7c4b652fc3ae76256718f53d0a956e996b7f`.
They match the reported values. We also reconstructed the generated
Dockerfile from the published script and matched its reported SHA-256.
We did not independently inspect the overlay image ID or the build log.

## Boundary and remaining work

The script reported that the original API container ID and image ID
were unchanged during the run. The script does not deploy the overlay,
restart the API, or access the database. The user's output reported
`FULL_SOURCE_BUILD_AND_RUNTIME_CORRESPONDENCE=NOT_ESTABLISHED`.

This result prepares one local image. It does not resolve the three
blocked Batch C states, establish a full source build, or approve runtime
testing with the overlay image.
