"""
https://codeforces.com/problemset/problem/1352/B
"""


# Odd + Odd = Even
# Even + Odd = Odd
# Even + Even = Even
def sameParitySummands(n, k):
    # if n is odd, we need k also to be odd
    # as for odd sum, we need odd number of odd numbers.
    a = []
    if n % 2 != 0:
        if k % 2 == 0 or n < k:
            return False, []
        a = [1] * k
        a[-1] += (n - k)
    elif n % 2 == 0:
        if k % 2 != 0:  # We need to choose only Even numbers.
            if n < 2 * k:
                return False, []
            a = [2] * k
            a[-1] += (n - 2 * k)
        else:  # k % 2 == 0
            if n < k:
                return False, []
            a = [1] * k
            a[-1] += (n - k)
    return True, a


if __name__ == "__main__":
    t = int(input())
    for case in range(t):
        n, k = map(int, input().split())
        possible, a = sameParitySummands(n, k)
        if possible:
            print("YES")
            print(" ".join(map(str, a)))
        else:
            print("NO")
