directions = [(1,0), (-1, 0), (0, -1), (0, 1)]

def dfs(image, sr, sc, orgCol, col):
    if image[sr][sc] != orgCol:
        return

    image[sr][sc] = col

    for dr, dc in directions:
        nr, nc = sr + dr, sc + dc
        if 0 <= nr < len(image) and 0 <= nc < len(image[0]):
            dfs(image, nr, nc, orgCol, col)

def helper(image, sr, sc, col):
    orgCol = image[sr][sc]

    if orgCol == col:
        return image
    
    dfs(image, sr, sc, orgCol, col)

    return image
