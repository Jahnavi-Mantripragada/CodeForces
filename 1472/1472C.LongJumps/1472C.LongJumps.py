def MaxScore(a, n):
    score = [0 for i in range(n+1)]
    for i, x in enumerate(a):
        if i + x > n:
            score[n] = max(score[i]+x, score[n])
        else:
            score[i+x] = max(score[i+x], score[i]+x)
    return score[n]


if __name__ == "__main__":
    T = int(input())
    for case in range(T):
        n = int(input())
        a = list(map(int, input().split()))
        print(MaxScore(a, n))
