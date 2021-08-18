"""
https://codeforces.com/problemset/problem/1553/C
"""
def minPossibleKicks(predictions):
    n = len(predictions)
    d = n

    scores = [0, 0]
    for turn in range(n):
        if turn % 2 == 0:
            scores[0] += (predictions[turn] == '1')
        else:
            scores[1] += (predictions[turn] != '0')
        if scores[0] > scores[1] + (10 - turn) // 2:
            d = min(d, turn)
        if scores[1] > scores[0] + (9 - turn) // 2:
            d = min(d, turn)

    scores = [0, 0]
    for turn in range(n):
        if turn % 2 != 0:
            scores[1] += (predictions[turn] == '1')
        else:
            scores[0] += (predictions[turn] != '0')
        if scores[0] > scores[1] + (10 - turn) // 2:
            d = min(d, turn)
        if scores[1] > scores[0] + (9 - turn) // 2:
            d = min(d, turn)

    return min(n, d + 1)


if __name__ == "__main__":
    t = int(input())
    for case in range(t):
        s = input()
        print(minPossibleKicks(s))
