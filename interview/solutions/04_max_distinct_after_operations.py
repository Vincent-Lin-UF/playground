from __future__ import annotations


def max_distinct_elements(nums: list[int], k: int) -> int:
    """
    Standard version:
    each nums[i] may be changed independently to any integer in [nums[i] - k, nums[i] + k].

    Greedy:
    sort nums, then assign each element the smallest feasible value that is strictly larger
    than the last assigned value.
    """
    nums.sort()
    last = -10**30
    answer = 0

    for x in nums:
        candidate = max(last + 1, x - k)
        if candidate <= x + k:
            answer += 1
            last = candidate

    return answer


if __name__ == "__main__":
    print(max_distinct_elements([1, 2, 2, 3, 3, 4], 2))  # 6
    print(max_distinct_elements([4, 4, 4, 4], 1))        # 3
