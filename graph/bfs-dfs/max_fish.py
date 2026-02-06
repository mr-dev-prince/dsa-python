def findMaxFish(grid):
    rows, cols = len(grid), len(grid[0])

    vis = [[False for _ in range(cols)] for _ in range(rows)]

    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    max_fish = 0

    def dfs(r, c, cur_total):
        nonlocal rows, cols
        vis[r][c] = True
        cur_total += grid[r][c]
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] > 0:
                if not vis[nr][nc]:
                    dfs(nr, nc, cur_total)
        
        return cur_total
    
    for r in range(rows):
        for c in range(cols):
            if not vis[r][c] and grid[r][c] > 0:
                print(f"r - {r} | c - {c}")
                fish = dfs(r, c, 0)
                print(vis)
                max_fish = max(max_fish, fish)
    
    return max_fish

grid = [[0,2,1,0],[4,0,0,3],[1,0,0,4],[0,3,2,0]]

print(findMaxFish(grid))