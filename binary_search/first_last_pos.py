def posRange(nums, target):
    def bs(nums, target, leftBias):
            low, high = 0, len(nums) - 1
            i = -1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] < target:
                     low = mid + 1
                elif nums[mid] > target:
                     high = mid - 1
                else:
                    i = mid
                    if leftBias:
                        high = mid - 1
                    else:
                        low = mid + 1
            return i
    
    return [bs(nums, target, True), bs(nums, target, False)]


print(posRange([5,7,7,8,8,10], 8))