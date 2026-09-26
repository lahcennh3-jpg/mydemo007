# Phase 21 — Action 21.1 — Assisted Clean Rebuild

Recorded: 2026-09-26T12:15:55Z

## Classification

PASS_ASSISTED_REBUILD

The bounded Onyx Lite lab was reconstructed from a separate clean worktree at:

`7aa32a730b337ace88db25fb579700a02b6b4216`

The commands were supplied by the assistant, so this is assisted evidence and
is not evidence of independent command selection.

## Fresh runtime

Before startup:

- project containers: none;
- project volumes: none.

A fresh PostgreSQL volume was created:

`phase21clean_db_volume`

Creation:

`2026-09-26T12:03:16Z`

## Services

```text
SERVICE=relational_db RUNNING=true HEALTH=healthy IMAGE_ID=sha256:d9c304353c031b21e9a7e33dc4781e272a9fa802a2ab9703fe4199d72ba1422c
SERVICE=api_server RUNNING=true HEALTH=healthy IMAGE_ID=sha256:fa570e141e39af5e1e48767fe14cbe227abe9a5ec0e3d08b9580c8bf60b35543
SERVICE=web_server RUNNING=true HEALTH=healthy IMAGE_ID=sha256:c967449a9e099fbc67d8f26f94c6b57d9a558bafdc7467a49708847d09f6deea
SERVICE=code-interpreter RUNNING=true HEALTH=healthy IMAGE_ID=sha256:e4d3e4d875309b90aaad810373dd8ea368e6692ffec6ac36b9eb2ea7f77f97f6
SERVICE=nginx RUNNING=true HEALTH=healthy IMAGE_ID=sha256:516475cc129da42866742567714ddc681e5eed7b9ee0b9e9c015e464b4221a00

```

ALL_FIVE_SERVICES_HEALTHY=PASS

## Database

```text
/var/run/postgresql:5432 - accepting connections
```

DATABASE_READY=PASS

## Onyx API

```text
status_code=200
{"success":true,"message":"ok","data":null}
```

API_HEALTH=PASS

## Code interpreter

```text
{"message": null, "status": "ok", "version": "0.4.7"}
```

CODE_INTERPRETER_HEALTH=PASS

## Isolation

NETWORK_INTERNAL=true

```text
SERVICE=relational_db HOST_PORTS=NONE
SERVICE=api_server HOST_PORTS=NONE
SERVICE=web_server HOST_PORTS=NONE
SERVICE=code-interpreter HOST_PORTS=NONE
SERVICE=nginx HOST_PORTS=NONE

```

EXECUTOR_PIN=onyxdotapp/python-executor-sci@sha256:185e1a7acfa2b7b3105f77a58fef3dc8bd310d5ad0f9a635e209aa4f8e94b1b8
EXECUTOR_WATCHDOG_INTERVAL=0

NETWORK_ISOLATION=PASS
HOST_PORT_EXPOSURE=NONE
EXECUTOR_PINNING=PASS

## Safety

REAL_CUSTOMER_DATA_USED=NO
REAL_CREDENTIALS_USED=NO
REAL_EXTERNAL_AI_API_USED=NO

## Rollback

Fresh containers, volumes, and project network were removed after verification.

ROLLBACK=PASS

## Final

SOURCE_IDENTITY=PASS
CLEAN_WORKTREE=PASS
FRESH_RUNTIME=PASS
FRESH_DATABASE_VOLUME=PASS
LITE_TOPOLOGY=5_SERVICES
ALL_FIVE_SERVICES_HEALTHY=PASS
DATABASE_READY=PASS
API_HEALTH=PASS
CODE_INTERPRETER_HEALTH=PASS
NETWORK_ISOLATION=PASS
HOST_PORT_EXPOSURE=NONE
EXECUTOR_PINNING=PASS
ROLLBACK=PASS

ACTION_RESULT=PASS_ASSISTED_REBUILD
INDEPENDENT_REBUILD=NOT_CLAIMED
