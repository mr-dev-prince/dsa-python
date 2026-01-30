from collections import deque

class Solution:
    def shortestPath(self, V, edges, src):
        dis = [-1] * V
        
        adj = {node : [] for node in range(V) }
        
        for start, end in edges:
            adj[start].append(end)
            adj[end].append(start)
            

        q = deque([src])
        # bfs guarantees shortest path
        dis[src] = 0
        
        while q:
            node = q.popleft()
            for nei in adj[node]:
                if dis[nei] == -1: # not visited
                    dis[nei] = dis[node] + 1
                    q.append(nei)
                
        return dis
        