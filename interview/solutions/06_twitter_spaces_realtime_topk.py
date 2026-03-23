from __future__ import annotations

import heapq
from collections import defaultdict


class TwitterSpacesTopK:
    """
    Real-time tracker for spaces with the largest number of currently active users.

    API:
    - process(operation, space_id, user_id, timestamp)
    - top_k(k) -> list[str]

    Uses:
    - active_users[space_id] = set of currently active users in that space
    - active_count[space_id] = number of active users
    - max-heap with lazy cleanup for top-k queries
    """

    def __init__(self) -> None:
        self.active_users: dict[str, set[str]] = defaultdict(set)
        self.active_count: dict[str, int] = defaultdict(int)
        self._version: dict[str, int] = defaultdict(int)
        self._heap: list[tuple[int, str, int]] = []

    def _push_snapshot(self, space_id: str) -> None:
        self._version[space_id] += 1
        heapq.heappush(
            self._heap,
            (-self.active_count[space_id], space_id, self._version[space_id]),
        )

    def process(self, operation: str, space_id: str, user_id: str, timestamp: int) -> None:
        del timestamp  # not needed for the active-count query itself

        users = self.active_users[space_id]

        if operation == "create" or operation == "join":
            if user_id not in users:
                users.add(user_id)
                self.active_count[space_id] += 1
                self._push_snapshot(space_id)
        elif operation == "leave":
            if user_id in users:
                users.remove(user_id)
                self.active_count[space_id] -= 1
                self._push_snapshot(space_id)
        else:
            raise ValueError(f"Unknown operation: {operation}")

    def top_k(self, k: int) -> list[str]:
        """
        Return up to k space IDs with the largest current active-user counts.
        Ties are broken by space_id because of the heap tuple ordering.
        """
        taken: list[tuple[int, str, int]] = []
        answer: list[str] = []
        seen: set[str] = set()

        while self._heap and len(answer) < k:
            neg_count, space_id, version = heapq.heappop(self._heap)
            if version != self._version[space_id]:
                continue
            if -neg_count != self.active_count[space_id]:
                continue
            if self.active_count[space_id] == 0:
                continue
            if space_id in seen:
                continue

            seen.add(space_id)
            answer.append(space_id)
            taken.append((neg_count, space_id, version))

        for item in taken:
            heapq.heappush(self._heap, item)

        return answer


if __name__ == "__main__":
    tracker = TwitterSpacesTopK()
    tracker.process("create", "abc", "u1", 1)
    tracker.process("join", "abc", "u2", 2)
    tracker.process("create", "def", "u3", 3)
    print(tracker.top_k(2))  # ['abc', 'def']
