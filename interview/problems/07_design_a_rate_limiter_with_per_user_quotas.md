# Design a Rate Limiter with Per-User Quotas

Design a rate limiter that supports **different token limits for different users**.

Unlike a standard rate limiter where every user shares the same quota, this system must allow each user to have a custom refill policy.

For example:

- a power user may receive `10000` tokens per second
- a regular user may receive `100` tokens per second
- a free user may receive `10` tokens per second

Your task is to design a system that can enforce these per-user limits efficiently.

## Implement the `RateLimiter` class

```python
class RateLimiter:
    def set_limit(self, user_id: str, capacity: int, refill_rate: float) -> None:
        pass

    def allow_request(self, user_id: str, tokens_requested: int, timestamp: float) -> bool:
        pass
```

## Behavior

### `set_limit(user_id, capacity, refill_rate)`

Assign or update the token bucket policy for a user:

- `capacity`: maximum number of tokens the user can store
- `refill_rate`: number of tokens added per second

Each user has an independent token bucket.

### `allow_request(user_id, tokens_requested, timestamp)`

Return `True` if the request can be allowed, otherwise return `False`.

For a request to be allowed:

- the user's bucket must be lazily refilled based on elapsed time
- the bucket must contain at least `tokens_requested` tokens
- if allowed, subtract `tokens_requested` from the bucket

If the user has no configured limit, treat the request as denied.

## Example

```python
rl = RateLimiter()

rl.set_limit("justin", capacity=10000, refill_rate=10000)
rl.set_limit("regular", capacity=100, refill_rate=100)
rl.set_limit("free", capacity=10, refill_rate=10)

# At time 0.0, "free" starts with 10 tokens
assert rl.allow_request("free", 5, 0.0) is True
assert rl.allow_request("free", 6, 0.0) is False
assert rl.allow_request("free", 1, 1.0) is True
```

## Constraints

- `1 <= capacity <= 10^9`
- `0 <= refill_rate <= 10^9`
- `1 <= tokens_requested <= 10^9`
- `0 <= timestamp <= 10^12`
- Up to `10^5` total operations
