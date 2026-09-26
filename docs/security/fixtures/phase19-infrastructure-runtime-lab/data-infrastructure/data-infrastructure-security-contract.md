# Phase 19 Data Infrastructure Security Contract

## Database

- Authentication is mandatory.
- Public database exposure is prohibited by default.
- Application and administrative roles are separated.
- Application roles follow least privilege.
- Tenant authorization remains enforced.
- Database credentials are not committed.

## Cache

- Cache systems remain private.
- Unauthenticated public access is prohibited.
- User and tenant cache keys require isolation.
- Cross-user cache-key collisions are security defects.

## Vector database

- Retrieval remains bound to requesting user/tenant authorization.
- Vector-store reachability does not authorize document access.
- Deleted or revoked content must not remain indefinitely retrievable.

## Object storage

- Public access is denied by default.
- Service credentials follow least privilege.
- Temporary access is time bounded.
- Sensitive content uses encryption where available.

## Backup

- Backup access is controlled.
- Integrity verification is required.
- Restore testing is required.
- Retention and deletion apply to backup copies.
- Real credentials are never committed as backup fixtures.
