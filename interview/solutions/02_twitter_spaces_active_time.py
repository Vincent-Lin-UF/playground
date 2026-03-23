from __future__ import annotations

from collections import defaultdict
from typing import Iterable


Record = tuple[str, str, str, int]


def calculate_space_active_time(records: Iterable[Record]) -> dict[str, int]:
    """
    Return total active time per Twitter Space.

    Assumptions:
    - "create" means the user joins immediately.
    - Every leave has a matching earlier create/join for the same (space, user).
    - If records are unsorted, they are processed in timestamp order.
    """
    records = sorted(records, key=lambda x: x[3])

    joined_at: dict[tuple[str, str], int] = {}
    totals: dict[str, int] = defaultdict(int)

    for operation, space_id, user_id, timestamp in records:
        key = (space_id, user_id)

        if operation == "create" or operation == "join":
            joined_at[key] = timestamp
        elif operation == "leave":
            start = joined_at.pop(key)
            totals[space_id] += timestamp - start
        else:
            raise ValueError(f"Unknown operation: {operation}")

    return dict(totals)


if __name__ == "__main__":
    records = [
        ("create", "abc", "user_1", 1234567000),
        ("join",   "abc", "user_2", 1234567100),
        ("leave",  "abc", "user_2", 1234567300),
        ("create", "def", "user_2", 1234568000),
        ("leave",  "def", "user_2", 1234568500),
        ("leave",  "abc", "user_1", 1234569000),
    ]
    print(calculate_space_active_time(records))  # {'abc': 2200, 'def': 500}
