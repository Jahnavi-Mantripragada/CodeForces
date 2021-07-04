import math


def CanBeRepresented(n):
    if n < 2020:
        return False
    if n < 2021:
        return n == 2020
    if (n % 2021) == 0:
        return True
    y = (n % 2020)
    q = n // 2020
    x = q - y
    return 2020 * (x + y) == n - y and x >= 0 and y >= 0


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        n = int(input())
        if CanBeRepresented(n):
            print("YES")
        else:
            print("NO")
