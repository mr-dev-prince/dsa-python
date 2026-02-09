from typing import List


class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        temp = 0
        for i in range(len(nums)):
            if str(bin(i)).count("1") == k:
                temp += nums[i]
        return temp
