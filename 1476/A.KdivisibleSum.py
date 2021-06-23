import math


def solve(n, k):
    if n % k == 0:
        return 1
    if k > n:
        return int(math.ceil(k / n))

    return 2


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        print(solve(n, k))
