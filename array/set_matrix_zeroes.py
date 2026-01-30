def setZeroes(mat):
    rows, cols = len(mat), len(mat[0])
    rowZero = False

    # determine which rows/cols need to be zero
    for r in range(rows):
        for c in range(cols):
            if mat[r][c] == 0:
                mat[0][c] == 0
                if r > 0:
                    mat[r][0] = 0
                else:
                    rowZero = True

    for r in range(1, rows):
        for c in range(1, cols):
            if mat[0][c] == 0 or mat[r][0] == 0:
                mat[r][c] = 0
    
    if mat[0][0] == 0:
        for r in range(rows):
            mat[r][0] = 0

    if rowZero:
        for c in range(cols):
            mat[0][c] = 0
