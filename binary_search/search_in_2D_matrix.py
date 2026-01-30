# sorted row-wise
def search(mat, key):
    c, r = len(mat[0]), len(mat)
    # the idea is to think of the given matrix as a flattened array of sorted numbers - because
    # in the question it is given that each row will be sorted and each column's first element will be greater than last element of column before it

    # [1,2]     -> this is a 2x2 matrix -> flattening it gives - [1,2,3,4]
    # [3,4]     -> now we can run a Binary search over it. 

    # we will not flatten it in real life but we will think of it as a flattened array
    # arr ---> [1,2,3,4]
    # indices -> 0, 1, 2, 3

    # with this indices we will find out at what co-ordinate the index appear

    # row = index / c -> because each row has 'c' elements and for each row 'c' elements have been passed
    # col = index % c -> because before each column multiple of c elements have passed

    # if index is 2 -> [ row = 2/2 -> 1 | col = 2%2 -> 1 ] --> so the index 2 appears at [1,1] co-ordinate and this is true for every index

    total_elem = c * r
    l, r = 0, total_elem - 1

    while l <= r:
        mid = (l + r) // 2

        row = mid // c
        col = mid % c

        elem = mat[row][col]

        if elem == key:
            return True
        elif elem > key:
            r = mid - 1
        else:
            l = mid + 1
    
    return False

# sorted row-wise and col-wise
def search2(matrix, target):
    c, r = len(matrix[0]), len(matrix)
        
    sr, sc = 0, c - 1
    while sr < r and sc >= 0:
        elem = matrix[sr][sc]
        if elem == target: return True
        elif elem > target: sc -= 1
        else : sr += 1
    
    return False