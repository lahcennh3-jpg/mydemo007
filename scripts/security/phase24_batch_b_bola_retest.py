from __future__ import annotations

import os
import uuid

import httpx


BASE = os.environ["PHASE24_BASE_URL"].rstrip("/")
TIMEOUT = 5.0

rows: list[tuple[str, str, str, str, str]] = []


def add(
    case_id: str,
    expectation: str,
    status: int | str,
    result: str,
    detail: str,
) -> None:
    rows.append(
        (
            case_id,
            expectation,
            str(status),
            result,
            detail.replace("\t", " ").replace("\n", " "),
        )
    )


def create_user(prefix: str) -> httpx.Client:
    client = httpx.Client(
        base_url=BASE,
        timeout=TIMEOUT,
        follow_redirects=False,
    )

    suffix = uuid.uuid4().hex
    email = f"phase24-retest-{prefix}-{suffix}@example.com"
    password = f"P24-R-{uuid.uuid4().hex}-Aa1!"

    r = client.post(
        "/auth/register",
        json={
            "email": email,
            "username": email,
            "password": password,
        },
    )
    r.raise_for_status()

    r = client.post(
        "/auth/login",
        data={
            "username": email,
            "password": password,
        },
    )
    r.raise_for_status()

    r = client.get("/me")
    r.raise_for_status()

    return client


# Bootstrap the first account separately.
bootstrap = create_user("bootstrap")
bootstrap.close()

owner = create_user("owner")
intruder = create_user("intruder")

try:
    create = owner.post(
        "/chat/create-chat-session",
        json={
            "persona_id": 0,
            "description": "Phase24 BOLA stop retest",
        },
    )

    add(
        "BOLA-R01",
        "OWNER_CREATES_SESSION",
        create.status_code,
        "PASS" if create.status_code == 200 else "FAIL",
        "positive_control",
    )

    if create.status_code != 200:
        raise SystemExit("owner session creation failed")

    session_id = create.json()["chat_session_id"]

    owner_read = owner.get(
        f"/chat/get-chat-session/{session_id}"
    )

    add(
        "BOLA-R02",
        "OWNER_CAN_READ_SESSION",
        owner_read.status_code,
        "PASS" if owner_read.status_code == 200 else "FAIL",
        "positive_control",
    )

    intruder_read = intruder.get(
        f"/chat/get-chat-session/{session_id}"
    )

    add(
        "BOLA-R03",
        "NON_OWNER_READ_DENIED",
        intruder_read.status_code,
        "PASS"
        if intruder_read.status_code in {403, 404}
        else "FAIL",
        "cross_user_read",
    )

    # Documented existing integration contract:
    # owner stop -> 200
    # non-owner stop -> 404
    intruder_stop = intruder.post(
        f"/chat/stop-chat-session/{session_id}"
    )

    add(
        "BOLA-R04",
        "NON_OWNER_STOP_DENIED",
        intruder_stop.status_code,
        "PASS"
        if intruder_stop.status_code == 404
        else "FAIL",
        "cross_user_state_change",
    )

    # Crucial positive control: same route/object must work for owner.
    owner_stop = owner.post(
        f"/chat/stop-chat-session/{session_id}"
    )

    add(
        "BOLA-R05",
        "OWNER_STOP_ALLOWED",
        owner_stop.status_code,
        "PASS"
        if owner_stop.status_code == 200
        else "FAIL",
        "owner_positive_control_same_route",
    )

    owner_after = owner.get(
        f"/chat/get-chat-session/{session_id}"
    )

    add(
        "BOLA-R06",
        "OWNER_STILL_READS_SESSION",
        owner_after.status_code,
        "PASS"
        if owner_after.status_code == 200
        else "FAIL",
        "post_retest_integrity_control",
    )

finally:
    owner.close()
    intruder.close()


print("case_id\texpectation\thttp_status\tresult\tdetail")

for row in rows:
    print("\t".join(row))
