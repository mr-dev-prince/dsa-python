from collections import defaultdict

def dfs(anc, adj, cur, ans):
    for nei in adj[cur]:
        if len(ans[nei]) == 0 or anc not in ans[nei]:
            ans[nei].append(anc)
            dfs(anc, adj, nei, ans)

def dfs2(src, adj, vis):
    vis[src] = True

    for nei in adj[src]:
        if not vis[nei]:
            dfs2(nei, adj, vis)

def all_ancestors(n, edges):
    adj = defaultdict(list)
    ans = [[] for _ in range(n)]
    # sc - O(V+E)

    for u, v in edges: # O(E)
        adj[u].append(v)

    for i in range(n): # O(V)
        dfs(i, adj, i, ans) # O(V+E)

    return ans

def all_ancestors2(n, edges):
    adj = defaultdict(list)
    ans = [None for _ in range(n)]

    for u, v in edges:
        adj[v].append(u)

    for i in range(n): # O(V)
        anc = []
        vis = [False] * n

        dfs2(i, adj, vis) # O(V+E)

        for j in range(n): # O(V)
            if j == i: continue
            if vis[j]:
                anc.append(j)
        ans[i] = anc

    return ans

# TC = O(V*(V+E))
# approach 1:
# dfs for each node - keep storing src in every node you reach 

# approach 2 :
# reverse directions of each edge

# approach 3: toposort [ in topo folder ]

n = 8
edgeList = [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]]

print(all_ancestors2(n, edgeList))