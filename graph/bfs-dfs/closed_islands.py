from collections import deque

directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

def closedIslands(grid):
    rows, cols = len(grid), len(grid[0])
    vis = [[False] * cols for _ in range(rows)]
    ans = 0

    def bfs(r, c):
        vis[r][c] = True
        q = deque([(r, c)])
        isClosed = True

        while q:
            row, col = q.popleft()
            
            # isClosed = False if touches border
            if row == 0 or row == rows - 1 or col == 0 or col == cols - 1:
                isClosed = False

            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if grid[nr][nc] == 0 and not vis[nr][nc]:
                        vis[nr][nc] = True
                        q.append((nr, nc))

        return isClosed

    for i in range(rows):
        for j in range(cols):
            if not vis[i][j]:
                if bfs(i,j): ans += 1

    return ans