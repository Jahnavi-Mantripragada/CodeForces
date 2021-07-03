# https://codeforces.com/problemset/problem/1399/C
from collections import Counter


def MaxPairs(n, w):
    max_pairs = 0
    for s in range(2 * max(w)+1):
        c = Counter(w)
        pairs = 0
        for i in range(n):
            if c[w[i]] > 0 and s - w[i] in c and c[s-w[i]] > 0:
                if w[i] == s - w[i] and c[w[i]] == 1:
                    continue
                c[s - w[i]] -= 1
                c[w[i]] -= 1
                pairs += 1

        max_pairs = max(pairs, max_pairs)
    return max_pairs


if __name__ == "__main__":
    t = int(input())
    for case in range(t):
        n = int(input())
        w = list(map(int, input().split()))
        print(MaxPairs(n, w))
