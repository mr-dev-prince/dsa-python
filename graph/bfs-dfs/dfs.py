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

def dfs(node, adjList, vis, li):
    vis[node] = 1
    li.append(node)
    for nei in adjList[node]:
        if not vis[nei]:
            dfs(nei, adjList, vis, li)


def helper(start, adjList):
    vis = [0 for _ in range(len(adjList) + 1)] # if 0 based else len(adjList) + 1
    li = []
    dfs(start, adjList, vis, li)
    print(li)

helper(1, adjList)