from __future__ import annotations

from typing import Callable, Set


def find_faulty_nodes(n: int, test: Callable[[Set[int]], bool]) -> Set[int]:
    """
    Reference implementation focused on correctness.

    Strategy:
    1. Find one known-good pair by testing pairs until one returns True.
       In the worst case with exactly two good nodes, any deterministic method
       may need to discover that exact pair.
    2. Once one good reference node g is known, test {g, x} for every other x.
       Since g is good:
         - True  => x is good
         - False => x is faulty

    Time complexity in number of test calls:
    - Worst case O(n^2) to find a good pair, then O(n) to classify everyone else.
    """
    if n < 2:
        raise ValueError("Need at least 2 nodes")

    good_a = good_b = None
    for i in range(n):
        for j in range(i + 1, n):
            if test({i, j}):
                good_a, good_b = i, j
                break
        if good_a is not None:
            break

    if good_a is None:
        # Guaranteed impossible under the stated assumption of at least 2 good nodes.
        raise RuntimeError("Could not find a good pair despite the problem guarantee")

    faulty: set[int] = set()
    good_reference = good_a

    for node in range(n):
        if node == good_a or node == good_b:
            continue
        if not test({good_reference, node}):
            faulty.add(node)

    return faulty


if __name__ == "__main__":
    def make_test(faulty_nodes):
        def test_fn(S):
            assert len(S) >= 2
            return len(S & faulty_nodes) == 0
        return test_fn

    print(find_faulty_nodes(8, make_test({2, 5})))  # {2, 5}
