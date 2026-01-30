from collections import deque

def detectCycleBfs(src, adjList, vis):
    q = deque((src, -1))
    vis[src] = 1

    while q:
        for _ in range(len(q)):
            node, src = q.popleft()
            for nei in adjList[node]:
                if not vis[nei]:
                    vis[nei] = 1
                    q.append((nei, node))
                elif vis[nei] and src != nei:
                    return True
                
    return False

def detectCycleDfs(node, src, adjList, vis):
    vis[node] = 1

    for nei in adjList[node]:
        if not vis[nei]:
            if detectCycleDfs(nei, node, adjList):
                return True
        elif nei != src:
            return True
        
    return False

def helper(adj):
    n = len(adj) 

    adjList = {node + 1 : [] for node in adj}

    for i in range(n):
        for j in range(n):
            if adj[i][j]:
                adjList[i + 1].append(j+1)

    vis = [0 for _ in range(n + 1)]

    # dfs 
    detectCycleDfs(0, 0, adjList, vis)

    # bfs 
    detectCycleBfs(0, adjList, vis)