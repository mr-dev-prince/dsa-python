def spiral(mat):
    n, m = len(mat), len(mat[0])
    l, r = 0, m
    t, b = 0, n

    res = []

    while l < r and t < b:
        # traverse right
        for i in range(l, r):
            res.append(mat[t][i])
        t += 1

        # traverse down
        for i in range(t, b):
            res.append(mat[i][r - 1])
        r -= 1

        if not (l < r and t < b):
            break

        # traverse left
        for i in range(r - 1, l - 1, -1):
            res.append(mat[b - 1][i])
        b -= 1

        # traverse top
        for i in range(b - 1, t - 1, -1):
            res.append(mat[i][l])
        l += 1
    return res


print(spiral([[1,2,3], [4,5,6], [7,8,9]]))
