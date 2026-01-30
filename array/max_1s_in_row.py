def rowWithMax1s(arr):
    maxRow = -1
    maxi = 0
    for i in range(len(arr)):
        cur = 0
        for j in range(len(arr[i])):
            if arr[i][j] == 1:
                cur += 1
        if cur > maxi:
            maxRow = i
            maxi = cur

    return maxRow


# concept : first occurence of n, last occurence of n
def lowerBound(arr, target): # index of number greater than or equal to target
    low, high = 0, len(arr) - 1
    ans = len(arr)

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] >= target:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans

def rowsWithMax1sBS(arr):
    maxRow = -1
    maxi = 0
    for i in range(len(arr)):
        idx = lowerBound(arr[i], 1)
        cnt = len(arr[i]) - idx

        if cnt > maxi:
            maxRow = i
            maxi = cnt

    return maxRow


print(rowsWithMax1sBS([[0, 1, 1, 1], [0, 0, 1, 1], [1, 1, 1, 1], [0, 0, 0, 0]]))
