# [baa, abcd, abca, cab, cad]
from collections import deque, defaultdict

def alien_dictionary(words):
    adj = defaultdict(set)
    indegree = {}
    
    for word in words:
        for ch in word:
            indegree[ch] = 0

    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i + 1]

        if len(w1) > len(w2) and w1.startswith(w2):
            return "" # invalid case
        
        for j in range(min(len(w1), len(w2))):
            if w1[j] != w2[j]:
                if w2[j] not in adj[w1[j]]:
                    adj[w1[j]].add(w2[j])
                    indegree[w2[j]] += 1
                break


    q = deque([c for c in indegree if indegree[c] == 0])
    topo = []
    
    while q:
        k = q.popleft()
        topo.append(k)

        for nei in adj[k]:
            indegree[nei] -= 1

            if indegree[nei] == 0:
                q.append(nei)

    return topo if len(topo) == len(indegree) else ""
    
print(alien_dictionary(["baa", "abcd", "abca", "cab", "cad"]))
            

