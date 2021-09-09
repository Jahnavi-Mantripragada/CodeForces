"""
Two operations:
1. Swap i, j -> Cost: |i - j|
2. Flip at index -> Cost: 1

On observation if |i - j| > 2 --> we can choose to flip them each at the cost of 2.
if |i - j| == 2 --> anything is fine.
if |i- j| < 2 --> we can chose swapping --> that means adjacent ones swap.
"""


def makeBFromA(n: int, a: str, b: str):
    cost = 0
    a = list(a)
    for i in range(1, n + 1):
        if i != n and a[i] != b[i] and a[i - 1] != b[i - 1] and a[i] != a[i - 1]:
            a[i], a[i - 1] = a[i - 1], a[i]
            cost += 1
        elif a[i - 1] != b[i - 1]:
            cost += 1
            a[i - 1] = b[i - 1]
    return cost


if __name__ == "__main__":
    n = int(input())
    a = input()
    b = input()
    print(makeBFromA(n, a, b))
