from typing import List
import heapq

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        n, m = len(moveTime), len(moveTime[0])

        # Correct initialization to avoid shared references
        dis = [[float("inf") for _ in range(m)] for _ in range(n)]
        dis[0][0] = 0

        # Heap stores: (current_time, row, col)
        mh = [(0, 0, 0)]

        while mh:
            t, x, y = heapq.heappop(mh)

            # Standard Dijkstra check: skip if we've found a better path already
            if t > dis[x][y]:
                continue

            if x == n - 1 and y == m - 1:
                return t

            for dr, dc in directions:
                nr, nc = x + dr, y + dc
                if 0 <= nr < n and 0 <= nc < m:
                    # You can only enter the cell at max(current_time, cell_open_time)
                    # and it takes 1 second to actually cross into it.
                    arrival_time = max(t, moveTime[nr][nc]) + 1
                    
                    if arrival_time < dis[nr][nc]:
                        dis[nr][nc] = arrival_time
                        heapq.heappush(mh, (arrival_time, nr, nc))

        return -1 # Should not be reached based on problem constraints

        