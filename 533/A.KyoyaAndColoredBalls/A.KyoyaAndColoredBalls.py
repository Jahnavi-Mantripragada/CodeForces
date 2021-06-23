MOD = 1000000007


def C(n, k):
    global coefficients
    if k > n:
        return 0
    if k == 0 or k == n:
        return 1
    if coefficients[n][k] != -1:
        return coefficients[n][k]
    coefficients[n][k] = C(n - 1, k - 1) + C(n - 1, k)
    #print(n, k, coefficients[n][k])
    return coefficients[n][k] % MOD


def numberOfWays(n, K, k):
    ways = 1
    for i in range(K - 1, 0, -1):
        ways *= C(n-1, k[i] - 1)
        ways %= MOD
        n -= k[i]
        #print(ways, n)
    return ways


if __name__ == "__main__":
    coefficients = [[-1] * 1001 for i in range(1001)]
    k = int(input())
    n = 0
    L = []
    for i in range(k):
        L.append(int(input()))
        n += L[-1]
    print(numberOfWays(n, k, L))
