def btwYWise(A, B, F):
    if A[1] <= F[1] <= B[1]:
        return True
    if B[1] <= F[1] <= A[1]:
        return True
    return False


def btwXWise(A, B, F):
    if A[0] <= F[0] <= B[0]:
        return True
    if B[0] <= F[0] <= A[0]:
        return True
    return False


def shortestPath(A, B, F):
    if A[0] == B[0] == F[0] and btwYWise(A, B, F):
        return 2 + abs(A[0] - B[0]) + abs(A[1] - B[1])
    if A[1] == B[1] == F[1] and btwXWise(A, B, F):
        return 2 + abs(A[0] - B[0]) + abs(A[1] - B[1])
    return abs(A[0] - B[0]) + abs(A[1] - B[1])


if __name__ == "__main__":
    t = int(input())
    for case in range(t):
        C = input()
        A = tuple(map(int, input().split()))
        B = tuple(map(int, input().split()))
        F = tuple(map(int, input().split()))
        print(shortestPath(A, B, F))
