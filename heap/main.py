import heapq

h = [10, 20, 30, 40]

heapq.heapify(h) # by default min-heap

heapq.heappush(h, 50)
heapq.heappush(h, 5)
heapq.heappush(h, 15)
heapq.heappush(h, 25)

print(heapq.heappop(h))
print(heapq.heappop(h))
print(heapq.heappop(h))

