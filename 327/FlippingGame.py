"""
https://codeforces.com/problemset/problem/327/A
"""
n = int(input())
a = list(map(int, input().split()))

before_flip = a.count(1)

max_diff = -float("inf")
diff = 0
for i in range(n):
    if a[i] == 1:
        diff = max(diff-1, -1)
    elif a[i] == 0:
        diff = max(diff+1, 1)
    max_diff = max(max_diff, diff)

after_flip = before_flip + max_diff
print(after_flip)