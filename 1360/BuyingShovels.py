# https://codeforces.com/problemset/problem/1360/D
from functools import reduce
import bisect

# from random import randint


def factors(n):
    if n in Factors:
        return Factors[n]
    Factors[n] = set(reduce(list.__add__, ([i, n // i] for i in range(1, int(n ** 0.5) + 1) if n % i == 0)))
    return Factors[n]


def minPackages(n, k):
    if n <= k:
        return 1
    L = sorted(factors(n))
    pos = bisect.bisect(L, k) - 1
    # print(k, L, L[pos])
    return n // (L[pos])


if __name__ == "__main__":
    t = int(input())
    Factors = dict()
    for case in range(t):
        n, k = map(int, input().split())
        # n, k = randint(1, 10 ** 9 + 1), randint(1, 10 ** 9 + 1)
        print(minPackages(n, k))
