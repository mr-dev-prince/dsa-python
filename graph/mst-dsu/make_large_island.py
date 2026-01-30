from typing import List
from graph.dsu.disjoint_set import DisjointSet
class Solution:
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        ds = DisjointSet(n * n)

        # Step 1: connect all 1 components
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0: 
                    continue
                for dr, dc in self.directions:
                    nr, nc = i + dr, j + dc
                    if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1:
                        ds.unionBySize(i * n + j, nr * n + nc)

        # Step 2: try flipping each 0
        mx = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1: 
                    continue  # ✅ only flip 0

                comp = set()
                for dr, dc in self.directions:
                    nr, nc = i + dr, j + dc
                    if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1:
                        comp.add(ds.findUPar(nr * n + nc))

                size = 0
                for p in comp:
                    size += ds.size[p]

                mx = max(mx, size + 1)

        # Edge case: all 1s
        for i in range(n * n):
            mx = max(mx, ds.size[ds.findUPar(i)])

        return mx