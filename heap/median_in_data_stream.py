import heapq

class MedianFinder:
    def __init__(self):
        self.left = []   # max heap (negative values)
        self.right = []  # min heap

    def addNum(self, num: int) -> None:
        # Step 1: push to max heap
        heapq.heappush(self.left, -num)

        # Step 2: balance ordering
        heapq.heappush(self.right, -heapq.heappop(self.left))

        # Step 3: balance sizes
        if len(self.right) > len(self.left):
            heapq.heappush(self.left, -heapq.heappop(self.right))

    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return -self.left[0]
        return (-self.left[0] + self.right[0]) / 2