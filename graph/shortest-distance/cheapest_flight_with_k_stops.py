# [[src, des, price]]
import heapq
def shortestFlight(n, src, des, k, mat):
    # build adjlist
    adj = {node : [] for node in range(n)}

    for u, v, p in mat:
        adj[u].append((v, p))
    
    price = [float("inf")] * n
    price[src] = 0

    minheap = [(src, 0)]
    level = 0
    while minheap:
        level += 1
        d, p = heapq.heappop(minheap)

        if p > price[d]: continue

        if level > k + 1 : continue

        for nei, pr in adj[d]:
            if p + pr < price[nei]:
                price[nei] = p + pr
                heapq.heappush(minheap, (nei, p + pr))

    return price[des]

def shortestFlight2(n, src, dst, k, mat):
    adj = {i: [] for i in range(n)}
    for u, v, w in mat:
        adj[u].append((v, w))

    # (cost, node, stops)
    pq = [(0, src, 0)]
    # dist[node][stops] => stores how much cost from src to node with stops
    dist = [[float("inf")] * (k + 2) for _ in range(n)]
    dist[src][0] = 0
    print(dist)

    while pq:
        cost, node, stops = heapq.heappop(pq)

        # if you reached destination return cost | because the next check ensures that there were not more than k stops
        if node == dst:
            return cost

        # ensures the number of stops is less than k
        if stops == k + 1:
            continue

        for nei, w in adj[node]:
            newCost = cost + w
            if newCost < dist[nei][stops + 1]:
                dist[nei][stops + 1] = newCost
                heapq.heappush(pq, (newCost, nei, stops + 1))

    return -1

mat = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]

print(shortestFlight2(4, 0, 3, 1, mat))