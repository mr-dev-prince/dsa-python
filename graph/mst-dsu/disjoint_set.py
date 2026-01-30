# find if two nodes exist in graph in constant time

# findParent() | union() by rank and size

class DisjointSet:
    def __init__(self, n):
        self.rank = []
        self.parent = []
        self.size = []
        for i in range(n + 1):
            self.rank.append(0)
            self.parent.append(i)
            self.size.append(1)

    def findUPar(self, node):
        if node == self.parent[node]: return node

        # path compression
        self.parent[node] = self.findUPar(self.parent[node])
        return self.parent[node]
    
    def unionByRank(self, u, v):
        up_u = self.findUPar(u)
        up_v = self.findUPar(v)

        if up_u == up_v: return 

        if self.rank[up_u] < self.rank[up_v]:
            self.parent[up_u] = up_v
        elif self.rank[up_v] < self.rank[up_u]:
            self.parent[up_v] = up_u
        else:
            self.parent[up_v] = up_u
            self.rank[up_u] += 1

    def unionBySize(self, u, v):
        up_u = self.findUPar(u)
        up_v = self.findUPar(v)

        if up_u == up_v: return 

        if self.size[up_u] < self.size[up_v]:
            self.parent[up_u] = up_v
            self.size[up_v] += self.size[up_u]
        else:
            self.parent[up_v] = up_u
            self.size[up_u] += self.size[up_v]

# ds = DisjointSet(7)

# ds.unionBySize(1, 2)
# ds.unionBySize(2, 3)
# ds.unionBySize(4, 5)
# ds.unionBySize(6, 7)
# ds.unionBySize(5, 6)

# if ds.findUPar(3) == ds.findUPar(7):
#     print("Same")
# else: print("Not Same")

# ds.unionBySize(3, 7)

# if ds.findUPar(3) == ds.findUPar(7):
#     print("Same")
# else: print("Not Same")