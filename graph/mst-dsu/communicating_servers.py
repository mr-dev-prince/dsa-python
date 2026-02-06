from typing import List

class SizeDSU:
    def __init__(self, n):
        self.size = []
        self.parent = []
        
        for i in range(n + 1):
            self.size.append(1)
            self.parent.append(i)
    
    def find(self, n):
        if self.parent[n] == n : return n

        self.parent[n] = self.find(self.parent[n])
        return self.parent[n]

    def union(self, u, v):
        u_par = self.find(u)
        v_par = self.find(v)

        if u_par == v_par : return 

        if self.size[u_par] > self.size[v_par]:
            self.parent[v_par] = u_par
            self.size[u_par] += self.size[v_par]
        else:
            self.parent[u_par] = v_par
            self.size[v_par] += self.size[u_par]

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        ds = SizeDSU(n * m)
        
        # Track the first server seen in each row and column to union with others
        row_first = [-1] * n
        col_first = [-1] * m

        for r in range(n):
            for c in range(m):
                if grid[r][c]:
                    curr_idx = r * m + c
                    
                    # Union with the first server found in this row
                    if row_first[r] != -1:
                        ds.union(curr_idx, row_first[r])
                    else:
                        row_first[r] = curr_idx
                    
                    # Union with the first server found in this column
                    if col_first[c] != -1:
                        ds.union(curr_idx, col_first[c])
                    else:
                        col_first[c] = curr_idx

        # Count servers in components with size > 1
        ans = 0
        unique_roots = set()
        for r in range(n):
            for c in range(m):
                if grid[r][c]:
                    root = ds.find(r * m + c)
                    if root not in unique_roots:
                        root_size = ds.size[root]
                        if root_size > 1:
                            ans += root_size
                        unique_roots.add(root)
        return ans