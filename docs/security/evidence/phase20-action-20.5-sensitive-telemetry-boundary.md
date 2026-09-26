# Phase 20 — Sensitive Telemetry Boundary

## Never intentionally place in Phase 20 evidence

- real passwords;
- API keys;
- access tokens;
- refresh tokens;
- session cookies;
- private keys;
- real customer data;
- raw production prompts;
- raw production retrieved documents.

## Minimize

- email addresses;
- document names;
- conversation titles;
- user-generated text;
- model inputs/outputs;
- tool arguments;
- URLs containing credentials or sensitive query parameters.

## Preferred investigation fields

Use opaque or synthetic identifiers for:

- user;
- tenant;
- conversation;
- document;
- agent;
- tool;
- request;
- trace.

## Detection design rule

A detection that requires unnecessary secret or content logging is not
considered a safe detection design.

## Evidence boundary

Phase 20 uses repository inspection and synthetic security-event fixtures.

No real production telemetry is authorized.
