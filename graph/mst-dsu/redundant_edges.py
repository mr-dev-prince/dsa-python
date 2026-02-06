from typing import List

class SizeDSU:
    def __init__(self, n):
        self.size = []
        self.parent = []
        self.maxSize = 1 if n > 0 else 0

        for i in range(n + 1):
            self.size.append(1)
            self.parent.append(i)
        
    def find(self, n):
        if self.parent[n] == n: return n

        self.parent[n] = self.find(self.parent[n])
        return self.parent[n]
    
    def union(self, u, v):
        u_par = self.find(u)
        v_par = self.find(v)

        if u_par == v_par : return 

        if self.size[u_par] > self.size[v_par]:
            self.parent[v_par] = u_par
            self.size[u_par] += self.size[v_par]
            self.maxSize = max(self.maxSize, self.size[u_par])
        else:
            self.parent[u_par] = v_par
            self.size[v_par] += self.size[u_par]
            self.maxSize = max(self.maxSize, self.size[v_par])

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0

        unique_nums = set(nums)
        ds = SizeDSU(len(unique_nums))

        val_to_idx = {val : i for i, val in enumerate(unique_nums)}

        for val in unique_nums:
            if val + 1 in val_to_idx:
                ds.union(val_to_idx[val], val_to_idx[val + 1])
        
        return ds.maxSize