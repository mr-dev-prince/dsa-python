def nextPermutation(arr):
    n = len(arr)

    # 1) find the dip
    dip = -1
    for i in range(n - 2, -1, -1):
        if arr[i] < arr[i + 1]:
            dip = i
            break

    # 2) if no dip, reverse whole array
    if dip == -1:
        arr.reverse()
        return arr

    # 3) find just greater element than arr[dip]
    for i in range(n - 1, dip, -1):
        if arr[i] > arr[dip]:
            arr[i], arr[dip] = arr[dip], arr[i]
            break

    # 4) reverse the right part
    arr[dip + 1:] = reversed(arr[dip + 1:])

    return arr
