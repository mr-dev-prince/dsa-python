def peakIn1D(nums):
    # modified Binary Search  | whichever side you find the greater element - go to that side
    l, r = 0, len(nums) - 1

    while l <= r:
        m = l + ((r - l) // 2)
        if m > 0 and nums[m] < nums[m-1]:
            r = m - 1
        elif m < len(nums) - 1 and nums[m] < nums[m + 1]:
            l = m + 1
        else:
            return m
    
def peakIn2D(nums):
    def findMaxRow(mid):
        ans = 0
        for i in range(len(nums)):
            if nums[i][mid] > nums[ans][mid]:
                ans = i

        return ans
    
    row, col = len(nums), len(nums[0])

    l , r = 0, col - 1

    while l <= r:
        mid = l + ( r - l) // 2

        maxRow = findMaxRow(mid)

        left = nums[maxRow][mid - 1] if mid - 1 >= 0 else -1
        right = nums[maxRow][mid + 1] if mid + 1 < col else -1

        if left < nums[maxRow][mid] > right:
            return [maxRow, mid]
        elif nums[maxRow][mid] < left:
            r = mid - 1
        else:
            l = mid + 1

    return [-1, -1]
