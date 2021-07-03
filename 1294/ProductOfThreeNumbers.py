# https://codeforces.com/problemset/problem/1294/C
from functools import reduce
import copy


def factors(n):
    if n in Factors:
        return Factors[n]
    Factors[n] = set(reduce(list.__add__, ([i, n // i] for i in range(1, int(n ** 0.5) + 1) if n % i == 0)))
    return Factors[n]


def productOfThreeNumbers(n):
    factors_of_n = copy.deepcopy(factors(n))
    factors_of_n.discard(n)
    factors_of_n.discard(1)
    F = dict()
    for i in factors_of_n:
        f = copy.deepcopy(factors(i))
        f.discard(i)
        f.discard(1)
        F[i] = f
    if len(F) == 0:
        return False, 0, 0, 0
    for x in F:
        X, Y = x, n // x
        if X not in F[Y] and len(F[Y]) > 1:
            a = X
            while F[Y]:
                b = F[Y].pop()
                if Y // b in F[Y]:
                    c = Y // b
                    F[Y].discard(c)
                    return True, a, b, c
        if X in F[Y] and len(F[Y]) > 2:
            F[Y].discard(X)
            a = X
            while F[Y]:
                b = F[Y].pop()
                if Y // b in F[Y]:
                    c = Y // b
                    F[Y].discard(c)
                    return True, a, b, c
    return False, 0, 0, 0


if __name__ == "__main__":
    t = int(input())
    Factors = dict()
    for case in range(t):
        n = int(input())
        possible, a, b, c = productOfThreeNumbers(n)
        if possible:
            print("YES")
            print(a, b, c)
        else:
            print("NO")
