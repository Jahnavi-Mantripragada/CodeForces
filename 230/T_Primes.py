"""
If a number is perfect square of a prime number,
then it is a T-prime, cause then the factors:
1, sqrt(number), number
since sqrt(number) is a prime number. This number will have only 3 factors including itself.
"""
import math

prime = []


def Sieve():
    global prime
    n = 1000000
    prime = [True for i in range(n + 1)]
    p = 2
    while p * p <= n:
        if prime[p]:
            # looping through the multiples of p
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1
    prime[0] = False
    prime[1] = False


Sieve()
N = int(input())
L = list(map(int, input().split()))
for x in range(N):
    SQRT = math.sqrt(L[x])
    if SQRT == int(SQRT) and prime[int(SQRT)]:
        print("YES")
    else:
        print("NO")
