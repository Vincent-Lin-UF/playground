from typing import List

def max_distinct_elements(nums: List[int], k: int) -> int:
    nums.sort()
    last = -10**30
    res = 0

    for num in nums:
        cand = max(last+1,num-k)
        if cand <= num+k:
            res += 1
            last = cand
    return res
