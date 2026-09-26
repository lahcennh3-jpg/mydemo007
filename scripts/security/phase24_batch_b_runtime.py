from __future__ import annotations

import os
import uuid

import httpx


BASE = os.environ["PHASE24_BASE_URL"].rstrip("/")
COOKIE_NAME = os.environ.get(
    "PHASE24_AUTH_COOKIE_NAME",
    "fastapiusersauth",
)

TIMEOUT = 5.0

rows: list[tuple[str, str, str, str, str, str]] = []


def record(
    case_id: str,
    evaluation_id: str,
    expectation: str,
    status: int | str,
    result: str,
    detail: str,
) -> None:
    # Never record bodies, cookies, passwords, or raw headers.
    safe_detail = (
        detail.replace("\t", " ")
        .replace("\n", " ")
        .replace("\r", " ")
    )

    rows.append(
        (
            case_id,
            evaluation_id,
            expectation,
            str(status),
            result,
            safe_detail,
        )
    )


def is_2xx(status: int) -> bool:
    return 200 <= status < 300


def create_user(prefix: str) -> tuple[httpx.Client | None, str]:
    client = httpx.Client(
        base_url=BASE,
        timeout=TIMEOUT,
        follow_redirects=False,
    )

    suffix = uuid.uuid4().hex

    # example.com is reserved for documentation/test use.
    email = f"phase24-{prefix}-{suffix}@example.com"

    # Synthetic, unique, never printed or persisted.
    password = f"P24-{uuid.uuid4().hex}-Aa1!"

    try:
        register = client.post(
            "/auth/register",
            json={
                "email": email,
                "username": email,
                "password": password,
            },
        )

        if not is_2xx(register.status_code):
            client.close()
            return None, f"register_http_{register.status_code}"

        login = client.post(
            "/auth/login",
            data={
                "username": email,
                "password": password,
            },
        )

        if not is_2xx(login.status_code):
            client.close()
            return None, f"login_http_{login.status_code}"

        me = client.get("/me")

        if me.status_code != 200:
            client.close()
            return None, f"me_http_{me.status_code}"

        return client, "ok"

    except Exception as exc:
        client.close()
        return None, f"exception_{type(exc).__name__}"


# ============================================================
# EV23-001 — AUTHENTICATION NEGATIVE PATHS
# ============================================================

try:
    with httpx.Client(
        base_url=BASE,
        timeout=TIMEOUT,
        follow_redirects=False,
    ) as unauth:
        r = unauth.get("/me")

        if r.status_code in {401, 403}:
            result = "PASS"
        elif is_2xx(r.status_code):
            result = "FAIL"
        else:
            result = "INCONCLUSIVE"

        record(
            "AUTH-001",
            "EV23-001",
            "UNAUTHENTICATED_ME_DENIED",
            r.status_code,
            result,
            "no_session_cookie",
        )

except Exception as exc:
    record(
        "AUTH-001",
        "EV23-001",
        "UNAUTHENTICATED_ME_DENIED",
        "NA",
        "INCONCLUSIVE",
        f"exception_{type(exc).__name__}",
    )


try:
    with httpx.Client(
        base_url=BASE,
        timeout=TIMEOUT,
        follow_redirects=False,
        cookies={COOKIE_NAME: "phase24-invalid-session-token"},
    ) as invalid_cookie:
        r = invalid_cookie.get("/me")

        if r.status_code in {401, 403}:
            result = "PASS"
        elif is_2xx(r.status_code):
            result = "FAIL"
        else:
            result = "INCONCLUSIVE"

        record(
            "AUTH-002",
            "EV23-001",
            "INVALID_SESSION_DENIED",
            r.status_code,
            result,
            "synthetic_invalid_cookie",
        )

except Exception as exc:
    record(
        "AUTH-002",
        "EV23-001",
        "INVALID_SESSION_DENIED",
        "NA",
        "INCONCLUSIVE",
        f"exception_{type(exc).__name__}",
    )


try:
    with httpx.Client(
        base_url=BASE,
        timeout=TIMEOUT,
        follow_redirects=False,
    ) as invalid_login:
        r = invalid_login.post(
            "/auth/login",
            data={
                "username": f"nonexistent-{uuid.uuid4().hex}@example.com",
                "password": f"invalid-{uuid.uuid4().hex}",
            },
        )

        if r.status_code in {400, 401, 403}:
            result = "PASS"
        elif is_2xx(r.status_code):
            result = "FAIL"
        else:
            result = "INCONCLUSIVE"

        record(
            "AUTH-003",
            "EV23-001",
            "INVALID_CREDENTIALS_DENIED",
            r.status_code,
            result,
            "synthetic_nonexistent_identity",
        )

except Exception as exc:
    record(
        "AUTH-003",
        "EV23-001",
        "INVALID_CREDENTIALS_DENIED",
        "NA",
        "INCONCLUSIVE",
        f"exception_{type(exc).__name__}",
    )


# Positive control. The first user also establishes an existing user before
# Alice/Bob creation so subsequent users follow the normal basic-user path.
bootstrap, bootstrap_reason = create_user("bootstrap")

if bootstrap is None:
    record(
        "AUTH-004",
        "EV23-001",
        "VALID_LOGIN_POSITIVE_CONTROL",
        "NA",
        "INCONCLUSIVE",
        bootstrap_reason,
    )
else:
    try:
        r = bootstrap.get("/me")

        record(
            "AUTH-004",
            "EV23-001",
            "VALID_LOGIN_POSITIVE_CONTROL",
            r.status_code,
            "PASS" if r.status_code == 200 else "FAIL",
            "valid_synthetic_session",
        )
    finally:
        bootstrap.close()


# ============================================================
# EV23-002 — BOLA / OBJECT OWNERSHIP
# ============================================================

alice, alice_reason = create_user("alice")
bob, bob_reason = create_user("bob")

if alice is None or bob is None:
    reason = (
        f"alice={alice_reason};bob={bob_reason}"
    )

    record(
        "BOLA-SETUP",
        "EV23-002",
        "TWO_AUTHENTICATED_USERS_REQUIRED",
        "NA",
        "BLOCKED",
        reason,
    )

    if alice is not None:
        alice.close()
    if bob is not None:
        bob.close()

else:
    try:
        create = alice.post(
            "/chat/create-chat-session",
            json={
                "persona_id": 0,
                "description": "Phase24 synthetic ownership regression",
            },
        )

        record(
            "BOLA-001",
            "EV23-002",
            "OWNER_CREATES_OBJECT",
            create.status_code,
            "PASS" if is_2xx(create.status_code) else "INCONCLUSIVE",
            "synthetic_chat_session",
        )

        if not is_2xx(create.status_code):
            record(
                "BOLA-002",
                "EV23-002",
                "OWNER_CAN_READ_OBJECT",
                "NA",
                "BLOCKED",
                "owner_object_creation_failed",
            )

            record(
                "BOLA-003",
                "EV23-002",
                "NON_OWNER_READ_DENIED",
                "NA",
                "BLOCKED",
                "owner_object_creation_failed",
            )

            record(
                "BOLA-004",
                "EV23-002",
                "NON_OWNER_DELETE_DENIED",
                "NA",
                "BLOCKED",
                "owner_object_creation_failed",
            )

            record(
                "BOLA-005",
                "EV23-002",
                "OBJECT_REMAINS_AFTER_INTRUDER_DELETE",
                "NA",
                "BLOCKED",
                "owner_object_creation_failed",
            )

        else:
            try:
                chat_id = create.json()["chat_session_id"]
            except Exception:
                chat_id = None

            if not chat_id:
                for cid, exp in (
                    ("BOLA-002", "OWNER_CAN_READ_OBJECT"),
                    ("BOLA-003", "NON_OWNER_READ_DENIED"),
                    ("BOLA-004", "NON_OWNER_DELETE_DENIED"),
                    (
                        "BOLA-005",
                        "OBJECT_REMAINS_AFTER_INTRUDER_DELETE",
                    ),
                ):
                    record(
                        cid,
                        "EV23-002",
                        exp,
                        "NA",
                        "INCONCLUSIVE",
                        "chat_id_missing_from_success_response",
                    )

            else:
                owner_read = alice.get(
                    f"/chat/get-chat-session/{chat_id}"
                )

                record(
                    "BOLA-002",
                    "EV23-002",
                    "OWNER_CAN_READ_OBJECT",
                    owner_read.status_code,
                    "PASS"
                    if owner_read.status_code == 200
                    else "FAIL",
                    "owner_positive_control",
                )

                intruder_read = bob.get(
                    f"/chat/get-chat-session/{chat_id}"
                )

                if intruder_read.status_code in {403, 404}:
                    intruder_read_result = "PASS"
                elif is_2xx(intruder_read.status_code):
                    intruder_read_result = "FAIL"
                else:
                    intruder_read_result = "INCONCLUSIVE"

                record(
                    "BOLA-003",
                    "EV23-002",
                    "NON_OWNER_READ_DENIED",
                    intruder_read.status_code,
                    intruder_read_result,
                    "cross_user_read",
                )

                intruder_delete = bob.delete(
                    f"/chat/delete-chat-session/{chat_id}"
                )

                if intruder_delete.status_code in {403, 404}:
                    intruder_delete_result = "PASS"
                elif is_2xx(intruder_delete.status_code):
                    intruder_delete_result = "FAIL"
                else:
                    intruder_delete_result = "INCONCLUSIVE"

                record(
                    "BOLA-004",
                    "EV23-002",
                    "NON_OWNER_DELETE_DENIED",
                    intruder_delete.status_code,
                    intruder_delete_result,
                    "cross_user_delete",
                )

                owner_after = alice.get(
                    f"/chat/get-chat-session/{chat_id}"
                )

                record(
                    "BOLA-005",
                    "EV23-002",
                    "OBJECT_REMAINS_AFTER_INTRUDER_DELETE",
                    owner_after.status_code,
                    "PASS"
                    if owner_after.status_code == 200
                    else "FAIL",
                    "post_attack_owner_control",
                )

    except Exception as exc:
        record(
            "BOLA-ERROR",
            "EV23-002",
            "OBJECT_OWNERSHIP_RUNTIME",
            "NA",
            "INCONCLUSIVE",
            f"exception_{type(exc).__name__}",
        )

    finally:
        alice.close()
        bob.close()


# ============================================================
# EV23-003 / EV23-004 — EXPLICIT BLOCKED DISPOSITIONS
# ============================================================

record(
    "TENANT-001",
    "EV23-003",
    "CROSS_TENANT_RUNTIME_ISOLATION",
    "NA",
    "BLOCKED",
    "second_tenant_fixture_not_established_in_current_control_plane_baseline",
)

record(
    "RAG-001",
    "EV23-004",
    "RAG_AUTHORIZATION_AND_REVOCATION",
    "NA",
    "BLOCKED",
    "model_dependent_security_validation_complete_no",
)


print(
    "case_id\tevaluation_id\texpectation\t"
    "http_status\tresult\tdetail"
)

for row in rows:
    print("\t".join(row))
