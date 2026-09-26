# Phase 19 Workload Identity Contract

Synthetic identity example:

`spiffe://phase19.local/ns/onyx/sa/api-server`

Requirements:

- identity is workload-bound;
- identity is not accepted from a user-controlled header;
- successful attestation is required before credential issuance;
- credentials are short-lived;
- normal workloads do not use shared permanent credentials;
- rotation occurs before expiry;
- compromised identities can be revoked independently;
- identity, attestation, and revocation-check failures fail closed;
- no permanent fallback credential is allowed.

All Phase 19 credentials are synthetic.
