from __future__ import annotations

from collections import defaultdict
from typing import Iterable


Event = tuple[int, str, str]
BASE_RATE = 0.30


def calculate_naive_pay(events: Iterable[Event]) -> float:
    """
    Compute total base pay.

    Important detail:
    - For the pay interval [t, next_t), ACCEPTs at t should count and FULFILLs at t should not.
    - This matches the example where an order active at accept time and inactive starting at fulfill time.
    """
    grouped: dict[int, dict[str, int]] = defaultdict(lambda: {"ACCEPT": 0, "FULFILL": 0})

    for timestamp, order_id, action in events:
        if action not in ("ACCEPT", "FULFILL"):
            raise ValueError(f"Unknown action: {action}")
        grouped[timestamp][action] += 1

    times = sorted(grouped)
    active = 0
    prev_time: int | None = None
    total = 0.0

    for t in times:
        if prev_time is not None:
            total += (t - prev_time) * active * BASE_RATE

        # ACCEPT before FULFILL at the same timestamp.
        active += grouped[t]["ACCEPT"]
        active -= grouped[t]["FULFILL"]
        prev_time = t

    return round(total, 2)


if __name__ == "__main__":
    events = [
        (375, "A", "ACCEPT"),
        (378, "B", "ACCEPT"),
        (396, "A", "FULFILL"),
        (405, "B", "FULFILL"),
    ]
    print(calculate_naive_pay(events))  # 14.40
