from disjoint_set import DisjointSet

# minimum spanning tree
# n - nodes | m - edges


# a tree in which we have n nodes and n-1 edges and all nodes are reachable from each other and sum of edge weights is minimum of all the MST that can be drawn for that graph

# PRIM's Algorithm
  # DS required -> priority queue (wt, node, parent), visisted array
  # 
# Kruskal's Algorithm
import heapq

def prims(V, edges):
    adj = {i: [] for i in range(V)}
    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))

    # Min heap: (weight, node)
    pq = [(0, 0)]
    visited = [False] * V   # ✅ size must be V

    total = 0
    count = 0

    while pq and count < V:
        wt, node = heapq.heappop(pq)

        if visited[node]:
            continue

        visited[node] = True
        total += wt
        count += 1

        for nei, w in adj[node]:
            if not visited[nei]:
                heapq.heappush(pq, (w, nei))

    return total

def kruskal(V, edges):
    edges.sort(key=lambda x: x[2])

    ds = DisjointSet(V)
    mstWt = 0
    count = 0

    # 2. Pick smallest edges that don't form a cycle
    for u, v, w in edges:
        if ds.findUPar(u) != ds.findUPar(v):
            ds.unionBySize(u, v)
            mstWt += w
            count += 1
            if count == V - 1:
                break

    return mstWt

print(kruskal(3, [[0, 1, 5], [1, 2, 3], [0, 2, 1]]))
