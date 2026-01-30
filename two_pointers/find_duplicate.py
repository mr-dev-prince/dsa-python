def findDup(nums):
    slow, fast = 0, 0
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            # slow pointer is at intersection
            break
    
    slow2 = 0
    while True:
        slow = nums[slow]
        slow2 = nums[slow2]
        if nums[slow2] == nums[[slow]]:
            return nums[slow]