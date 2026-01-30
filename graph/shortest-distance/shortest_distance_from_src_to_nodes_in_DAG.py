def dfs(src, st, vis, adj):
    vis[src] = 1

    for v, _ in adj[src]:
        if not vis[v]:
            dfs(v, st, vis, adj)

    st.append(src)

def findShortestPaths(V, adjMat, src):
    # build adj list
    adj = {node : [] for node in range(V)}

    for u, v, d in adjMat:
        adj[u].append([v, d])

    vis = [0 for _ in range(V)]
    st = []

    for i in range(V):
        if not vis[i]:
            dfs(i, st, vis, adj)

    topo = []

    while st:
        topo.append(st.pop())

    dis = [float("inf")] * V
    dis[src] = 0

    for node in topo:
        if dis[node] == float("inf"):
            continue
        for v, d in adj[node]:
            dis[v] = min(dis[v], dis[node] + d)

    for i in range(len(dis)):
        if dis[i] == float("inf"):
            dis[i] = -1

    return dis

edges = [[0,1,2], [0,4,1], [4,5,4], [4,2,2], [1,2,3], [2,3,6], [5,3,1]] # [src, destination, weight]
V = 6 # vertices

print(findShortestPaths(V, edges, 0))