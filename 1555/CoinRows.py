"""
score: the total number of coins Bob collects.
Alice wants to minimize the score.
Bob wants to maximize the score.
"""


def coinRows(grid, m):
    grid[0][0] = 0
    grid[1][m - 1] = 0
    prefixSum = [[grid[i][j] for j in range(m)] for i in range(2)]
    suffixSum = [[grid[i][j] for j in range(m)] for i in range(2)]

    for i in range(1, m):
        prefixSum[0][i] += prefixSum[0][i - 1]
        prefixSum[1][i] += prefixSum[1][i - 1]

    for i in range(m - 2, -1, -1):
        suffixSum[0][i] += suffixSum[0][i + 1]
        suffixSum[1][i] += suffixSum[1][i + 1]
    # print(grid)
    # print(prefixSum)
    # print(grid)
    # print(suffixSum)
    score = float("inf")
    for i in range(m):
        t = score
        if 1 <= i < m - 1:
            first = suffixSum[0][i + 1]
            second = prefixSum[1][i - 1]
            # print(i, first, second)
            t = max(first, second)
        elif i == 0 and i + 1 < m:
            t = suffixSum[0][i + 1]
        elif i == m - 1 and i > 0:
            t = prefixSum[1][i - 1]
        # print("{}: {}".format(i, t))
        score = min(score, t)
    return score if score != float("inf") else 0


if __name__ == '__main__':
    t = int(input())  # no of test cases
    for case in range(t):
        m = int(input())
        grid = []
        for i in range(2):
            grid.append(list(map(int, input().split())))
        print(coinRows(grid, m))
