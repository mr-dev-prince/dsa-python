# if you are given co-ordinate and you want to convert into index [ n -> rows | m -> cols ]

mat = [[(0,0), (0,1), (0,2)], [(1,0), (1,1), (1,2)], [(2,0), (2,1), (2,2)]]
n = m = 3

# convert 0-based co-ordinates into 0 -> based indices | Formula -> (row * m) + col
ans = []

for r in mat:
    rows = []
    for row, col in r:
        rows.append((row * m) + col)
    
    ans.append(rows)

print(ans)

# conver 0-based co-ordinates into 1 based indices | Formula -> (row * m) + col + 1
ans2 = []
for r in mat:
    rows = []
    for row, col in r:
        rows.append((row * m) + col + 1)
    
    ans2.append(rows)

print(ans2)