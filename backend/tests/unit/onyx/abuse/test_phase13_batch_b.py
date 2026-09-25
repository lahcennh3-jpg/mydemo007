import unittest
from unittest.mock import patch
from uuid import UUID

from onyx.configs.constants import (
    CELERY_EXTERNAL_GROUP_SYNC_LOCK_TIMEOUT,
    CELERY_GENERIC_BEAT_LOCK_TIMEOUT,
    CELERY_USER_FILE_DELETE_TASK_EXPIRES,
    CELERY_USER_FILE_PROCESSING_LOCK_TIMEOUT,
    CELERY_USER_FILE_PROCESSING_TASK_EXPIRES,
    CELERY_USER_FILE_PROJECT_SYNC_LOCK_TIMEOUT,
    CELERY_USER_FILE_PROJECT_SYNC_TASK_EXPIRES,
    USER_FILE_DELETE_MAX_QUEUE_DEPTH,
    USER_FILE_PROCESSING_MAX_QUEUE_DEPTH,
    USER_FILE_PROJECT_SYNC_MAX_QUEUE_DEPTH,
)

from onyx.background.celery.tasks.user_file_processing import tasks as uf


FID = UUID("00000000-0000-0000-0000-000000000013")
TENANT = "phase13-synthetic"


class FakeLock:
    def __init__(self):
        self.acquired = False
        self.released = False

    def acquire(self, blocking=False):
        self.acquired = True
        return True

    def owned(self):
        return self.acquired and not self.released

    def release(self):
        self.released = True


class FakeRedis:
    def __init__(self):
        self.keys = set()
        self.deleted = []
        self.lock_obj = FakeLock()

    def set(self, key, value, nx=False, ex=None):
        if nx and key in self.keys:
            return False
        self.keys.add(key)
        return True

    def delete(self, key):
        self.deleted.append(key)
        self.keys.discard(key)
        return 1

    def lock(self, *args, **kwargs):
        return self.lock_obj


class FakeCelery:
    def __init__(self):
        self.sent = []

    def send_task(self, *args, **kwargs):
        self.sent.append((args, kwargs))


class FailingCelery:
    def send_task(self, *args, **kwargs):
        raise RuntimeError("synthetic publish failure")


class Phase13BatchB(unittest.TestCase):

    def test_13_5_finite_controls(self):
        values = [
            CELERY_EXTERNAL_GROUP_SYNC_LOCK_TIMEOUT,
            CELERY_GENERIC_BEAT_LOCK_TIMEOUT,
            CELERY_USER_FILE_PROCESSING_LOCK_TIMEOUT,
            CELERY_USER_FILE_PROCESSING_TASK_EXPIRES,
            CELERY_USER_FILE_PROJECT_SYNC_LOCK_TIMEOUT,
            CELERY_USER_FILE_PROJECT_SYNC_TASK_EXPIRES,
            CELERY_USER_FILE_DELETE_TASK_EXPIRES,
            USER_FILE_PROCESSING_MAX_QUEUE_DEPTH,
            USER_FILE_PROJECT_SYNC_MAX_QUEUE_DEPTH,
            USER_FILE_DELETE_MAX_QUEUE_DEPTH,
        ]

        for value in values:
            self.assertIsInstance(value, int)
            self.assertGreater(value, 0)

        self.assertLessEqual(USER_FILE_PROCESSING_MAX_QUEUE_DEPTH, 10000)
        self.assertLessEqual(USER_FILE_PROJECT_SYNC_MAX_QUEUE_DEPTH, 10000)
        self.assertLessEqual(USER_FILE_DELETE_MAX_QUEUE_DEPTH, 10000)

    def test_13_6_duplicate_work(self):
        redis = FakeRedis()
        celery = FakeCelery()

        first = uf.enqueue_user_file_project_sync_task(
            celery_app=celery,
            redis_client=redis,
            user_file_id=FID,
            tenant_id=TENANT,
        )

        second = uf.enqueue_user_file_project_sync_task(
            celery_app=celery,
            redis_client=redis,
            user_file_id=FID,
            tenant_id=TENANT,
        )

        self.assertTrue(first)
        self.assertFalse(second)
        self.assertEqual(len(celery.sent), 1)

        _, kwargs = celery.sent[0]
        self.assertEqual(
            kwargs["expires"],
            CELERY_USER_FILE_PROJECT_SYNC_TASK_EXPIRES,
        )

    def test_13_7_queue_backpressure(self):
        redis = FakeRedis()

        with (
            patch.object(uf, "get_redis_client", return_value=redis),
            patch.object(uf, "celery_get_broker_client", return_value=object()),
            patch.object(
                uf,
                "celery_get_queue_length",
                return_value=USER_FILE_PROCESSING_MAX_QUEUE_DEPTH + 1,
            ),
            patch.object(
                uf,
                "get_session_with_current_tenant",
            ) as database_path,
        ):
            result = uf.check_user_file_processing.run(
                tenant_id=TENANT
            )

        self.assertIsNone(result)
        database_path.assert_not_called()
        self.assertTrue(redis.lock_obj.released)

    def test_13_8_publish_failure_rollback(self):
        redis = FakeRedis()

        with self.assertRaisesRegex(
            RuntimeError,
            "synthetic publish failure",
        ):
            uf.enqueue_user_file_project_sync_task(
                celery_app=FailingCelery(),
                redis_client=redis,
                user_file_id=FID,
                tenant_id=TENANT,
            )

        self.assertEqual(len(redis.deleted), 1)
        self.assertEqual(redis.keys, set())


if __name__ == "__main__":
    unittest.main(verbosity=2)
