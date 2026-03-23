from __future__ import annotations

from dataclasses import dataclass


@dataclass
class _Bucket:
    tokens: float
    last_time: float
    capacity: int
    refill_rate: float


class RateLimiter:
    def __init__(self) -> None:
        self._limits: dict[str, tuple[int, float]] = {}
        self._buckets: dict[str, _Bucket] = {}

    def set_limit(self, user_id: str, capacity: int, refill_rate: float) -> None:
        self._limits[user_id] = (capacity, refill_rate)

        bucket = self._buckets.get(user_id)
        if bucket is None:
            self._buckets[user_id] = _Bucket(
                tokens=float(capacity),
                last_time=0.0,
                capacity=capacity,
                refill_rate=refill_rate,
            )
        else:
            bucket.capacity = capacity
            bucket.refill_rate = refill_rate
            bucket.tokens = min(bucket.tokens, float(capacity))

    def allow_request(self, user_id: str, tokens_requested: int, timestamp: float) -> bool:
        if user_id not in self._limits:
            return False

        capacity, refill_rate = self._limits[user_id]
        bucket = self._buckets.setdefault(
            user_id,
            _Bucket(
                tokens=float(capacity),
                last_time=timestamp,
                capacity=capacity,
                refill_rate=refill_rate,
            ),
        )

        elapsed = max(0.0, timestamp - bucket.last_time)
        bucket.tokens = min(bucket.capacity, bucket.tokens + elapsed * bucket.refill_rate)
        bucket.last_time = timestamp

        if bucket.tokens >= tokens_requested:
            bucket.tokens -= tokens_requested
            return True
        return False


if __name__ == "__main__":
    rl = RateLimiter()
    rl.set_limit("free", capacity=10, refill_rate=10)
    print(rl.allow_request("free", 5, 0.0))  # True
    print(rl.allow_request("free", 6, 0.0))  # False
    print(rl.allow_request("free", 1, 1.0))  # True
