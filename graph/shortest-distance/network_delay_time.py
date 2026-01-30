import heapq
def netDelay(times, n, k):
    # times = [src, target, time]
    # n = nodes
    # k = start point
    adj = {i + 1 : [] for i in range(n)}

    for src, tar, ti in times:
        adj[src].append((tar, ti))

    # minimum time to receive signal from k to all the nodes
    pq = [(0, k)]
    dist = [float("inf")] * (n + 1)
    dist[k] = 0
    while pq:
        time, node = heapq.heappop(pq)

        if time > dist[node]: continue

        for nei, w in adj[node]:
            newTime = time + w
            if newTime < dist[nei]:
                dist[nei] = newTime
                heapq.heappush(pq, (newTime, nei))

    ans = max(dist[1:])
    return ans if ans != float("inf") else -1


# times = [[2,1,1],[2,3,1],[3,4,1]] 
# n = 4
# k = 2

# times = [[1,2,1]]
# n = 2
# k = 1

times = [[1,2,1]]
n = 2
k = 2

print(netDelay(times, n, k))