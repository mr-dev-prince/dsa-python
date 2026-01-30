def search(self, nums, target):
    # duplicated values allowed and arr was sorted in non-increasing order before rotation
    l, r = 0, len(nums) - 1
    while l <= r:
        m = (l + r) // 2
        if nums[m] == target: return True
        if nums[l] < nums[m]:
            if nums[l] <= target < nums[m]:
                r = m - 1
            else:
                l = m + 1
        elif nums[l] > nums[m]:
            if nums[m] < target <= nums[r]:
                l = m + 1
            else:
                r = m - 1
        # if values at mid and low are equal - we don't know whether it contains other numbers or just same duplicated number
        else:
            l += 1
    return False    