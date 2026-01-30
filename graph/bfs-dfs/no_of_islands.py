from collections import deque

directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

def numIslands(grid):
    rows, cols = len(grid), len(grid[0])
    ans = 0
    vis = [[False] * cols for _ in range(rows)]
    
    def bfs(r, c):
        q = deque([(r, c)])
        while q:
            row, col = q.popleft()
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if 0 <= nr < rows and 0 <= nc < cols and not vis[nr][nc] and grid[nr][nc] == "1":
                    vis[nr][nc] = True
                    q.append((nr, nc))

    for i in range(rows):
        for j in range(cols):
            if not vis[i][j] and grid[i][j] == "1":
                ans += 1
                vis[i][j] = True 
                bfs(i, j)

    return ans

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

print(numIslands(grid))
