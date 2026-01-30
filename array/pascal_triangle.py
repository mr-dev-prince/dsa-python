def pascal(n):
    ans = []
    for i in range(n):
        curRow = []
        for j in range(i+1):
            if j == 0 or j == i:
                curRow.append(1)
            else:
                curRow.append(ans[i-1][j-1] + ans[i-1][j])
        ans.append(curRow)
    
    return ans

