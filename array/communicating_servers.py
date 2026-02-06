from typing import List

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        
        row_servers = [0] * n
        col_servers = [0] * m

        for r in range(n):
            for c in range(m):
                if grid[r][c]:
                    row_servers[r] += 1
                    col_servers[c] += 1
        
        ans = 0

        for r in range(n):
            for c in range(m):
                if grid[r][c]:
                    if row_servers[r] > 1 or col_servers[c] > 1:
                        ans += 1
        
        return ans