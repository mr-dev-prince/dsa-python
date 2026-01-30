def removeDuplicates(nums):
    if len(nums) < 2:
        return len(nums)

    write_idx = 2
    for i in range(2, len(nums)):
        if nums[i] != nums[write_idx - 2]:
            nums[i] = nums[write_idx]
            write_idx += 1
        
    return write_idx

print(removeDuplicates([1,2,2,2,3,3]))