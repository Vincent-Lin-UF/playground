# Flatten and Rebuild Nested Integer Structure

You are given a nested Python-style data structure that may contain:

- `list`
- `tuple`
- `dict`

All leaf values are guaranteed to be integers.

Your task is to implement two functions:

1. **Flatten** the nested structure into a single list of integers in traversal order.
2. **Rebuild** a new nested structure using a flat list of integers and a template structure.

For dictionaries, preserve the original key iteration order.

## Part 1: Flatten Nested Structure

Given a nested structure, return a flat list containing all integer values in order.

```python
from typing import List, Any

def flatten(structure: Any) -> List[int]:
    pass
```

### Example

```python
structure = {
    'a': [1, 2, 3],
    'b': {
        'c': [{'d': 4}],
        'e': 5,
    },
}

# Output: [1, 2, 3, 4, 5]
```

## Part 2: Rebuild Nested Structure

Given:

- `flat_list`: a list of integers
- `structure`: a nested structure used as a template

Return a new object with the **same shape and container types** as `structure`, but replace each integer leaf with values from `flat_list` in order.

```python
from typing import List, Any

def unflatten(flat_list: List[int], structure: Any) -> Any:
    pass
```

### Example

```python
flat_list = [6, 7, 8, 9, 0]
structure = {
    'a': [1, 2, 3],
    'b': {
        'c': [{'d': 4}],
        'e': 5,
    },
}

# Output:
# {
#     'a': [6, 7, 8],
#     'b': {
#         'c': [{'d': 9}],
#         'e': 0,
#     },
# }
```

## Constraints

- The structure contains only `list`, `tuple`, `dict`, and `int`
- Every leaf node is an `int`
- `1 <= number of integer leaves <= 10^5`
- Dictionary key order must be preserved
- For `unflatten`, `len(flat_list)` equals the number of integer leaves in `structure`

## Follow-up

Can you solve both parts using recursion?
