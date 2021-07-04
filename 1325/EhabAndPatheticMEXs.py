def EhabAndPatheticMEXs(n, e, max_node):
    Label = [None for i in range(n-1)]
    label = 0
    for index in e[max_node]:
        if Label[index] is None:
            Label[index] = label
            label += 1

    for i in range(n-1):
        if Label[i] is None:
            Label[i] = label
            label += 1

    return Label


if __name__ == "__main__":
    n = int(input())
    degree = [0 for i in range(n+2)]
    edges = [[] for i in range(n+2)]
    max_, max_node = 0, 1
    for i in range(n - 1):
        u, v = map(int, input().split())
        edges[u].append(i)
        edges[v].append(i)
        degree[u] += 1
        degree[v] += 1
    for node in range(1, n+1):
        if max_ < degree[node]:
            max_ = degree[node]
            max_node = node
    L = EhabAndPatheticMEXs(n, edges, max_node)
    for x in L:
        print(x)