def rotate(mat):
    l, r = 0, len(mat) - 1
    
    while l < r:
        for i in range(r - l):
            top, bottom = l, r

            # save top-left
            topLeft = mat[top][l + i]

            # move bottom left to top left
            mat[top][l + i] = mat[bottom - i][l]

            # move bottom right into bottom left
            mat[bottom - i][l] = mat[bottom][r - i]

            # move top right into bottom right
            mat[bottom][r-i] = mat[top + i][r]

            # move top left into top right
            mat[top + i][r] = topLeft

        r -= 1
        l += 1