import heapq
dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def min_effort(mat):
    rows, cols = len(mat), len(mat[0])

    efforts = [[float("inf")] * cols for _ in range(rows)]

    # (effort, row, col)
    pq = [(0, 0, 0)]
    efforts[0][0] = 0

    while pq:
        diff, row, col = heapq.heappop(pq)

        if row == rows - 1 and col == cols - 1:
            return diff

        if diff > efforts[row][col]:
            continue

        for dr, dc in dir:
            nr, nc = row + dr, col + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                absDiff = abs(mat[row][col] - mat[nr][nc])
                newEffort = max(absDiff, diff)
                if newEffort < efforts[nr][nc]:
                    efforts[nr][nc] = newEffort
                    heapq.heappush(pq, (newEffort, nr, nc))

    return 0

print(min_effort([[1, 2, 2], [3, 8, 2], [5, 3, 5]]))
