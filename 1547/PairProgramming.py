def order(k, n, m, a, b):
    i = 0
    j = 0
    o = []
    while i < n and j < m:
        Mono = a[i]
        Poly = b[j]
        # print(o, Mono, Poly, k)
        if Mono == 0:
            i += 1
            k += 1
            o.append(Mono)
        elif Poly == 0:
            j += 1
            k += 1
            o.append(Poly)
        elif 0 < Mono <= k:
            i += 1
            o.append(Mono)
        elif 0 < Poly <= k:
            j += 1
            o.append(Poly)
        else:
            return [-1]
    while i < n:
        Mono = a[i]
        if Mono == 0:
            i += 1
            k += 1
            o.append(Mono)
        elif 0 < Mono <= k:
            i += 1
            o.append(Mono)
        else:
            return [-1]
    while j < m:
        Poly = b[j]
        if Poly == 0:
            j += 1
            k += 1
            o.append(Poly)
        elif 0 < Poly <= k:
            j += 1
            o.append(Poly)
        else:
            return [-1]
    return o


if __name__ == "__main__":
    t = int(input())
    for case in range(t):
        c = input()
        k, n, m = map(int, input().split())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        print(" ".join(map(str, order(k, n, m, a, b))))
