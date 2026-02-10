# bit masking

def findKor(nums, k):
    ans = 0

    for i in range(31):
        count = 0

        mask = 1 << i

        for n in nums:
            if n & mask:
                count += 1
        
        if count >= k:
            ans += mask
            

    return mask