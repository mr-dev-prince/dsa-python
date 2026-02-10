def findAllPaths(graph):
    ans = []
    target = len(graph) - 1

    def dfs(node, path):
        if node == target:
            ans.append(list(path))
            return 

        for nei in graph[node]:
            path.append(nei)
            dfs(nei, path)
            # backtracking
            path.pop()
    
    dfs(0, [0])
    return ans