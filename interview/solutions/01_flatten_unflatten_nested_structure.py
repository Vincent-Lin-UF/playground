from __future__ import annotations

from collections.abc import Iterator
from typing import Any


def flatten(structure: Any) -> list[int]:
    """
    Return all integer leaves in traversal order.

    Traversal rules:
    - list / tuple: left to right
    - dict: insertion order of keys
    """
    out: list[int] = []

    def dfs(node: Any) -> None:
        if isinstance(node, int):
            out.append(node)
        elif isinstance(node, list) or isinstance(node, tuple):
            for child in node:
                dfs(child)
        elif isinstance(node, dict):
            for child in node.values():
                dfs(child)
        else:
            raise TypeError(f"Unsupported node type: {type(node)!r}")

    dfs(structure)
    return out


def unflatten(flat_list: list[int], structure: Any) -> Any:
    """
    Rebuild a structure with the same shape as `structure`,
    replacing integer leaves with values from `flat_list` in traversal order.
    """
    it = iter(flat_list)

    def rebuild(node: Any) -> Any:
        if isinstance(node, int):
            try:
                return next(it)
            except StopIteration as exc:
                raise ValueError("flat_list is shorter than the number of leaves") from exc
        if isinstance(node, list):
            return [rebuild(child) for child in node]
        if isinstance(node, tuple):
            return tuple(rebuild(child) for child in node)
        if isinstance(node, dict):
            return {key: rebuild(value) for key, value in node.items()}
        raise TypeError(f"Unsupported node type: {type(node)!r}")

    rebuilt = rebuild(structure)

    try:
        extra = next(it)
    except StopIteration:
        return rebuilt
    raise ValueError(f"flat_list is longer than the number of leaves, first extra value: {extra}")


if __name__ == "__main__":
    structure = {
        "a": [1, 2, 3],
        "b": {
            "c": [{"d": 4}],
            "e": 5,
        },
    }
    flat = flatten(structure)
    print(flat)  # [1, 2, 3, 4, 5]
    print(unflatten([6, 7, 8, 9, 0], structure))
