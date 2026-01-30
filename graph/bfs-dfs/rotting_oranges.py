from collections import deque

def oranges_rotting(grid):
    # 2 - rotten | 1 - fresh | 0 - no orange
    row, col = len(grid), len(grid[0])
    fresh = 0
    q = deque()
    minutes = 0

    for i in range(row):
        for j in range(col):
            if grid[i][j] == 2:
                #rotten
                q.append((i, j))
            elif grid[i][j] == 1:
                # fresh
                fresh += 1

    directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]

    while q and fresh > 0:
        for _ in range(len(q)):
            r, c = q.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == 1:
                    fresh -= 1
                    grid[nr][nc] = 2
                    q.append((nr, nc))
        minutes += 1