from typing import List
import heapq
from concurrent.futures import ThreadPoolExecutor
from math import ceil

def parallel_sort(arr: List[int], num_threads: int) -> List[int]:
    if len(arr) <= 1: return arr
    
    num_threads = max(1,min(num_threads,len(arr)))
    chunk_size = ceil(len(arr)/num_threads)
    
    chunks = [arr[i:i+chunk_size] for i in range(0,len(arr),chunk_size)]

    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        sorted_chunks = list(exeuctor.map(sorted,chunks))

    return list(heapq.merge(*sorted_chunks))

