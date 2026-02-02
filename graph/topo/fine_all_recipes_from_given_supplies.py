from collections import defaultdict, deque

def find_recipes(recipes, ingredients, supplies):
    adj = defaultdict(list)
    indegree = [0] * len(recipes)

    for i in range(len(recipes)):
        for ing in ingredients[i]:
            if ing not in supplies:
                adj[ing].append(i)
                indegree[i] += 1

    q = deque()

    for i in range(len(indegree)):
        if indegree[i] == 0:
            q.append(i)

    result = []

    while q:
        i = q.popleft
        result.append(recipes[i])

        for nei in adj[recipes[i]]:
            indegree[nei] -= 1

            if indegree[nei] == 0:
                q.append(nei)

    return result