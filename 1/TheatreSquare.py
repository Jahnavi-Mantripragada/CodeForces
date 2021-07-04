def theatreSquare(n, m, a):
    x = (n // a + (1 if n % a != 0 else 0)) * a
    y = (m // a + (1 if m % a != 0 else 0)) * a
    return (x * y) // (a * a)


if __name__ == "__main__":
    n, m, a = map(int, input().split())
    print(theatreSquare(n, m, a))
