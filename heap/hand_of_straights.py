from collections import Counter
import heapq

def solve(hand, n):
    if len(hand) % n:
        return False
    
    count = Counter(hand) # creates frequency map

    # count = {}
    # for n in hand:
    #     count[n] = 1 + count.get(n, 0)

    minHeap = list(count.keys()) # create heap with unique elements
     
    heapq.heapify(minHeap)

    while minHeap:
        first = minHeap[0]

        for i in range(first, first + n):
            if i not in count:
                return False
            count[i] -= 1
            if count[i] == 0:
                if i != minHeap[0]:
                    return False
                heapq.heappop(minHeap)

    return True


