# representation of undirected graph

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

print(adjList)