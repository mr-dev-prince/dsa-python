from typing import List
from collections import defaultdict
import heapq

class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        if n == 1 : return 0
        adj = defaultdict(list)

        for u, v, w in edges:
            adj[u].append((w,v))
            adj[v].append((w,u))

        def dijkstra():
            mh = [(0, n)]
            distances = [float("inf")] * (n + 1)
            distances[n] = 0

            while mh:
                d, u = heapq.heappop(mh)

                if d != distances[u]: continue

                for w, v in adj[u]:
                    if distances[v] > distances[u] + w:
                        distances[v] = distances[u] + w
                        heapq.heappush(mh, (distances[v], v))

            return distances
        
        @lru_cache(None)
        def dfs(start):
            if start == n:
                return 1
            res = 0

            for _, nei in adj[start]:
                if distances[start] > distances[nei]:
                    res = (res + dfs(nei)) % (10**9+7)
            
            return res
        
        distances = dijkstra()
        return dfs(1)
