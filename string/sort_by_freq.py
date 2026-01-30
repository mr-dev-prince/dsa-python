from collections import defaultdict
import heapq
def sortStr(s):
    freq = defaultdict(int)

    for ch in s:
        freq[ch] += 1

    mh = []

    for key, val in freq.items():
        heapq.heappush(mh, (-val, key))
    
    print(mh)
    ans = []
    while mh:
        val, key = heapq.heappop(mh)
        for _ in range(val * -1):
            ans.append(key)
    print("".join(ans))

sortStr("bbAa")
