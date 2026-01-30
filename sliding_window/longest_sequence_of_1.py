def longestSeq(nums, k):
    # k is the number of zeroes you can flip to 1 to achieve max length
    ws = 0
    freqOf0 = 0
    maxi = 0
    for we in range(len(nums)):
        if nums[we] == 0:
            freqOf0 += 1

        while freqOf0 > k:
            ws += 1
            if nums[ws] == 0:
                freqOf0 -= 1
            

        maxi = max(maxi, we - ws + 1)

    return maxi

print(longestSeq([1,0,0,1,1,1,0,1], 2))


