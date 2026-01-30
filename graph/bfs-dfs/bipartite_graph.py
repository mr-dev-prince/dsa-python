# a graph where every node of the graph can be colored with only two colors such 
# that none of the two adjacent nodes have same color

# a graph can never be bipartite if it has odd length cycle
# linear graphs are always bipartite

def isBipartite(adjList, src, vis, col):
    vis[src] = col

    for node in adjList[src]:
        if vis[node] == -1:
            if not isBipartite(adjList, node, vis, not col):
                return False
            elif vis[node] == col:
                return False
    return True

def helper(graph):
    n = len(graph)
    vis = [-1] * n

    # for disconnected graphs
    for i in range(n):
        if vis[i] == -1:
            if not isBipartite(graph, i, vis, 0):
                return False
    return True