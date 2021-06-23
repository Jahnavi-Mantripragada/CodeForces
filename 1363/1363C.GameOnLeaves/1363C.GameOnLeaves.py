from collections import defaultdict


def Winner(degree, n, x):
    if n == 1:
        return "Ayush"
    if degree[x] <= 1:
        return "Ayush"
    if n % 2 != 0:
        return "Ashish"
    return "Ayush"


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, x = map(int, input().split())
        degree = dict()
        for i in range(n - 1):
            u, v = map(int, input().split())
            degree[v] = degree.get(v, 0) + 1
            degree[u] = degree.get(u, 0) + 1

        print(Winner(degree, n, x))
