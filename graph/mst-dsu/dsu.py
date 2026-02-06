# Sets whose intersection is null are called Disjoint Set Union

# Every set has a leader/parent

# Operations
    # -> Combine two given sets
    # -> Tell if two members belong to the same set or not [ this is because it is also called 'Union Find Algorithm']

# Element = [a,b,c,d,e,f,g,h] | sets
# Parent = [a,b,c,d,e,f,g,h]  | parent of respective sets

# Union
    # -> when a and b are merged together : lets say a becomes parent of that set
    # -> So, in set (a, b) -> parent is a and a & b belongs to that set

    # -> U(a,b)
    # Element = [a,b,c,d,e,f,g,h]
    # Parent = [a,a,c,d,e,f,g,h]

    # -> U(c,d)
    # Element = [a,b,c,d,e,f,g,h]
    # Parent = [a,a,c,c,e,f,g,h]

    # -> Again if set (a,b) and (c,d) has to be merge -> we make a parent of the set (a,b,c,d)

    # U((a,b), (c,d))
    # -> Element = [a,b,c,d,e,f,g,h] 
    # -> Parent = [a,a,a,a,e,f,g,h]

# Union Find
    # find(a) -> parent -> a
    # find(d) -> parent -> a

# Disjoint Set Union (DSU) -> is a Data-Structure used to implement the above operations

# size
# if size of u is greater the v -> merge v into u's set and increase the size of u | and vice-versa
class SizeDSU:
    def __init__(self, n):
        self.size = []
        self.parent = []

        for i in range(n + 1):
            self.size.append(1) # [1,1,1,..... n times] | size of each set is initially '1'
            self.parent.append(i) # [0,1,2,3,4,...., n] | each element is parent of the set initially

    def findUPar(self, n):
        if self.parent[n] == n:
            return n
        
        self.parent[n] = self.findUPar(self.parent[n])
        return self.parent[n]
    
    def union(self, u, v):
        u_par = self.parent(u)
        v_par = self.parent(v)

        if u_par == v_par : return

        if self.size[u_par] > self.size[v_par]:
            self.parent[v_par] = u_par
            self.size[u_par] += self.size(v_par)
        else:
            self.parent[u_par] = v_par
            self.size[v_par] += self.size(u_par)

# rank
    # if rank is equal -> increment the rank of parent
    # if rank is not equal -> don't increment just make the parent
class RankDSU:
    def __init__(self, n):
        self.rank =  []
        self.parent = []

        for i in range(n + 1):
            self.rank.append(0) # [0,0,0,0.....n times] | We will update the rank with Union operation | initial rank of each node is 0
            self.parent.append(i) # [0,1,2,3,....., n] | We will update the parent of each node when we run find for one node or while creating union.
    
    def findUPar(self, n):
        if self.parent[n] == n:
            return n

        self.parent[n] = self.findUPar(self.parent[n])
        return self.parent[n]

    def union(self, u, v):
        u_par = self.findUPar(u)
        v_par = self.findUPar(v)

        if u_par == v_par : return 

        if self.rank[u_par] > self.rank[v_par]:
            self.parent[v_par] = u_par
        elif self.rank[u_par] < self.rank[v_par]:
            self.parent[u_par] = v_par
        else:
            self.parent[u_par] = v_par
            self.rank[v_par] += 1