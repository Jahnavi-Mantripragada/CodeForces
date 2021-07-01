"""
https://codeforces.com/problemset/problem/279/B
"""

if __name__ == "__main__":
    n, t = map(int, input().split())
    a = list(map(int, input().split()))
    maximum_books = 0
    acquire = 0
    release = 0
    time = 0
    while acquire < n:
        time += a[acquire]
        acquire += 1
        while release <= acquire and time > t:
            time -= a[release]
            release += 1
        maximum_books = max(maximum_books, acquire-release)
    print(maximum_books)
