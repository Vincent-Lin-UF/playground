from __future__ import annotations

import time
from dataclasses import dataclass


class DistributedCache:
    """
    Simple in-memory stand-in for a distributed cache like Redis.
    """

    def __init__(self) -> None:
        self._store: dict[str, object] = {}

    def get(self, key: str) -> object | None:
        return self._store.get(key)

    def put(self, key: str, value: object) -> None:
        self._store[key] = value


@dataclass
class TokenBucket:
    tokens: float
    last_refill_time: float
    capacity: int
    refill_rate: float


DEFAULT_CAPACITY = 100
DEFAULT_REFILL_RATE = 10.0


def refill_token_bucket(bucket: TokenBucket, current_time: float) -> TokenBucket:
    elapsed = max(0.0, current_time - bucket.last_refill_time)
    new_tokens = elapsed * bucket.refill_rate
    bucket.tokens = min(bucket.capacity, bucket.tokens + new_tokens)
    bucket.last_refill_time = current_time
    return bucket


def allow_request(
    cache: DistributedCache,
    user_id: str,
    tokens_requested: int,
    *,
    current_time: float | None = None,
) -> bool:
    if current_time is None:
        current_time = time.time()

    bucket = cache.get(user_id)
    if bucket is None:
        bucket = TokenBucket(
            tokens=float(DEFAULT_CAPACITY),
            last_refill_time=current_time,
            capacity=DEFAULT_CAPACITY,
            refill_rate=DEFAULT_REFILL_RATE,
        )

    assert isinstance(bucket, TokenBucket)
    bucket = refill_token_bucket(bucket, current_time)

    if bucket.tokens >= tokens_requested:
        bucket.tokens -= tokens_requested
        cache.put(user_id, bucket)
        return True

    cache.put(user_id, bucket)
    return False


if __name__ == "__main__":
    cache = DistributedCache()
    for _ in range(100):
        allow_request(cache, "user_123", 1, current_time=0.0)
    print(allow_request(cache, "user_123", 1, current_time=0.0))  # False
    print(allow_request(cache, "user_123", 1, current_time=1.0))  # True
