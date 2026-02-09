from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        l = r = 0

        while r < len(s) and l < len(g):
            if s[r] >= g[l]:
                l += 1
            r += 1

        return l
