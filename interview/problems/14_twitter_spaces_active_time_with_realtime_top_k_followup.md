# Twitter Spaces Active Time with Realtime Top-K Follow-up

You are given a list of logs describing user activity in Twitter Spaces. Each log entry represents one of three operations:

- `"create"`: a user creates a new Space and joins it immediately
- `"join"`: a user joins an existing Space
- `"leave"`: a user leaves a Space

Each log is represented as:

```python
[operation, space_id, user_id, timestamp]
```

Your task is to compute the **total active time** for every Space.

The active time contributed by a user is `leave_time - join_time`.

The total active time of a Space is the sum of all users' active times in that Space.

Return a mapping from `space_id` to its total active time.

## Function Signature

```python
from typing import List, Dict, Union

def calculate_space_active_time(logs: List[List[Union[str, int]]]) -> Dict[str, int]:
    pass
```

## Example

```python
logs = [
    ["create", "abc", "user_1", 1234567000],
    ["join",   "abc", "user_2", 1234567100],
    ["leave",  "abc", "user_2", 1234567300],
    ["create", "def", "user_2", 1234568000],
    ["leave",  "def", "user_2", 1234568500],
    ["leave",  "abc", "user_1", 1234569000],
]

# Output: {"abc": 2200, "def": 500}
```

## Follow-up

Design a real-time system that supports:

- processing `create`, `join`, and `leave` events
- tracking the current number of active users in each Space
- returning the top `k` Spaces with the largest number of active users at any moment

### Example API

```python
class TwitterSpaces:
    def process(self, operation: str, space_id: str, user_id: str, timestamp: int) -> None:
        pass

    def top_k(self, k: int) -> List[str]:
        pass
```
