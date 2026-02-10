from collections import defaultdict
import heapq
from typing import List


class Solution:
    def maxProbability(
        self,
        n: int,
        edges: List[List[int]],
        succProb: List[float],
        start_node: int,
        end_node: int,
    ) -> float:
        adj = defaultdict(list)

        for i in range(len(edges)):
            u, v = edges[i]
            p = succProb[i]
            adj[u].append((v, p))
            adj[v].append((u, p))

        prob = [0.0] * n
        prob[start_node] = 1.0

        pq = [(-1, start_node)]

        while pq:
            cPr, node = heapq.heappop(pq)
            cPr = -cPr

            if cPr < prob[node]:
                continue

            if node == end_node:
                return cPr

            for nei, pr in adj[node]:
                nxtPr = cPr * pr
                if nxtPr > prob[nei]:
                    prob[nei] = nxtPr
                    heapq.heappush(pq, (-nxtPr, nei))

        return prob[end_node]
