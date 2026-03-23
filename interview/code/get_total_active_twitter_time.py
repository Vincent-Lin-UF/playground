from typing import List, Tuple, Dict

def get_total_active_time(records: List[Tuple(str,str,str,int)]) -> Dict[str,int]:
    roomTime = {}
    startTime = {}

    for op,tid,uid,time in records:
        if op == "create":
            roomTime[tid] = 0
            # has start time 
            startTime[(tid,uid)] = time
        elif op == "join":
            # has start time
            if tid not in roomTime:
                raise ValueError(f"The room has not been made yet: {tid}")
            startTime[(tid,uid)] = time
        elif op == "leave":
            # has end time and add to roomTime
            roomTime[tid] += time - startTime[(tid,uid)]
            del startTime[(tid,uid)]
        else:
            raise ValueError(f"Invalid value given here {op}")
    return roomTime
