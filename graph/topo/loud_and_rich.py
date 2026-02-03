from collections import defaultdict, deque

def loud_and_rich(richer, quiet):
    adj = defaultdict(list)
    indegree = [0] * len(quiet)

    for u, v in richer:
        adj[u].append(v)
        indegree[v] += 1

    q, res = deque([i for i, v in enumerate(indegree) if v == 0]), list(range(len(quiet)))

    while q:
        node = q.popleft()

        for nei in adj[node]:
            if quiet[res[node]] < quiet[res[nei]]:
                res[nei] = res[node]
            
            indegree[nei] -= 1
            if indegree[nei] == 0:
                q.append(nei)

    
    return res