from typing import List

class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        rows, cols = len(grid), len(grid[0])

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        vis = [[False for _ in range(cols)] for _ in range(rows)]

        def dfs(r, c):
            vis[r][c] = True

            cur_val = grid[r][c]

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] and not vis[nr][nc]:
                    cur_val += dfs(nr, nc)
            
            return cur_val
        
        res = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] and not vis[r][c]:
                    val = dfs(r, c)
                    if val % k == 0:
                        res += 1
        
        return res