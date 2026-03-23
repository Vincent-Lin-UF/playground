# Maximum Number of Distinct Elements After Unique Adjustments

You are given an integer array `nums` and an integer `k`.

For each element `nums[i]`, you must choose a **distinct** integer adjustment value from the range `[0, k]`, and then either:

- add that value to `nums[i]`, or
- subtract that value from `nums[i]`

Each adjustment value in `[0, k]` can be used **at most once** across the entire array.

Return the maximum possible number of distinct integers in the final array.

## Function Signature

```python
from typing import List

def max_distinct_after_unique_adjustments(nums: List[int], k: int) -> int:
    pass
```

## Example

```python
nums = [0, 0, 0]
k = 1

# Output: 3
# One valid result is [-1, 0, 1]
```

## Another Example

```python
nums = [1, 1, 1, 1]
k = 2

# Output: 4
# One possible assignment is [-1, 0, 1, 3]
```

## Constraints

- `1 <= nums.length <= 10^5`
- `0 <= nums[i] <= 10^9`
- `0 <= k <= 10^9`

## Note

If `nums.length > k + 1`, the original wording is ambiguous because there are not enough distinct offsets in `[0, k]` to assign one to every element. A full interview version should clarify whether every element must consume a unique offset or whether some elements may remain unchanged without consuming a new offset.
