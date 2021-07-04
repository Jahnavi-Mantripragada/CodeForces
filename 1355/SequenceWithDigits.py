# https://codeforces.com/problemset/problem/1355/A
"""
a2 = a1 + mx1*mn1
a3 = a2 + mx2*mx2
"""


def max_min_digits(n):
    x = list(map(int, list(str(n))))
    return max(x) * min(x)


def a(n):
    if n == 1:
        return a1
    ai = a1
    n -= 1
    while n > 0:
        y = max_min_digits(ai)
        if y == 0:  # once minimum digit becomes 0, we don't are not adding anything new, so number remains same.
            break
        ai += y
        n -= 1
    return ai


if __name__ == "__main__":
    t = int(input())
    for case in range(t):
        a1, K = map(int, input().split())
        print(a(K))
