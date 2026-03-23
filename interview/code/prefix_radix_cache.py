from typing import List

@dataclass
class Node:
    terminal: bool = False
    children = field(default_factory=dict)

class RadixCache:

    def __init__(self):
        self.root = Node()

    def insert(self, sequence: List[int]) -> None:
        if not sequence:
            self.root.terminal = True
            return

        node = self.root
        rem = sequence[:]

        while rem:
            first = rem[0]
            edge = node.children.get(first)

            if edge is None:
                child = Node(terminal=True)
                node.children[first] = (rem,child)
                return

            label, child = edge
            shared = _lcp_len(label,rem)

            
