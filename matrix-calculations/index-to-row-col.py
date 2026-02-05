# if you are given indices of a matrix and the number of rows (n) and number of columns (m) : you can find the co-ordinates

# 0 - Based Indexing | 0 - based co-ordinates
    # -> row = index // m
    # -> col = index % m

# 1 - Based Indexing | 0 - based co-ordinates
    # -> row = index - 1 // m
    # -> col = index - 1 % m

mat = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
n = 4
m = 4

# change indices to matrix

ans = []
rows = []

for i in range(len(mat)):
    row = mat[i] // m
    col = mat[i] % m
    rows.append((row, col)) 
    if len(rows) == n:
        ans.append(rows)
        rows = []


mat2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]      

ans2 = []
rows2 = []

for i in range(len(mat2)):
    row = ((mat2[i] - 1) // m)
    col = ((mat2[i] - 1) % m)
    rows2.append((row, col))
    if len(rows2) == n:
        ans2.append(rows2)
        rows2 = []

print(ans2)