from typing import List
from collections import deque

class Solution:
    directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]

    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        row, col = len(mat), len(mat[0])
        q = deque()

        ans = [[-1] * col for _ in range(row)] # -1 : not visited | 0 : visited | 1-inf : distance

        for i in range(row):
            for j in range(col):
                if mat[i][j] == 0:
                    ans[i][j] = 0
                    q.append((i, j))

        while q:
            r, c = q.popleft()
            for dr, dc in self.directions:
                nr , nc = r + dr, c + dc
                if 0 <= nr < row and 0 <= nc < col and ans[nr][nc] == -1:
                    ans[nr][nc] = ans[r][c] + 1
                    q.append((nr, nc))
        
        return ans
