def singleNonDuplicate(self, nums):
    l, r = 0, len(nums) - 1
    while l <= r:
        m = l + (r - l) // 2

        # if values at mid doesn't match val on either sides -> that is the answer
        if (m - 1 < 0 or nums[m - 1] != nums[m]) and (m + 1 == len(nums) or nums[m] != nums[m+1]):
            return nums[m]
        
        #- core idea 1: if we find out that two consecutive elements are equal -> middle and left or middle and right:
            # we ignore both of these values

        #- core idea 2: since it is given that all the other elements appear twice
            # we can suppose that after finding out that mid value where we are currently at is duplicate, the unique
            # value will exist on the side having odd number of elements left
        leftSize = m - 1 if nums[m-1] == nums[m] else m
        # here - if the element on the left and middle elements are equal 
            # we can assume that the length of remaining array on left side is [m - 1]
            # or if it is not equal -> lenght of the remaining left array on left side is [m]

        if leftSize % 2: # true if left size is odd else false
            # if the left side of array is odd -> we search on left -> r = m + 1
            r = m - 1
        else:
            # if the right side of the array is odd -> we search on right -> l = m + 1
            l = m + 1