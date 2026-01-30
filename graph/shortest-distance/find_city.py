import heapq
def findCity(n, edges, k):
    # build adj

    adj = {i: [] for i in range(n)}

    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))

    def dijkstra(src):
        dist = [float("inf")] * n
        dist[src] = 0

        pq = [(0, src)]

        while pq:
            d, node = heapq.heappop(pq)

            if d > dist[node]: continue

            for nei, wt in adj[node]:
                nd = d + wt
                if nd < dist[nei]:
                    dist[nei] = nd
                    heapq.heappush(pq, (nd, nei))

        return dist
    
    ans = -1 
    minReach = float("inf")

    for city in range(n):
        dist = dijkstra(city)
        reachable = sum(1 for d in dist if d <= k)

        # tie -> choose largest
        if reachable <= minReach:
            minReach = reachable
            ans = city

    return ans

n = 4
edges = [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]]
k = 4

findCity(n, edges, k)
