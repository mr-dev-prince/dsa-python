def missing_positive(arr, k):
    num = 1
    i = 0
    while i < len(arr) and k > 0:
        if arr[i] == num:
            i += 1
        else: k -= 1
        num += 1
    
    num += k
    
    return num - 1

def missing_positive2(arr, k):
    l,r = 0, len(arr)

    while l <= r:
        m = (l + r)//2

        missing = arr[m] - (m + 1)

        if missing >= k:
            r = m - 1
        else:
            l = m + 1
        
    return l + k


print(missing_positive([2,3,4,5,7,11], 5))