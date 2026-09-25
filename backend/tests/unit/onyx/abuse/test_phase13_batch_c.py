import threading
import time
import unittest
from concurrent.futures import ThreadPoolExecutor
from unittest.mock import patch

from onyx.background.celery.tasks.user_file_processing import tasks as uf
from onyx.configs.constants import (
    CELERY_INDEXING_LOCK_TIMEOUT,
    CELERY_INDEXING_WATCHDOG_CONNECTOR_TIMEOUT,
    CELERY_INDEXING_WATCHDOG_SIGTERM_GRACE_SECONDS,
    CELERY_TASK_WAIT_FOR_FENCE_TIMEOUT,
    USER_FILE_PROCESSING_MAX_QUEUE_DEPTH,
)


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
        self.lock_obj = FakeLock()

    def lock(self, *args, **kwargs):
        return self.lock_obj


class Phase13BatchC(unittest.TestCase):

    def test_13_11_watchdog_and_timeout_bounds(self):
        self.assertGreater(
            CELERY_INDEXING_WATCHDOG_CONNECTOR_TIMEOUT,
            0,
        )
        self.assertGreater(
            CELERY_INDEXING_WATCHDOG_SIGTERM_GRACE_SECONDS,
            0,
        )
        self.assertGreater(
            CELERY_TASK_WAIT_FOR_FENCE_TIMEOUT,
            0,
        )

        # The lock survives slightly longer than the connector watchdog,
        # allowing hard termination to occur before lock expiry.
        self.assertGreater(
            CELERY_INDEXING_LOCK_TIMEOUT,
            CELERY_INDEXING_WATCHDOG_CONNECTOR_TIMEOUT,
        )

        self.assertLess(
            CELERY_INDEXING_WATCHDOG_SIGTERM_GRACE_SECONDS,
            CELERY_INDEXING_WATCHDOG_CONNECTOR_TIMEOUT,
        )

    def test_13_12_bounded_100_task_10_worker_harness(self):
        lock = threading.Lock()
        active = 0
        peak = 0

        def synthetic_work(item):
            nonlocal active, peak

            with lock:
                active += 1
                peak = max(peak, active)

            try:
                time.sleep(0.002)
                return item
            finally:
                with lock:
                    active -= 1

        with ThreadPoolExecutor(max_workers=10) as executor:
            results = list(
                executor.map(
                    synthetic_work,
                    range(100),
                )
            )

        self.assertEqual(results, list(range(100)))
        self.assertEqual(active, 0)
        self.assertLessEqual(peak, 10)
        self.assertGreater(peak, 0)

    def test_13_13_backpressure_is_observable(self):
        redis = FakeRedis()

        with (
            patch.object(
                uf,
                "get_redis_client",
                return_value=redis,
            ),
            patch.object(
                uf,
                "celery_get_broker_client",
                return_value=object(),
            ),
            patch.object(
                uf,
                "celery_get_queue_length",
                return_value=(
                    USER_FILE_PROCESSING_MAX_QUEUE_DEPTH + 1
                ),
            ),
            patch.object(
                uf,
                "get_session_with_current_tenant",
            ) as database_path,
            patch.object(
                uf.task_logger,
                "warning",
            ) as warning,
        ):
            result = uf.check_user_file_processing.run(
                tenant_id="phase13-synthetic"
            )

        self.assertIsNone(result)
        database_path.assert_not_called()
        self.assertTrue(warning.called)

        warning_text = " ".join(
            str(value)
            for value in warning.call_args[0]
        )

        self.assertIn(
            "Queue depth",
            warning_text,
        )
        self.assertIn(
            "skipping enqueue",
            warning_text,
        )

        self.assertTrue(redis.lock_obj.released)


if __name__ == "__main__":
    unittest.main(verbosity=2)
