def dfs(graph, vis, pathVis, src):
    vis[src] = 1
    pathVis[src] = 1

    for node in graph[src]:
        if not vis[node]:
            if dfs(graph, vis, pathVis, node):
                return True
        elif pathVis[node]:
            return True
        
    pathVis[src] = 0
    return False

# space complexity - O(2N) | TC = O(V+E)

def detect_cycle(graph):
    n = len(graph)

    vis = [0] * n
    pathVis = [0] * n

    for i in range(n):
        if not vis[i]:
            if dfs(graph, vis, pathVis, i):
                return True
            
    return False