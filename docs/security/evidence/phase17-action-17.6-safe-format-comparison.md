# Phase 17 — Serialization Format Security Comparison

| Property | JSON | Pickle | Safetensors |
|---|---|---|---|
| Synthetic Batch-A artifact | Yes | Yes | No |
| Arbitrary Python reconstruction concern | No | Yes | No |
| Hash verification required | Yes | Yes | Yes |
| Provenance required | Yes | Yes | Yes |
| Quarantine before approval | Yes | Yes | Yes |
| Batch-A deserialization | No | No | No |

## JSON

The synthetic JSON artifact is treated as untrusted data until its
identity, hash, provenance, and approval state are verified.

## Pickle

Pickle receives stronger restrictions because serialized Python object
graphs can contain reconstruction behavior.

The Batch-A fixture was inspected as bytes only.

It was never deserialized.

The result cannot be generalized to arbitrary pickle files.

## Safetensors

Safetensors remains the selected safer tensor-format comparison target.

The package cannot currently be verified through the host Python
environment because the host does not provide Python.

This is recorded as a capability gap rather than hidden.

## Tool behavior

ModelScan, Fickling, Safetensors, and MLflow capabilities are not
silently marked successful.

Missing capabilities remain explicit until they can be exercised in an
approved environment.

No dependency is downloaded merely to satisfy the checklist.
