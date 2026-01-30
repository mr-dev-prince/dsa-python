adjMat = [
    [1,1,0],
    [1,1,0],
    [0,0,1]
]

n = len(adjMat)

adjList = {node + 1: [] for node in range(n)}

for i in range(n):
    for j in range(n):
        if adjMat[i][j] and i != j:
            adjList[i + 1].append(j + 1)

print(adjList)