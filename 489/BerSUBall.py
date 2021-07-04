"""
https://codeforces.com/problemset/problem/489/B
"""

n = int(input())
a = list(map(int, input().split()))

m = int(input())
b = list(map(int, input().split()))

a.sort()
b.sort()
boys = 0
girls = 0
pairs = 0
while boys < n and girls < m:
    gSkill, bSkill = b[girls], a[boys]
    if abs(gSkill - bSkill) <= 1:
        girls += 1
        boys += 1
        pairs += 1
    elif gSkill < bSkill:
        girls += 1
    else:
        boys += 1
print(pairs)
