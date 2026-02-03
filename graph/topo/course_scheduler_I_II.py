from typing import List
from collections import deque


class Solution:
    # course scheduler I
    def canFinishI(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for course, preReq in prerequisites:
            adjList[preReq].append(course)
            indegree[course] += 1

        q = deque()
        cnt = 0

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        while q:
            curr = q.popleft()
            cnt += 1

            for nxt in adjList[curr]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0: 
                    q.append(nxt)

        return cnt == numCourses
    
    # course scheduler II
    def canFinishII(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for course, preReq in prerequisites:
            adjList[preReq].append(course)
            indegree[course] += 1

        q = deque([i for i, v in enumerate(indegree) if v == 0])
        topo = []

        while q:
            curr = q.popleft()
            topo.append(curr)

            for nxt in adjList[curr]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0: 
                    q.append(nxt)

        return topo if len(topo) == numCourses else []

