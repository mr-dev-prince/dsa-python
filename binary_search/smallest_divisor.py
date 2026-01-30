import math

def smallestDivisor(nums, maxDivisionRes):
    l, r = 1, max(nums)

    res = 0

    while l <= r:
        m = (l + r) // 2

        total = 0
        for n in nums:
            total += math.ceil(n/m)
        
        if total <= maxDivisionRes:
            res = m
            r = m - 1
        else:
            l = m + 1
    
    return res
