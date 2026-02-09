from typing import List

class SizeDSU:
    def __init__(self, n):
        self.size = [1] * (n + 1)
        self.parent = list(range(n + 1))
        # track min weight for each component root
        self.min_edge = [float("inf")] * (n + 1)
    
    def find(self, n):
        if self.parent[n] == n: 
            return n
        self.parent[n] = self.find(self.parent[n])
        return self.parent[n]

    def union(self, u, v, wt):
        u_par = self.find(u)
        v_par = self.find(v)

        # We must update the min weight of the component regardless of 
        # whether they are already in the same set.
        if u_par != v_par:
            if self.size[u_par] > self.size[v_par]:
                self.parent[v_par] = u_par
                self.size[u_par] += self.size[v_par]
                # Update the new root's min edge with the other root's min
                self.min_edge[u_par] = min(self.min_edge[u_par], self.min_edge[v_par], wt)
            else:
                self.parent[u_par] = v_par
                self.size[v_par] += self.size[u_par]
                self.min_edge[v_par] = min(self.min_edge[v_par], self.min_edge[u_par], wt)
        else:
            # Even if already connected, this specific road might be the smallest
            self.min_edge[u_par] = min(self.min_edge[u_par], wt)

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        ds = SizeDSU(n)

        for u, v, wt in roads:
            ds.union(u, v, wt)
        
        # Find the root of the component containing city 1
        root_1 = ds.find(1)
        return ds.min_edge[root_1]