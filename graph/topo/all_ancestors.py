from collections import defaultdict, deque

def all_ancestors(n, edges):
    adj = defaultdict(list)
    indegree = [0] * n
    q = deque()

    # step 1 : create indegree and adjlist
    for u, v in edges:
        adj[u].append(v)
        indegree[v] += 1
    
    # step 2 : enqueue all the nodes with indegree 0 | means they are ancestors of some node
    for i in range(n):
        if indegree[i] == 0:
            q.append(i)

    topo = []

    # step 3 : find out topological order of nodes
    while q:
        curr = q.popleft()
        topo.append(curr)

        for v in adj[curr]:
            indegree[v] -= 1
            if indegree[v] == 0:
                q.append(v)
    
    tmp = defaultdict(set)
    
    # step 4 : store ancestors for each node 
    for node in topo:
        for nei in adj[node]:
            tmp[nei].add(node) # add node ancestor
            for ancs in tmp[node]: # add ancestors of node
                tmp[nei].add(ancs)

    res = [None for _ in range(n)]

    # step 5 : build the result
    for i in range(n):
        res[i] = sorted(tmp[i])

    return res
    

n = 8
edgeList = [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]]

print(all_ancestors(n, edgeList))