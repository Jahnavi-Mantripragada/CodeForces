import math


def solve(n, p, k):
    total = p[0]
    answer = 0
    for i in range(1, n):
        val = p[i]
        if val / total > k / 100:
            answer += math.ceil(100 * val / k) - total
            total = math.ceil(100 * val / k)
        # print(val / total, k / 100, val, total, val / total > k / 100)
        total += val
    return answer


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        p = list(map(int, input().split()))
        print(solve(n, p, k))
