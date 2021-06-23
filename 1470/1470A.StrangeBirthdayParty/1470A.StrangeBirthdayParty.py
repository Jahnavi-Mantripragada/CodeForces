# Note that C is sorted
# We sort K in reverse order
# If we give presents to first m in sorted K, we will be left with smaller K values
# which in turn means that we are left with smaller c values.
def minAmount(n, m, C, K):
    K.sort(reverse=True)
    Amount = 0
    j = 0
    for i in range(n):
        k = K[i]-1
        if j < m and C[j] < C[k]:
            Amount += C[j]
            j += 1
        else:
            Amount += C[k]
    return Amount


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        K = list(map(int, input().split()))
        C = list(map(int, input().split()))
        print(minAmount(n, m, C, K))
