from typing import List,Any

def flatten(structure: Any) -> List[int]:
    res = []

    def dfs(node: Any):
        if isinstance(node,int):
            res.append(node)
        elif isinstance(node,list) or isinstance(node,tuple):
            for child in node:
                dfs(child)
        elif isinstance(node,dict):
            for child in node.values():
                dfs(child)
        else:
            raise TypeError(f"Unsupported type: {type(node)}")
    
    dfs(structure)
    return res

def unflatten(flat_list: List[int], structure: Any) -> Any:
    it = iter(flat_list)

    def rebuild(node: Any) -> Any:
        if isinstance(node,int):
            try:
                return next(it)
            except StopIteration as exc:
                raise ValueError("flat_list is shorter than # of leaves") from exc 
        elif isinstance(node,list):
            return [rebuild(child) for child in node]
        elif isinstance(node,tuple):
            return tuple(rebuild(child) for child in node)
        elif isinstance(node,dict):
            return {key: rebuild(val) for key,val in node.items()}
        else:
            raise TypeError(f"Unsupported type: {type(node)}")

    rebuilt = rebuild(structure)
    try:
        extra = next(it)
    except StopIteration:
        return rebuilt
    raise ValueError(f"flat_list is longer than # of leaves, first extra is {extra}")
                


