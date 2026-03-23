# Find All Faulty GPU Nodes

You are given `n` GPU nodes labeled from `0` to `n - 1`. Some of the nodes are faulty, and the rest are good.

You do not know which nodes are faulty directly. Instead, you are given access to a helper function:

```python
test(S: Set[int]) -> bool
```

where `S` is a set of node indices.

The function behaves as follows:

- returns `True` if **every** node in `S` is good
- returns `False` if **at least one** node in `S` is faulty

Your task is to identify **all faulty nodes**.

## Rules

- You may only call `test(S)` on a set with at least 2 nodes.
- You are not allowed to test a single node by itself.
- It is guaranteed that there are always at least 2 good nodes in the cluster.

## Function Signature

```python
from typing import Callable, Set

def find_faulty_nodes(n: int, test: Callable[[Set[int]], bool]) -> Set[int]:
    pass
```

## Example

```python
n = 8
faulty = {2, 5}

# Hidden test(S) returns True iff S contains no faulty nodes

# Output: {2, 5}
```

## Constraints

- `2 <= n <= 10^5`
- `test(S)` may only be called when `len(S) >= 2`
- There are always at least 2 good nodes
- Node labels are integers in the range `[0, n - 1]`

## Follow-up

Can you design an algorithm that minimizes the number of calls to `test`?
