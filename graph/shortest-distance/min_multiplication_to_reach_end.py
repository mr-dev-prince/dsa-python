# given start and end integers, find the minimum number of multiplications by 2, 3, or 5 needed to reach end from start
from collections import deque

def minMulti(start, end, arr):
    MOD = 10 ** 5

    q = deque([(0, start)]) # tuple of (distance, node)
    dist = [float("inf")] * 10 ** 3
    dist[start] = 0
    
    while q:
        d, node = q.popleft()
        dist[node] = d
        for n in arr:
            mul = (node * n) % MOD
            if d + 1 < dist[mul]:
                dist[mul] = d + 1
                if mul == end : return d + 1
                q.append((d+1, mul)) 
    
    return -1
    

print(minMulti(3, 30, [2, 5, 7]))