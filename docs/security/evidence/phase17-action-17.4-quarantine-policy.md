# Phase 17 — AI Artifact Quarantine Policy

## Default state

Every incoming AI artifact starts untrusted.

## Permitted trust transition

`source -> quarantine -> verification -> explicit approval -> approved`

A direct `source -> approved` transition is prohibited.

## Required verification

An artifact remains quarantined whenever any required property is
missing, invalid, conflicting, or unverifiable:

- source identity
- artifact identity
- version
- declared format
- cryptographic hash
- provenance
- license classification
- serialization analysis when applicable
- evaluation evidence
- explicit approval

## Serialized artifacts

Pickle-family artifacts must not be deserialized merely to inspect
their contents.

Inspection precedes any authorization to load or execute.

## Failure behavior

Verification failure is fail-closed.

The artifact remains quarantined or is rejected.

## Production boundary

Synthetic, unverified, quarantined, and revoked artifacts are not
authorized for production deployment by Phase 17.
