"""
https://codeforces.com/problemset/problem/520/B
"""
"""
red button -> * 2
blue button -> - 1

stop when number on screen < 0
"""

from collections import deque

n, m = map(int, input().split())

queue = deque()
queue.append((m, 0))
seen = set()
while queue:
    number, steps = queue.popleft()
    if number == n:
        print(steps)
        break
    if number in seen:
        continue
    seen.add(number)
    if number % 2 == 0:
        queue.append((number // 2, steps + 1))
    queue.append((number + 1, steps + 1))
