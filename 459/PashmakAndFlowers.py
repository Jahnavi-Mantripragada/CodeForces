"""
https://codeforces.com/problemset/problem/459/B
"""

# A and B -> #OfA * #OfB

if __name__ == "__main__":
    n = int(input())
    b = list(map(int, input().split()))
    m1, m2 = max(b), min(b)
    max_diff = m1 - m2
    if m1 != m2:
        # nC1 * mC1
        print(max_diff, b.count(m1)*b.count(m2))
    else:
        # nC2
        n = b.count(m1)
        print(max_diff, (n*(n-1))//2)

