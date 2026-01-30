# shortest path between weighted un-directed graph
import heapq
# [[1, 2, 2], [2, 5, 5], [2, 3, 4], [1, 4, 1], [4, 3, 3], [3, 5, 1]]
# [src, des, wt]

def dijkstra_pq(V, edges, src):
    # create adjlist
    adj = {node + 1 : [] for node in range(V)}

    for u, v, w in edges:
        adj[u].append([v, w])

    dis = [float("inf")] * (V + 1)

    dis[src] = 0

    # min-heap : (distance, node)
    pq = [(0, src)]

    while pq:
        curDis, node = heapq.heappop(pq)

        if curDis > dis[node]:
            continue

        for nei, wt in adj[node]:
            newDis = curDis + wt
            if newDis < dis[nei]:
                dis[nei] = newDis
                heapq.heappush(pq, (newDis, nei))

    return dis[1:]

def dijkstra_set(V, edges, src):
    # 1. Create adjacency list
    adj = {i: [] for i in range(V)}
    for u, v, w in edges:
        adj[u].append((v, w))

    # 2. Distance array
    dist = [float("inf")] * V
    dist[src] = 0

    # 3. Set of unvisited nodes
    unvisited = set(range(V))

    while unvisited:
        # pick node with minimum distance from set
        node = min(unvisited, key=lambda x: dist[x])
        unvisited.remove(node)

        # if smallest distance is infinity → unreachable
        if dist[node] == float("inf"):
            break

        # relax neighbors
        for nei, wt in adj[node]:
            if nei in unvisited:
                newDist = dist[node] + wt
                if newDist < dist[nei]:
                    dist[nei] = newDist

    return dist


edges = [[1, 2, 2], [2, 5, 5], [2, 3, 4], [1, 4, 1], [4, 3, 3], [3, 5, 1]]

print(dijkstra_pq(5, edges, 1))

        


