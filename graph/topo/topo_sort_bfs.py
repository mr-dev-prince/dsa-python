# use queue and in-degree

# in-degree -> no. of incoming edges

# in the queue -> insert all the nodes with indegree 0
from collections import deque

def topo_sort(adjList):
    n = len(adjList)

    indegree = [0] * n
    q = deque()
    topo = []

    for i in range(n):
        for j in range(len(adjList[i])):
            indegree(adjList[i][j]) += 1

    for i in range(n):
        if indegree[i] == 0:
            q.append(i)

    while q:
        curr = q.popleft()
        topo.append(curr)

        for node in adjList[curr]:
            indegree[node] -= 1
            if indegree[node] == 0: 
                q.append(node)

    print(topo)

