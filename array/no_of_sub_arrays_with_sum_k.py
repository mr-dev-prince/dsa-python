def subArraySum(nums, k):
    count = 0
    curSum = 0

    freq = {}
    freq[0] = 1

    for x in nums:
        curSum += x
        diff = curSum - k
        count += freq.get(diff, 0)
        freq[curSum] = 1 + freq.get(curSum, 0)

    return count

print(subArraySum([1,1,1], 2))