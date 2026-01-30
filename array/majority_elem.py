# brute force algo
def majorityElem(nums):
    freq = {}
    ans = []
    for n in nums:
        freq[n] = 1 + freq.get(n, 0)

    for key, val in freq.items():
        if val >= len(nums) / 3:
            ans.append(key)
    return ans


# boyer-moore voting algo
# in an arr of size n : there can be atmost (k-1) elements that appear n/k times
# n/2 => 1 majority element
# n/3 => 2 majority elements
# n/4 => 3 majority elements ans so on


def majorityElem1(nums):
    maj = None
    cnt = 0

    for n in nums:
        if n == maj:
            cnt += 1
        elif cnt == 0:
            maj = n
            cnt += 1
        else:
            cnt -= 1

    return maj


def majorityElement(nums):
    maj1 = None
    maj2 = None
    cnt1 = 0
    cnt2 = 0
    for n in nums:
        if n == maj1:
            cnt1 += 1
        elif n == maj2:
            cnt2 += 1
        elif cnt1 == 0:
            maj1 = n
            cnt1 += 1
        elif cnt2 == 0:
            maj2 = n
            cnt2 += 1
        else:
            cnt1 -= 1
            cnt2 -= 1

    ans = []
    freq1 = 0
    freq2 = 0
    for n in nums:
        if n == maj1:
            freq1 += 1
        elif n == maj2:
            freq2 += 1
    if freq1 > len(nums) / 3:
        ans.append(maj1)
    if freq2 > len(nums) / 3:
        ans.append(maj2)
    return ans
