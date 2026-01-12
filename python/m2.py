# given an array parent where the 
# index -> node value
# parent[i] is the parent of node i
from dataclasses import dataclass, field
from typing import List

@dataclass
class Node:
    val : int
    children : List["Node"] = field(default_factory=list)
        
def buildTree(parent: List[int]):
    n = len(parent)
    nodes = [Node(i) for i in range(n)]
    root = None
    
    for idx,val in enumerate(parent):
        if val == -1:
            root = nodes[idx]
        else:
            nodes[val].children.append(nodes[idx])
    
    return root
        

print(buildTree([-1, 0, 0, 1, 1, 2]))
    