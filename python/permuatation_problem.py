from itertools import permutations


def permuatation_problem():
    n = 9
    res = 0
    for a,b,c,d,e,f,g,h,i in permutations(range(1,10),9):
        if a + 13 * b / c + d + 12 * e - f - 11 + g * h / i - 10 == 66.0:
            print(f"{a} + 13 * {b} / {c} + {d} + 12 * {e} - {f} - 11 + {g} * {h} / {i} - 10")
            res += 1 
    print("Amount of solutions:", res)
    return

