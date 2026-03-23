# Maximum Number of Distinct Elements After Operations

You are given an integer array `nums` and an integer `k`.

For each element `nums[i]`, you may perform the following operation at most once:

- replace `nums[i]` with any integer in the range `[nums[i] - k, nums[i] + k]`

Return the maximum possible number of distinct elements in the array after performing the operations optimally.

## Function Signature

```python
from typing import List

def max_distinct_elements(nums: List[int], k: int) -> int:
    pass
```

## Example 1

```python
nums = [1, 2, 2, 3, 3, 4]
k = 2

# Output: 6
```

One optimal assignment is `[-1, 0, 1, 2, 3, 4]`.

## Example 2

```python
nums = [4, 4, 4, 4]
k = 1

# Output: 3
```

Each `4` can be changed to any value in the range `[3, 5]`. An optimal result is `[3, 4, 5, 4]`.

## Constraints

- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^9`
- `0 <= k <= 10^9`

## Follow-up

Can you solve this in `O(n log n)` time or better?
