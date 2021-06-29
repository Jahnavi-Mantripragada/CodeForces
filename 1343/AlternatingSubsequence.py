T = int(input())
for case in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    L = []
    pos, neg = [], []
    for i in range(n):
        if a[i] > 0:
            if neg:
                L.append(neg)
                neg = []
            pos.append(a[i])
        elif a[i] < 0:
            if pos:
                L.append(pos)
                pos = []
            neg.append(a[i])
    if pos:
        L.append(pos)
    if neg:
        L.append(neg)

    max_sum = 0
    for x in L:
        max_sum += max(x)
    print(max_sum)
