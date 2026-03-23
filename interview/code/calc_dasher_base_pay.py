from typing import List, Tuple

def calculate_naive_pay(events: List[Tuple[int,str,str]]) -> float:
    # O(N) space and time 
    mp = {}
    res = 0.0

    for time,oid,action in events:
        if action == "ACCEPT":
            mp[oid] = time 
        else:
            res += (time - mp[oid]) * 0.3
            del mp[oid]
    return round(res,2)

if __name__ == "__main__":
    events = [
    (375, "A", "ACCEPT"),
    (378, "B", "ACCEPT"),
    (396, "A", "FULFILL"),
    (405, "B", "FULFILL"),
    ]

    print(calculate_naive_pay(events))


