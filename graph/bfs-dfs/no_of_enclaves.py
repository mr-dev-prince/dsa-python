from typing import List

class Solution:
    directions = [(1,0), (-1, 0), (0, 1), (0, -1)]

    def dfs(self, grid, r, c, vis):
        vis[r][c] = 1
        for dr, dc in self.directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and not vis[nr][nc] and grid[nr][nc]:
                self.dfs(grid, nr, nc, vis)


    def numEnclaves(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        vis = [[0] * col for _ in range(row)]

        count = 0

        # first and last row
        for c in range(col):
            if not vis[0][c] and grid[0][c]:
                self.dfs(grid, 0, c, vis)
            
            if not vis[row - 1][c] and grid[row - 1][c]:
                self.dfs(grid, row - 1, c, vis)
            
        # first and last column
        for r in range(row):
            if not vis[r][0] and grid[r][0]:
                self.dfs(grid, r, 0, vis)

            if not vis[r][col - 1] and grid[r][col - 1]:
                self.dfs(grid, r, col - 1, vis)
        
        for i in range(row):
            for j in range(col):
                if vis[i][j] != grid[i][j]:
                    count += 1

        return count
