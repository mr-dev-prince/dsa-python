# works with negative weights | only works on directed graph | if un-directed change to directed

def bellman(V, edges):
    # find shortest distance between all the nodes with -ve weights
    dist = [float("inf")] * V
    dist[0] = 0

    for _ in range(V):
        for u, v, w in edges:
            if dist[u] != "inf" and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    for u, v, w in edges:
        if dist[u] != "inf" and dist[u] + w < dist[v]:
            return [-1]


    return dist

print(bellman(5, [[1, 3, 2], [4, 3, -1], [2, 4, 1], [1, 2, 1], [0, 1, 5]]))