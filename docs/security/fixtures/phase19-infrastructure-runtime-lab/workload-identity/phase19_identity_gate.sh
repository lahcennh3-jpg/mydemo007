#!/usr/bin/env bash
set -euo pipefail

source \
"docs/security/fixtures/phase19-infrastructure-runtime-lab/workload-identity/workload-identity-policy.env"

test "$TRUST_DOMAIN" = "phase19.local"
test "$IDENTITY_SCHEME" = "spiffe"
test "$ATTESTATION_REQUIRED" = "true"
test "$STATIC_LONG_LIVED_CREDENTIALS_ALLOWED" = "false"
test "$MAX_CREDENTIAL_TTL_SECONDS" -le 900
test "$ROTATE_BEFORE_EXPIRY_SECONDS" -gt 0
test "$ROTATE_BEFORE_EXPIRY_SECONDS" -lt "$MAX_CREDENTIAL_TTL_SECONDS"
test "$REVOCATION_REQUIRED" = "true"
test "$REVOCATION_PROPAGATION_MAX_SECONDS" -le 300
test "$FAIL_CLOSED_ON_IDENTITY_FAILURE" = "true"
test "$FAIL_CLOSED_ON_ATTESTATION_FAILURE" = "true"
test "$FAIL_CLOSED_ON_REVOCATION_CHECK_FAILURE" = "true"

echo "PHASE19_IDENTITY_GATE=PASS"
echo "ATTESTATION=PASS"
echo "SHORT_LIVED_CREDENTIALS=PASS"
echo "ROTATION=PASS"
echo "REVOCATION=PASS"
echo "FAIL_CLOSED=PASS"
