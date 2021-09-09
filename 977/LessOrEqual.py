def countNumber(n, a, key):
    count = 0
    for i in range(n):
        count += (a[i] <= key)
    return count


def getX(n, k, a):
    low = 1
    high = 10 ** 9
    while low <= high:
        mid = low + (high - low) // 2
        s = countNumber(n, a, mid)
        if s == k:
            return mid
        if s > k:
            high = mid - 1
        else:
            low = mid + 1
    return -1


if __name__ == "__main__":
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(getX(n, k, a))
