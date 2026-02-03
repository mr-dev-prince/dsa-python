from collections import defaultdict
from typing import List

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        adj = defaultdict(list)

        for u, v in prerequisites:
            adj[v].append(u)
        
        def dfs(crs):
            if crs not in mp:
                for nei in adj[crs]:
                    mp[crs] |= dfs(nei) # union
                mp[crs].add(crs)
            return mp[crs]

        mp = defaultdict(set)

        for crs in range(numCourses):
            dfs(crs)
        
        result = []
        for u, v in queries:
            result.append(u in mp[v])

        return result