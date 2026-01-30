# representation of graph

# you will be given edgeList which you will have to change to adjList

#  edges are in form- [from, to] | [0, 1] means -> there is a edge [ from 0 to 1 ]

# naive/manual way --->

edgeList = [
    [0,1], 
    [0,3], 
    [1,2], 
    [3,4], 
    [3,6], 
    [3,7], 
    [4,5], 
    [4,2], 
    [5,2]
]

adjList = {}

for start, end in edgeList:
    if start in adjList:
        adjList[start].append(end)
    else:
        adjList[start] = [end]

print(adjList)

# intermediate/better way --->

from collections import defaultdict

adjList2 = defaultdict(list)

for start, end in edgeList:
    adjList2[start].append(end)

print(dict(adjList2))

# include nodes with no outgoing-edges

nodes = set()

for u, v in edgeList:
    nodes.add(u)
    nodes.add(v)

adjList3 = {node : [] for node in nodes}

for start, end in edgeList:
    adjList3[start].append(end)

print(adjList3)