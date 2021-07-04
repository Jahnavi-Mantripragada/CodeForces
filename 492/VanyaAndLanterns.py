def VanyaAndLanterns(n, a, l):
    a.sort()
    count = 0
    prev = 0
    div = 1
    if a[0] == 0:
        div = 2
    for i in range(n):
        count = max(count, (a[i] - prev) / div)
        prev = a[i]
        div = 2
    if a[-1] != l:
        count = max(count, l - a[-1])
    return count


if __name__ == "__main__":
    n, l = map(int, input().split())
    a = list(map(int, input().split()))
    print(VanyaAndLanterns(n, a, l))