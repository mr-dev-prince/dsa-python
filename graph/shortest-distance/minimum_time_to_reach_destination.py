from collections import defaultdict
from typing import List
import heapq


class Solution:
    def minTime(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        ans = [float("inf")] * n

        for u, v, s, e in edges:
            adj[u].append((v, s, e))

        pq = [(0, 0)]
        ans[0] = 0

        while pq:
            t, u = heapq.heappop(pq)

            if t > ans[u]:
                continue

            if u == n - 1:
                return t

            for v, st, en in adj[u]:
                if st <= t and en >= t and ans[v] > t:
                    ans[v] = t + 1
                    heapq.heappush(pq, (t + 1, v))
                elif t < st and ans[v] > st + 1:
                    ans[v] = st + 1
                    heapq.heappush(pq, (st + 1, v))

        return -1
