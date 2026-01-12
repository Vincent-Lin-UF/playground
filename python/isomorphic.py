# s = egg -> t = add
# s = foo -> t = bar

def isIso(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    s_first = {}
    t_first = {}
    
    for i, (cs,ct) in enumerate(zip(s,t)):
        if cs not in s_first:
            s_first[cs] = i
        if ct not in t_first:
            t_first[ct] = i
        
        if s_first[cs] != t_first[ct]:
            return False
    
    return True

print("Starting test cases")
assert isIso("egg","add")
assert isIso("paper","title")
assert not isIso("foo","bar")
assert not isIso("ab","aa")
print("End of test cases")
