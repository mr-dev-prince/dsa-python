# Topological Sorting only Exist on DAG - Directed Acyclic Graph
# Can also be used to determine if a directed Graph has cycle or not

# intuition : use stack 

def dfs(graph, vis, src, st):
    vis[src] = 1

    for node in graph[src]:
        if not vis[node]:
            dfs(graph, vis, node, st)
    st.append(src)

def topo_sort(graph):
    n = len(graph)
    st = []
    vis = [0] * n

    for i in range(n):
        if not vis[i]:
            dfs(graph, vis, i, st)
    
    ans = []
    while st:
        ans.append(st.pop())

    print(ans)

graph = [[], [], [3], [1], [0,1], [0,2]]

topo_sort(graph)