"""
https://codeforces.com/problemset/problem/451/B
"""
def subUnsort(A):
    answer = []
    minElement = max(A)
    maxElement = min(A)
    start, end = -1, -1

    # Where did the sorting conflict occur? (from front)
    for i in range(len(A) - 1):
        if A[i] > A[i + 1]:
            start = i
            break
    # Where did the sorting conflict occur? (from back )
    for i in range(len(A) - 1, 0, -1):
        if A[i] < A[i - 1]:
            end = i
            break
    # No Conflict??
    if start == -1 or end == -1:
        return [1, 1]
    # Else, we calculate the maximum and minimum elements in this A[start:end]
    minElement = float("inf")
    maxElement = -float("inf")
    for i in range(start, end + 1):
        minElement = min(minElement, A[i])
        maxElement = max(maxElement, A[i])
    """
    In a sorted array, the smaller elements should be at the beginning,
    Let's see an example: [2,3,1,5,7,4,6]
    Now, our start and end:    ^     ^
    But, as we can see [2,3] are greater than 1 but there are not included in the unsorted part.
    And also from back, [6] is certainly less than 7 and it should be included too.
    For, this we found max and min elements in that range.
    
    Though there is no guarantee that the sub array we find between start and end is in descending order,
    but, we will make sure we include the correct possible sub-array.
    """
    for i in range(start):
        if A[i] > minElement:
            start = i
            break
    for i in range(len(A) - 1, end, -1):
        if A[i] < maxElement:
            end = i
            break
    # Are they in descending order??
    for i in range(start + 1, end + 1):
        if A[i] > A[i - 1]:
            return [-1, -1]
    return [start + 1, end + 1]


if __name__ == "__main__":
    n = int(input())
    A = list(map(int, input().split()))
    s,e = subUnsort(A)
    if s == -1 or e == -1:
        print("no")
    else:
        print("yes")
        print(s, e)
