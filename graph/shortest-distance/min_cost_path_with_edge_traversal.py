from collections import defaultdict
from typing import List
import heapq


class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)

        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, 2 * w))

        dis = [float("inf")] * n
        dis[0] = 0

        pq = [(0, 0)]

        while pq:
            di, node = heapq.heappop(pq)

            if di > dis[node]:
                continue

            if node == n - 1:
                return di

            for nbr, d in adj[node]:
                nd = d + di
                if nd < dis[nbr]:
                    dis[nbr] = nd
                    heapq.heappush(pq, (nd, nbr))

        return -1
