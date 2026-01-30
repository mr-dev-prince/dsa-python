def search(nums, target):
    low, high = 0, len(nums) - 1

    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid

        # ascending order portion
        if nums[low] <= nums[mid]:
            if target > nums[mid] or target < nums[low]: # target does'nt exist on left
                low = mid + 1
            else:
                high = mid - 1
        # descending order portion
        else:
            if target < nums[mid] or target > nums[high]:
                high = mid - 1
            else:
                low = mid + 1
        
    return -1