# Implement Prefix Radix Cache

A **radix tree** is a compressed trie that stores sequences by merging common prefixes. Instead of storing one value per edge or node like a standard trie, a radix tree compresses chains of single-child nodes into one segment.

You need to implement a **Prefix Radix Cache** for sequences of integers.

## Task

Implement a data structure that supports inserting integer sequences into a radix tree.

When two sequences share a common prefix, that prefix should be stored only once.

## Class Definition

```python
from typing import List

class RadixCache:
    def __init__(self):
        pass

    def insert(self, sequence: List[int]) -> None:
        pass
```

## Example

```python
tree = RadixCache()
tree.insert([10, 20])
tree.insert([1, 2, 3])
tree.insert([1, 2, 3, 4, 5, 6])
```

Resulting tree:

```text
Root
├── [1, 2, 3]
│   └── [4, 5, 6]
└── [10, 20]
```

## Behavior

When inserting a new sequence:

- If it shares no prefix with an existing branch, create a new child.
- If it fully matches an existing edge label, continue traversing downward.
- If it partially matches an existing edge label, split that edge into:
  - the shared prefix
  - the remaining suffix of the old edge
  - the remaining suffix of the new sequence

## Constraints

- `1 <= len(sequence) <= 10^5`
- Each element in `sequence` is an integer
- The total number of inserted integers across all operations does not exceed `2 * 10^5`

## Follow-up

Can you extend the data structure to support:

- `search(sequence) -> bool`
- `starts_with(prefix) -> bool`
