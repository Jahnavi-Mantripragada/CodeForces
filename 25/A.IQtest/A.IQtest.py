def IQtest(n, L):
    even, odd = 0, 0
    for i in range(n):
        if L[i] & 1 == 0:
            even += 1
        else:
            odd += 1
    if even >= odd:
        for i in range(n):
            if L[i] & 1 != 0:
                return i + 1
    else:
        for i in range(n):
            if L[i] & 1 == 0:
                return i + 1
if __name__ == '__main__':
    n = int(input())
    L = list(map(int, input().split()))
    print(IQtest(n, L))