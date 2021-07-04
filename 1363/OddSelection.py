"""
http://codeforces.com/problemset/problem/1363/A
"""


# Even + Odd = Odd
def oddSelection(n, x, a):
    if n == x:
        return sum(a) % 2 != 0
    AllOdd = True
    AllEven = True
    NumberOfEven = 0
    NumberOfOdd = 0
    for i in range(n):
        AllOdd &= (a[i] % 2 != 0)
        AllEven &= (a[i] % 2 == 0)
        if a[i] % 2 != 0:
            NumberOfOdd += 1
        else:
            NumberOfEven += 1
    if AllEven:
        return False
    # We need odd number of odd numbers.
    NumberOfOdd -= (1 if NumberOfOdd % 2 == 0 else 0)
    if x % 2 == 0 and AllOdd:
        return False
    return NumberOfOdd + NumberOfEven >= x


if __name__ == "__main__":
    t = int(input())
    for case in range(t):
        n, x = map(int, input().split())
        a = list(map(int, input().split()))
        if oddSelection(n, x, a):
            print("Yes")
        else:
            print("No")
