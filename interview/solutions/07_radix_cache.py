from __future__ import annotations

from dataclasses import dataclass, field
from typing import Iterable


def _lcp_len(a: list[int], b: list[int]) -> int:
    i = 0
    while i < len(a) and i < len(b) and a[i] == b[i]:
        i += 1
    return i


@dataclass
class Node:
    terminal: bool = False
    children: dict[int, tuple[list[int], "Node"]] = field(default_factory=dict)


class RadixCache:
    """
    Compressed trie for integer sequences.
    """

    def __init__(self) -> None:
        self.root = Node()

    def insert(self, sequence: list[int]) -> None:
        if not sequence:
            self.root.terminal = True
            return

        node = self.root
        remaining = sequence[:]

        while remaining:
            first = remaining[0]
            edge = node.children.get(first)

            if edge is None:
                child = Node(terminal=True)
                node.children[first] = (remaining, child)
                return

            label, child = edge
            shared = _lcp_len(label, remaining)

            if shared == len(label):
                remaining = remaining[shared:]
                node = child
                if not remaining:
                    node.terminal = True
                    return
                continue

            # Split the edge on the common prefix.
            shared_prefix = label[:shared]
            old_suffix = label[shared:]
            new_suffix = remaining[shared:]

            middle = Node(terminal=False)

            # Existing branch becomes a child of the new middle node.
            middle.children[old_suffix[0]] = (old_suffix, child)

            # New sequence may end at the split point or continue below it.
            if not new_suffix:
                middle.terminal = True
            else:
                new_child = Node(terminal=True)
                middle.children[new_suffix[0]] = (new_suffix, new_child)

            node.children[first] = (shared_prefix, middle)
            return

        node.terminal = True

    def search(self, sequence: list[int]) -> bool:
        node = self.root
        remaining = sequence[:]

        if not remaining:
            return node.terminal

        while remaining:
            edge = node.children.get(remaining[0])
            if edge is None:
                return False

            label, child = edge
            if len(remaining) < len(label) or remaining[:len(label)] != label:
                return False

            remaining = remaining[len(label):]
            node = child

        return node.terminal

    def starts_with(self, prefix: list[int]) -> bool:
        node = self.root
        remaining = prefix[:]

        if not remaining:
            return True

        while remaining:
            edge = node.children.get(remaining[0])
            if edge is None:
                return False

            label, child = edge
            shared = _lcp_len(label, remaining)

            if shared == len(remaining):
                return True
            if shared < len(label):
                return False

            remaining = remaining[shared:]
            node = child

        return True


if __name__ == "__main__":
    tree = RadixCache()
    tree.insert([10, 20])
    tree.insert([1, 2, 3])
    tree.insert([1, 2, 3, 4, 5, 6])

    print(tree.search([1, 2, 3]))           # True
    print(tree.search([1, 2]))              # False
    print(tree.starts_with([1, 2, 3, 4]))   # True
