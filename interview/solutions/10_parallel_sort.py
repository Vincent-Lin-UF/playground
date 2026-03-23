from __future__ import annotations

import heapq
from concurrent.futures import ThreadPoolExecutor
from math import ceil
from typing import List


def parallel_sort(arr: List[int], num_threads: int) -> List[int]:
    """
    Sort by:
    1. splitting into chunks
    2. sorting each chunk in a separate thread
    3. merging the sorted chunks

    Note:
    In CPython, CPU-bound sorting does not get true parallel speedup from threads
    because of the GIL. This is still a faithful threaded design for the interview prompt.
    """
    if len(arr) <= 1:
        return arr[:]

    num_threads = max(1, min(num_threads, len(arr)))
    chunk_size = ceil(len(arr) / num_threads)

    chunks = [arr[i:i + chunk_size] for i in range(0, len(arr), chunk_size)]

    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        sorted_chunks = list(executor.map(sorted, chunks))

    return list(heapq.merge(*sorted_chunks))


if __name__ == "__main__":
    arr = [38, 27, 43, 3, 9, 82, 10]
    print(parallel_sort(arr, 4))  # [3, 9, 10, 27, 38, 43, 82]
