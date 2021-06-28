"""
A type rides: one ride -> a rubles
B type rides: m rides -> b rubles
"""
"""
For n rides:

A + B * m = n

Cost: A*a + B*b
"""

n, m, a, b = map(int, input().split())

# if riding m rides using A type ticket value (m * a)
# is less than B type ticket (b), we will never get to use B type tickets
# Otherwise, if m * a > b -> as much as possible we will use B type ticket.

if m * a <= b:
    print(n * a)
else:
    q, r = divmod(n, m)
    print(b*q + min(b, r*a))
