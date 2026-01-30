# multi-src shortest path algorithm
# shortest path from every node to every node

def floyd_warshal(edges):
    V = len(edges)
    # return matrix of shortest distance 
    for i in range(V):
        for j in range(V):
            if edges[i][j] == -1:
                edges[i][j] = float("inf")
            if i == j : edges[i][j] = 0

    for via in range(V):
        for i in range(V):
            for j in range(V):
                edges[i][j] = min(edges[i][j], edges[i][via] + edges[via][j])

    for i in range(V):
        for j in range(V):
            if edges[i][j] == float("inf"):
                edges[i][j] = -1 

    return edges

print(floyd_warshal([[0, 25], [-1, 0]]))
