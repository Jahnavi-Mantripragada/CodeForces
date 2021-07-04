# https://codeforces.com/problemset/problem/479/C
def min_no_of_days(n, ab):
    ab.sort()
    days = []
    prev = ab[0]
    # print(ab)
    days.append(prev[-1])
    for i in range(1, n):
        curr = ab[i]
        if days[-1] <= curr[-1]:
            days.append(curr[-1])
        else:
            days.append(curr[0])
    return max(days)


if __name__ == "__main__":
    n = int(input())
    ab = []
    for i in range(n):
        ai, bi = map(int, input().split())
        ab.append((ai, bi))
    print(min_no_of_days(n, ab))
