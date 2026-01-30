from collections import defaultdict
from disjoint_set import DisjointSet

def accountsMerge(accounts):
    n = len(accounts)

    mp = defaultdict(int)
    ds = DisjointSet(n)
    for i in range(n):
        for j in range(1, len(accounts[i])):
            mail = accounts[i][j]
            if mp.get(mail) == None:
                mp[mail] = i
            else:
                ds.unionBySize(i, mp.get(mail))

    mergedMails = defaultdict(list)
    for mail in mp.keys():
        node = ds.findUPar(mp.get(mail))
        mergedMails[node].append(mail)
    
    ans = []

    for i in range(n):
        if not mergedMails[i] : continue
        tmp = []
        tmp.append(accounts[i][0])
        tmp.extend(mergedMails[i])
        ans.append(sorted(tmp))

    print(ans)

accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]

accountsMerge(accounts)