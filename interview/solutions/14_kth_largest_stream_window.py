from __future__ import annotations

from collections import Counter, defaultdict, deque


class KthLargestInWindow:
    """
    Exact sliding-window kth-largest query using:
    - a queue for the window
    - bucket counts for coarse aggregation
    - exact counts inside each bucket for final resolution

    This keeps insertion/removal simple while avoiding a fully sorted structure.
    """

    def __init__(self, k: int, window_size: int, bucket_size: int):
        if k <= 0 or window_size <= 0 or bucket_size <= 0:
            raise ValueError("k, window_size, and bucket_size must be positive")

        self.k = k
        self.window_size = window_size
        self.bucket_size = bucket_size

        self.window: deque[int] = deque()
        self.bucket_counts: dict[int, int] = defaultdict(int)
        self.value_counts: dict[int, Counter[int]] = defaultdict(Counter)

    def _bucket_id(self, val: int) -> int:
        return val // self.bucket_size

    def _add_value(self, val: int) -> None:
        b = self._bucket_id(val)
        self.bucket_counts[b] += 1
        self.value_counts[b][val] += 1

    def _remove_value(self, val: int) -> None:
        b = self._bucket_id(val)
        self.bucket_counts[b] -= 1
        if self.bucket_counts[b] == 0:
            del self.bucket_counts[b]

        self.value_counts[b][val] -= 1
        if self.value_counts[b][val] == 0:
            del self.value_counts[b][val]
        if not self.value_counts[b]:
            del self.value_counts[b]

    def add(self, val: int) -> int:
        self.window.append(val)
        self._add_value(val)

        if len(self.window) > self.window_size:
            old = self.window.popleft()
            self._remove_value(old)

        return self.query()

    def query(self) -> int:
        if len(self.window) < self.k:
            return -1

        remaining = self.k

        for bucket_id in sorted(self.bucket_counts.keys(), reverse=True):
            count = self.bucket_counts[bucket_id]
            if remaining > count:
                remaining -= count
                continue

            # The kth largest lies in this bucket.
            for value in sorted(self.value_counts[bucket_id].keys(), reverse=True):
                freq = self.value_counts[bucket_id][value]
                if remaining > freq:
                    remaining -= freq
                else:
                    return value

        raise RuntimeError("Internal state error while answering kth-largest query")


if __name__ == "__main__":
    stream = KthLargestInWindow(k=2, window_size=3, bucket_size=10)
    values = [4, 1, 7, 3, 9]
    print([stream.add(v) for v in values])  # [-1, 1, 4, 3, 7]
