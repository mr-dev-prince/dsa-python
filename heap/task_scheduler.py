from collections import Counter, deque
import heapq
from typing import List
# task = A, A, A, B, B, B | n = 2
# A -> idle -> idle -> A -> idle -> idle -> A -> B -> idle -> idle -> B -> idle -> idle -> B
# time = 16
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)

        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        q = deque() # stores pair of [cnt, idleTime]
        time = 0
        while maxHeap or q:
            time += 1
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time

