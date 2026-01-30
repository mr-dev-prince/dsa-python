from typing import List

class Solution:
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    
    def dfs(self, r, c, pr, pc, grid, vis, rows, cols):       
        vis[r][c] = True

        for dr, dc in self.directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == grid[r][c]:
                if not vis[nr][nc]:
                    if self.dfs(nr, nc, r, c, grid, vis, rows, cols):
                        return True
                
                elif (nr, nc) != (pr, pc):
                    return True

        return False
            

    def containsCycle(self, grid: List[List[str]]) -> bool:
        rows, cols = len(grid), len(grid[0])
        vis = [[False] * cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if not vis[i][j]:
                    if self.dfs(i, j, -1, -1, grid, vis, rows, cols):
                        return True

        return False