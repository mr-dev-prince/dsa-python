from collections import deque
# Breadth First Search // Level-Order Traversal

edgeList = [
    [1, 2],
    [1, 6],
    [2, 1],
    [2, 3],
    [2, 4],
    [3, 2],
    [4, 5],
    [4, 2],
    [5, 4],
    [5, 8],
    [6, 1],
    [6, 7],
    [6, 9],
    [7, 6],
    [7, 8],
    [8, 7],
    [8, 5],
    [9, 6]
]

nodes = set()

for u, v in edgeList:
    nodes.add(u)
    nodes.add(v)

adjList = {node : [] for node in nodes}

for start, end in edgeList:
    adjList[start].append(end)

def bfs(head, adjList):
    q = deque([head])
    vis = set([head])
    ans = []

    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node)

            for nei in adjList[node]:
                if nei not in vis:
                    vis.add(nei)
                    q.append(nei)
                    
        ans.append(level)
    
    print(ans)

bfs(1, adjList)