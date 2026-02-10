from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [-1] * 1001

        def solve(idx):
            if idx >= len(cost):
                return 0

            if dp[idx] != -1:
                return dp[idx]

            a = cost[idx] + solve(idx + 1)
            b = cost[idx] + solve(idx + 2)

            dp[idx] = min(a, b)

            return min(a, b)

        return min(solve(0), solve(1))

    def bottomUp(self, cost: List[int]) -> int:
        pass
