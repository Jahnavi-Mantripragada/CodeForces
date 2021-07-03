def min_prefix_len(n, a):
    sort_break = -1
    for i in range(n - 2, -1, -1):
        if a[i] < a[i + 1]:  # 2 5
            sort_break = i
            break
    for i in range(sort_break, 0, -1):
        if a[i] < a[i-1]:
            return i
    return 0


if __name__ == "__main__":
    t = int(input())
    for case in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        print(min_prefix_len(n, a))
