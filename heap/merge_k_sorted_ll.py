from typing import List, Optional
import heapq

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        
        minHeap = []
        heapq.heapify(minHeap)

        for i in range(len(lists)):
            head = lists[i]
            while head:
                heapq.heappush(minHeap, head.val)
                head = head.next

        dummy = ListNode()
        tmp = dummy
        while minHeap:
            newNode = ListNode(heapq.heappop(minHeap))
            tmp.next = newNode
            tmp = tmp.next

        return dummy.next

        # while len(lists) > 1:
        #     anslist = []

        #     for i in range(0, len(lists), 2):
        #         l1 = lists[i]
        #         l2 = lists[i + 1] if (i + 1) < len(lists) else None
        #         anslist.append(self.mergeLists(l1, l2))
        #     lists = anslist
        # return lists[0]
    
    # def mergeLists(self, l1, l2):
    #     dummy = ListNode()
    #     tail = dummy

    #     while l1 and l2:
    #         if l1.val > l2.val:
    #             tail.next = l2
    #             l2 = l2.next
    #         else:
    #             tail.next = l1
    #             l1 = l1.next
    #         tail = tail.next
    #     if l1:
    #         tail.next = l1
    #     if l2:
    #         tail.next = l2
        
    #     return dummy.next
            