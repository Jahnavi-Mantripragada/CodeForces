import bisect

n = int(input())
a = list(map(int, input().split()))
m = int(input())
q = list(map(int, input().split()))

start_end = [(1, a[0])]
for i in range(1, n):
    start_end.append((start_end[-1][1] + 1, start_end[-1][1] + a[i]))
length = len(start_end)
for query in q:
    pos = bisect.bisect(start_end, (query, query))
    if pos == length:
        print(length)
    else:
        s, e = start_end[pos]
        if s <= query <= e:
            print(pos + 1)
        else:
            print(pos)
