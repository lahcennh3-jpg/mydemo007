import unittest
from types import SimpleNamespace
from unittest.mock import MagicMock
from uuid import uuid4

from sqlalchemy.orm import Session

from onyx.access.access import (
    _user_can_access_generated_image,
    collect_user_file_access,
)
from onyx.db.models import FileRecord
from onyx.file_store.constants import (
    CHAT_IMAGE_GEN_CHAT_SESSION_ID_METADATA_KEY,
    CHAT_IMAGE_GEN_OWNER_USER_ID_METADATA_KEY,
)


ALICE = "alice@tenant-alpha.test"
BOB = "bob@tenant-alpha.test"


def _user(email: str):
    return SimpleNamespace(
        id=uuid4(),
        email=email,
    )


def _image_db(
    metadata: dict,
    *,
    public_session: bool = False,
) -> MagicMock:
    db_session = MagicMock(spec=Session)

    file_result = MagicMock()
    file_result.scalar_one_or_none.return_value = FileRecord(
        file_metadata=metadata
    )

    session_result = MagicMock()
    session_result.first.return_value = (
        (uuid4(),) if public_session else None
    )

    db_session.execute.side_effect = [
        file_result,
        session_result,
    ]

    return db_session


def _user_file(
    *,
    owner,
    shared_user=None,
):
    user_file = SimpleNamespace(
        id=uuid4(),
        user=owner,
        user_id=owner.id,
        assistants=[],
    )

    if shared_user is None:
        return user_file

    persona = SimpleNamespace(
        deleted=False,
        is_public=False,
        user_id=owner.id,
        user=owner,
        users=[shared_user],
    )

    user_file.assistants = [persona]

    return user_file


class TestPhase12CrossUserPrivacyNegative(unittest.TestCase):

    def test_generated_image_owner_allowed(self) -> None:
        owner = _user(ALICE)

        db_session = _image_db(
            {
                CHAT_IMAGE_GEN_OWNER_USER_ID_METADATA_KEY:
                    str(owner.id),
                CHAT_IMAGE_GEN_CHAT_SESSION_ID_METADATA_KEY:
                    str(uuid4()),
            }
        )

        self.assertTrue(
            _user_can_access_generated_image(
                "phase12-synthetic-image",
                owner,
                db_session,
            )
        )

    def test_foreign_private_generated_image_denied(self) -> None:
        owner = _user(ALICE)
        foreign_user = _user(BOB)

        db_session = _image_db(
            {
                CHAT_IMAGE_GEN_OWNER_USER_ID_METADATA_KEY:
                    str(owner.id),
                CHAT_IMAGE_GEN_CHAT_SESSION_ID_METADATA_KEY:
                    str(uuid4()),
            },
            public_session=False,
        )

        self.assertFalse(
            _user_can_access_generated_image(
                "phase12-synthetic-image",
                foreign_user,
                db_session,
            )
        )

    def test_malformed_generated_image_owner_fails_closed(self) -> None:
        foreign_user = _user(BOB)

        db_session = _image_db(
            {
                CHAT_IMAGE_GEN_OWNER_USER_ID_METADATA_KEY:
                    "not-a-uuid",
                CHAT_IMAGE_GEN_CHAT_SESSION_ID_METADATA_KEY:
                    str(uuid4()),
            },
            public_session=True,
        )

        self.assertFalse(
            _user_can_access_generated_image(
                "phase12-synthetic-image",
                foreign_user,
                db_session,
            )
        )

    def test_private_user_file_excludes_foreign_user(self) -> None:
        owner = _user(ALICE)
        foreign_user = _user(BOB)

        user_file = _user_file(owner=owner)

        emails, is_public = collect_user_file_access(
            user_file
        )

        self.assertEqual(emails, {ALICE})
        self.assertNotIn(
            foreign_user.email,
            emails,
        )
        self.assertFalse(is_public)

    def test_explicit_share_includes_shared_user(self) -> None:
        owner = _user(ALICE)
        shared_user = _user(BOB)

        user_file = _user_file(
            owner=owner,
            shared_user=shared_user,
        )

        emails, is_public = collect_user_file_access(
            user_file
        )

        self.assertIn(ALICE, emails)
        self.assertIn(BOB, emails)
        self.assertFalse(is_public)


if __name__ == "__main__":
    unittest.main()
