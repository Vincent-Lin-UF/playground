# Calculate Dasher Base Pay

You are given a list of delivery events for a Dasher. Each event represents either accepting or fulfilling an order. Your task is to compute the Dasher's total **base pay**.

## Pay Rules

- The Dasher earns **0.30 USD per minute** for each active order.
- An order becomes **active** at the time of its `ACCEPT` event, inclusive.
- An order becomes **inactive** at the time of its `FULFILL` event, inclusive.
- If there are `k` active orders during a time interval, then the Dasher earns `k * 0.30` USD per minute.
- If multiple events happen at the same timestamp, process all `ACCEPT` events before all `FULFILL` events.

Return the total pay rounded to **2 decimal places**.

## Function Signature

```python
from typing import List, Tuple

def calculate_naive_pay(events: List[Tuple[int, str, str]]) -> float:
    pass
```

## Input Format

Each event is represented as:

- `time`: an integer timestamp in minutes
- `order_id`: a non-empty string identifying the order
- `action`: either `"ACCEPT"` or `"FULFILL"`

The input list may be unsorted.

## Output Format

Return a floating-point number representing the Dasher’s total base pay, rounded to 2 decimal places.

## Example

### Input

```python
events = [
    (375, "A", "ACCEPT"),
    (378, "B", "ACCEPT"),
    (396, "A", "FULFILL"),
    (405, "B", "FULFILL"),
]
```

### Explanation

- From minute `375` to `378`, 1 order is active  
  Pay = `3 * 0.30 = 0.90`
- From minute `378` to `396`, 2 orders are active  
  Pay = `18 * 2 * 0.30 = 10.80`
- From minute `396` to `405`, 1 order is active  
  Pay = `9 * 0.30 = 2.70`

Total = `0.90 + 10.80 + 2.70 = 14.40`

### Output

```python
14.40
```

## Constraints

- `1 <= len(events) <= 2 * 10^5`
- `0 <= time <= 10^9`
- `order_id` is a non-empty string
- `action` is either `"ACCEPT"` or `"FULFILL"`

## Notes

- You may assume each order has exactly one `ACCEPT` event and one `FULFILL` event.
- `ACCEPT` always happens at or before `FULFILL` for the same order.
