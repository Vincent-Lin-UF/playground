# 703 -> AAA

def ex(n : int) -> str:
    res = []
    while n > 0:
        n -= 1
        res.append(chr(ord('A') + (n % 26)))
        n //= 26
    return "".join(reversed(res))


print(ex(702))
print(ex(703))
print(ex(704))

    