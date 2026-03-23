# Design a Distributed Token Bucket Rate Limiter

Design a distributed rate limiter using the **Token Bucket** algorithm with **lazy refill**.

A rate limiter controls how many requests a user can make over time. Each user has a token bucket:

- Each request consumes some number of tokens.
- Tokens are added back over time at a fixed refill rate.
- The bucket cannot hold more than its maximum capacity.
- Refill should happen lazily, only when a request is checked.

You are given two prebuilt components:

- `DistributedCache`: shared storage for persisting bucket state
- `TokenBucket`: stores the token bucket data for a user

Your task is to implement:

1. `refill_token_bucket`
2. `allow_request`

## Prebuilt Components

```python
from dataclasses import dataclass

class DistributedCache:
    def get(self, key: str) -> object | None:
        pass

    def put(self, key: str, value: object) -> None:
        pass

@dataclass
class TokenBucket:
    tokens: float
    last_refill_time: float
    capacity: int
    refill_rate: float
```

## Functions to Implement

```python
def refill_token_bucket(bucket: TokenBucket, current_time: float) -> TokenBucket:
    pass

def allow_request(cache: DistributedCache, user_id: str, tokens_requested: int) -> bool:
    pass
```

## Default Bucket Settings

Use the following default settings for every new user:

- `capacity = 100`
- `refill_rate = 10.0` tokens per second

## Behavior

### `refill_token_bucket(bucket, current_time)`

Update the bucket by adding tokens based on the elapsed time since `last_refill_time`.

- Tokens added = `(current_time - last_refill_time) * refill_rate`
- The number of tokens cannot exceed `capacity`
- Update `last_refill_time` to `current_time`

### `allow_request(cache, user_id, tokens_requested)`

Check whether the user can make a request requiring `tokens_requested` tokens.

- If the user has no existing bucket, create one full of tokens.
- Refill the bucket lazily before checking tokens.
- If enough tokens are available, subtract `tokens_requested`, save the updated bucket, and return `True`.
- Otherwise, save the updated bucket and return `False`.

## Follow-up

How would you make this implementation safe under concurrent requests from multiple servers?
