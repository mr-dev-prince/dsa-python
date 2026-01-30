from typing import List

class Solution:
    def dfs(self, src, des, vis, adj):
        if src == des : return True

        vis[src] = True

        for nei in adj[src]:
            if not vis[nei]:
                if self.dfs(nei, des, vis, adj):
                    return True
        
        return False

    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination: return True
        elif len(edges) == 0: return False

        adj = {node : [] for node in range(n)}
        vis = [False] * n
        
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        return self.dfs(source, destination, vis, adj)