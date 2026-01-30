from typing import List
from collections import deque

class Solution:
    # reverse graph & kahn's algorithm
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        indegree = [0] * len(graph)
        q = deque()

        # reverse the graph
        revGraph = [[] for _ in range(len(graph))]
        for u in range(len(graph)):
            for v in graph[u]:
                revGraph[v].append(u)
                indegree[u] += 1
        
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)

        while q:
            cur = q.popleft()
            for nxt in revGraph[cur]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    q.append(nxt)
        
        ans = []

        for i in range(len(indegree)):
            if indegree[i] == 0:
                ans.append(i)

        return ans