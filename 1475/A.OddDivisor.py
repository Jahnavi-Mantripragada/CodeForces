def hasOddDivisor(n):
    return n & (n - 1) != 0


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        n = int(input())
        if hasOddDivisor(n):
            print("YES")
        else:
            print("NO")
