from collections import defaultdict


def HideAndSeek(n, k, BobsQuestions):
    indices = defaultdict(list)
    for i in range(k):
        indices[BobsQuestions[i]].append(i)
    #print(indices)
    count = 0
    for i in range(1, n + 1):
        for j in range(max(i-1, 1), min(i+2, n+1)):
            if i == j:
                if i not in indices:
                    #print(i, j)
                    count += 1
            elif j not in indices or i not in indices:
                #print(i, j)
                count += 1
            else:
                x = indices[i][0]
                y = indices[j][-1]
                if y < x:
                    count += 1
                    #print(i, j)
    return count


if __name__ == "__main__":
    n, k = map(int, input().split())
    BobsQuestions = list(map(int, input().split()))
    print(HideAndSeek(n, k, BobsQuestions))
