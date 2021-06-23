"""
Odd + Odd = Even
Even + Even = Even
Odd + Even = Odd
Even + Odd = Odd
"""
N = int(input())
if N % 2 == 0 and N >= 4:
    print("YES")
else:
    print("NO")
