# in kahn's algorithm - we saw the concept of indegree
# if the graph is a DAG we will find out that at the end the indegree of every node is 0
# but if it is a DCG [ Directed Cyclic Graph ] the indegree of one node will be non-zero.

# we will use that to our advantage to tell if there is a cycle in the given graph or not
from collections import deque

def kahn(adjList):
    n = len(adjList)
    # topo = []
    cnt = 0
    indegree = [0] * n
    q = deque()
    for i in range(n):
        for j in range(len(adjList[i])):
            indegree[adjList[i][j]] += 1

    
    for i in range(n):
        if indegree[i] == 0:
            q.append(i)

    while q:
        curr = q.popleft()
        cnt += 1
        # topo.append(curr)

        for node in adjList[curr]:
            indegree[node] -= 1

            if indegree[node] == 0:
                q.append(node)

    if cnt == n:
        return True
    return False