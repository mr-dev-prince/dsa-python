from typing import List
import heapq

class Solution:
    directions = [
        (-1, -1), (1, -1), (-1, 1), (1, 1),
        (-1, 0), (1, 0), (0, -1), (0, 1)
    ]

    def shortestPathBinaryMatrix(self, mat: List[List[int]]) -> int:
        n = len(mat)

        # blocking cases
        if mat[0][0] == 1 or mat[n-1][n-1] == 1:
            return -1

        dis = [[float("inf") for _ in range(n)] for _ in range(n)]

        pq = [(1, (0, 0))]

        dis[0][0] = 1

        while pq:
            curDis, (r, c) = heapq.heappop(pq)

            if curDis > dis[r][c]:
                continue

            if r == n - 1 and c == n - 1:
                return curDis
            
            for dr, dc in self.directions:
                newR, newC = r + dr, c + dc

                if 0 <= newR < n and 0 <= newC < n and mat[newR][newC] == 0:
                    if curDis + 1 < dis[newR][newC]:
                        dis[newR][newC] = curDis + 1
                        heapq.heappush(pq, (curDis + 1, (newR, newC)))
        return -1