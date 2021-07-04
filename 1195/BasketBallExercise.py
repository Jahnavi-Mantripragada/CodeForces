import sys

sys.setrecursionlimit(10 ** 6)


# No adjacent elements
# Every element picked should have a greater index than the previously picked one

def BasketBallExercise(n, first, second):
    """
    Q1 Q2
    Q3 Q4

    how do we calculate values at col (Q2, Q4)? max(Q3 + Q2, Q1), since Q1 and Q2 can't be taken together (adjacent
    in same row) max(Q1+Q4, Q3), since Q3 and Q4 can't be taken together (adjacent in same row) if we observe,
    we cannot take (Q1, Q3) or (Q2, Q4) as pairs, since we choose elements only in increasing order of their indices.

    Example 1:

    1 2 9
    10 1 1

    max(0, 1 + 0), max(0, 10 + 0) --> 1,10
    (1) 2 9     1 2 9
    10 1 1     (10) 1 1

    max(1, 10 + 2), max(10, 1 + 1) --> 12, 10
    (1) 2 9    or   1 (2) 9
    10 1 1        (10) 1 1
    (1) 2 9   or    1 2 9
    10 (1) 1      (10) 1 1

    max(12, 10+9), max(10, 12+1) --> 19, 13
    1 (2) 9    or   1 2 (9)
    (10) 1 1        (10) 1 1
    1 2 9   or    1 (2) 9
    (10) 1 1      (10) 1 (1)

    Final Answer: 19
    1 2 (9)
    (10) 1 1
    """
    # before value: the total value of height taking the before element in the same row
    # without before element: the total value of height without taking the before element in the same row
    dp = [[0 for i in range(3)] for i in range(n + 1)]
    for i in range(1, n + 1):
        # Take before value from row 1 along with current row 2
        dp[i][1] = dp[i - 1][0] + second[i - 1]
        # Take before value from row 2 along with current row 1
        dp[i][0] = dp[i - 1][1] + first[i - 1]
        # if we did not take before element from row 1
        dp[i][0] = max(dp[i - 1][2] + first[i - 1], dp[i][0])
        # if we did not take before element from row 2
        dp[i][1] = max(dp[i - 1][2] + second[i - 1], dp[i][1])
        # don't take any of the current elements
        dp[i][2] = max(dp[i - 1][0], dp[i - 1][1])
    return max(dp[n][0], dp[n][1])


if __name__ == "__main__":
    n = int(input())
    first = list(map(int, input().split()))
    second = list(map(int, input().split()))
    print(BasketBallExercise(n, first, second))
