from __future__ import annotations


def max_distinct_after_unique_adjustments(nums: list[int], k: int) -> int:
    """
    Assumption used here:
    each element must choose a DISTINCT signed adjustment d from the integer interval [-k, k],
    and the final value becomes nums[i] + d.

    This matches the example:
      nums = [0, 0, 0], k = 1
      choose d in {-1, 0, 1} => final values {-1, 0, 1}

    Greedy idea:
    - sort nums
    - process left to right
    - for each x, assign the smallest unused d such that x + d is strictly greater
      than the last distinct final value we formed
    - use a sparse disjoint-set structure to find the next unused integer >= lower_bound
      inside [-k, k]
    """
    nums.sort()

    parent: dict[int, int] = {}

    def find(x: int) -> int:
        if x not in parent:
            return x
        parent[x] = find(parent[x])
        return parent[x]

    def use_smallest_unused_at_least(lower_bound: int) -> int | None:
        lower_bound = max(lower_bound, -k)
        d = find(lower_bound)
        if d > k:
            return None
        parent[d] = find(d + 1)
        return d

    last_value = -10**30
    answer = 0

    for x in nums:
        d = use_smallest_unused_at_least(last_value + 1 - x)
        if d is None:
            continue
        y = x + d
        if y > last_value:
            last_value = y
            answer += 1

    return answer


if __name__ == "__main__":
    print(max_distinct_after_unique_adjustments([0, 0, 0], 1))  # 3
