def findMin(self, nums):
    l, r = 0, len(nums) - 1
    res = float("inf")
    while l <= r:
        # if the current portion is already sorted
        if nums[l] < nums[r]:
            res = min(res, nums[l])
            break

        m = (l + r) // 2

        res = min(res, nums[m])

        # left sorted array -> search on right -> because we will find smaller values on right as the array is rotated 1-n times 
        if nums[m] >= nums[l]:
            l = m + 1
        # right sorted array -> search on left
        else:
            r = m - 1
        
    return res
    
# another approach could be -> find the pivot and return the second value for asceding sorted array and first value for descending sorted array

