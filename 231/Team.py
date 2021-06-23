"""
Implement if at least 2/3 feel sure about the solution.
"""
N = int(input())
solved = 0
for i in range(N):
    a, b, c = map(int, input().split())
    if a + b + c >= 2:
        solved += 1
print(solved)