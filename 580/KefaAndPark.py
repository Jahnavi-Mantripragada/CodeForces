# https://codeforces.com/problemset/problem/580/C
# BFS
from collections import deque

if __name__ == "__main__":
    n, m = map(int, input().split())
    HasCat = list(map(int, input().split()))
    edges = [[] for i in range(n)]
    for i in range(n - 1):
        a, b = map(int, input().split())
        edges[a - 1].append(b - 1)
        edges[b - 1].append(a - 1)
    # Leaf node: # of edges = 1
    IsLeaf = [len(edges[i]) == 1 and i != 0 for i in range(n)]
    # print(IsLeaf)
    Visited = [False for i in range(n)]
    queue = deque()
    queue.append(0)
    Visited[0] = True
    restaurant = 0
    while queue:
        # print(queue, HasCat, restaurant)
        node = queue.popleft()
        HasCats = HasCat[node] > 0
        if HasCat[node] > m:
            continue
        for i in edges[node]:
            if not Visited[i]:
                Visited[i] = True
                queue.append(i)
                if HasCats and HasCat[i] > 0:
                    HasCat[i] += HasCat[node]
        if IsLeaf[node] and HasCat[node] <= m:
            restaurant += 1
    print(restaurant)
