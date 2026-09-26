# Phase 19 Admission Policy Contract

A workload is rejected when any of these conditions are violated:

1. Container images must not use mutable `latest` tags.
2. Production-target images must be pinned to a digest.
3. Privileged containers are prohibited.
4. Host PID, host IPC, and host networking are prohibited by default.
5. Privilege escalation must be disabled.
6. Containers must run as non-root.
7. Root filesystems should be read-only unless an approved exception exists.
8. Linux capabilities are dropped by default.
9. RuntimeDefault or stronger seccomp must be used.
10. Resource requests and limits are required.
11. Service-account tokens are not automatically mounted unless required.
12. Cluster-admin bindings require explicit security approval.
13. HostPath volumes require explicit security approval.
14. Namespace network policy defaults to deny.
15. Secrets must not be embedded in committed workload manifests.
