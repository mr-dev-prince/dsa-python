from collections import defaultdict, deque

def ladderLengthNeetCode(bw, ew, wl):
    if not ew in wl:
        return 0

    nei =  defaultdict(list)

    wl.append(bw)

    for w in wl:
        for j in range(len(w)):
            pattern = w[:j] + "*" + w[j+1:]
            nei[pattern].append(w)

    vis = set([bw])

    q = deque([bw])

    res = 1

    while q:
        for _ in range(len(q)):
            word = q.popleft()
            if word == ew:
                return res
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                for neiWord in nei[pattern]:
                    if neiWord not in vis:
                        vis.add(neiWord)
                        q.append(neiWord)

        res += 1

    return 0

def ladderLengthStriver(bw, ew, wl):
    if ew not in wl:
            return 0

    wordSet = set(wl)
    q = deque([(bw, 1)])

    while q:
        word, steps = q.popleft()

        if word == ew:
            return steps

        for i in range(len(word)):
            for c in range(26):
                new_word = (
                    word[:i] +
                    chr(ord('a') + c) +
                    word[i+1:]
                )

                if new_word in wordSet:
                    wordSet.remove(new_word)
                    q.append((new_word, steps + 1))

    return 0



