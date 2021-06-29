"""
https://codeforces.com/problemset/problem/1352/C
"""


def kthNotDivisibleByN(n, k):
    q, r = divmod(k, n - 1)
    # print(k, n-1, q, r)
    return n * q + (r if r != 0 else -1)


if __name__ == '__main__':
    T = int(input())
    for case in range(T):
        n, k = map(int, input().split())
        print(kthNotDivisibleByN(n, k))
