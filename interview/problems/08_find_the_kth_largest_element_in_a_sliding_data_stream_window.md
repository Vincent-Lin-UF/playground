# Find the Kth Largest Element in a Sliding Data Stream Window

You are given a large stream of integers, an integer `k`, and a window size `window_size`.

Design a system that processes the stream one element at a time and returns the **kth largest element** within the current sliding time window.

Because the stream is large and memory is limited:

- use a **queue** to track which elements are currently inside the window
- use **buckets** to store frequencies of value ranges instead of storing every value in a fully sorted structure

## Task

Implement a data structure that supports:

- adding a new number from the stream
- removing expired numbers when the window exceeds `window_size`
- returning the kth largest element in the current window

## Class Definition

```python
class KthLargestInWindow:
    def __init__(self, k: int, window_size: int, bucket_size: int):
        pass

    def add(self, val: int) -> int:
        """
        Adds val to the stream, removes the oldest value if needed,
        and returns the kth largest element in the current window.
        If the window contains fewer than k elements, return -1.
        """
        pass
```

## Example

```python
k = 2
window_size = 3
stream = [4, 1, 7, 3, 9]

# Output: [-1, 1, 4, 3, 7]
```

### Explanation

- add `4` -> window = `[4]` -> fewer than 2 elements, return `-1`
- add `1` -> window = `[4, 1]` -> 2nd largest = `1`
- add `7` -> window = `[4, 1, 7]` -> 2nd largest = `4`
- add `3` -> window = `[1, 7, 3]` -> 2nd largest = `3`
- add `9` -> window = `[7, 3, 9]` -> 2nd largest = `7`

## Constraints

- `1 <= k <= window_size <= 10^5`
- `-10^9 <= val <= 10^9`
- The total number of stream updates can be very large
- Memory usage should be efficient enough for large streams

## Note

This version assumes a **count-based sliding window** of the last `window_size` elements.
