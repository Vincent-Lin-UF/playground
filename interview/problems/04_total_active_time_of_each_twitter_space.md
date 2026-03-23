# Total Active Time of Each Twitter Space

You are given a list of records describing user activity in Twitter Spaces. Each record is a tuple:

`(operation, space_id, user_id, timestamp)`

where:

- `operation` is one of `"create"`, `"join"`, or `"leave"`
- `space_id` is the ID of a Twitter Space
- `user_id` is the ID of a user
- `timestamp` is a Unix timestamp in seconds

A `"create"` operation means the user creates the space and joins it immediately.

For each Twitter Space, compute its **total active time**, defined as the sum of the durations that all users spent in that space.

A user's active time in a space is `leave_time - join_time`.

Return a map from `space_id` to its total active time.

## Function Signature

```python
from typing import List, Tuple, Dict

def get_total_active_time(records: List[Tuple[str, str, str, int]]) -> Dict[str, int]:
    pass
```

## Example

```python
records = [
    ("create", "abc", "user_1", 1234567000),
    ("join",   "abc", "user_2", 1234567100),
    ("leave",  "abc", "user_2", 1234567300),
    ("create", "def", "user_2", 1234568000),
    ("leave",  "def", "user_2", 1234568500),
    ("leave",  "abc", "user_1", 1234569000),
]

# Output: {"abc": 2200, "def": 500}
```

## Explanation

For space `"abc"`:

- `user_1` stayed from `1234567000` to `1234569000` -> `2000`
- `user_2` stayed from `1234567100` to `1234567300` -> `200`

Total for `"abc"` = `2200`

For space `"def"`:

- `user_2` stayed from `1234568000` to `1234568500` -> `500`

Total for `"def"` = `500`

## Constraints

- `1 <= len(records) <= 2 * 10^5`
- `operation` is one of `"create"`, `"join"`, `"leave"`
- `space_id` and `user_id` are non-empty strings
- `0 <= timestamp <= 10^9`
- Every `"leave"` has a matching earlier `"create"` or `"join"` for the same `(space_id, user_id)`

## Follow-up

Design a data structure that supports generating the **top k spaces with the largest number of active users in real time**.
