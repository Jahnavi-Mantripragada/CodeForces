"""
https://codeforces.com/problemset/problem/455/A
"""
from collections import Counter

n = int(input())
a = list(map(int, input().split()))

c = Counter(a)
l = max(a)+1

WITHOUT = 0
WITH = 0
for i in range(l):
    NEW_WITHOUT = max(WITH, WITHOUT)
    NEW_WITH = i * c.get(i, 0) + WITHOUT
    WITH, WITHOUT = NEW_WITH, NEW_WITHOUT
print(max(WITH, WITHOUT))

