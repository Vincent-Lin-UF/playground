# Sort an Array Using Multiple Threads

You are given an integer array `arr` and an integer `num_threads`.

Write a function that sorts the array in ascending order using multiple threads.

The goal is to divide the work across `num_threads` threads, sort parts of the array in parallel, and then merge the results into one fully sorted array.

## Function Signature

```python
from typing import List

def parallel_sort(arr: List[int], num_threads: int) -> List[int]:
    pass
```

## Example

```python
arr = [38, 27, 43, 3, 9, 82, 10]
num_threads = 4

# Output: [3, 9, 10, 27, 38, 43, 82]
```

## Constraints

- `0 <= len(arr) <= 10^5`
- `-10^9 <= arr[i] <= 10^9`
- `1 <= num_threads <= 32`

## Notes

- You may divide the array into chunks, sort each chunk in parallel, and then merge the sorted chunks.
- If `num_threads > len(arr)`, some threads may remain unused.
- The returned array must contain exactly the same elements as the input.
