import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        k = len(lists)
        def popHead(i):
            head = lists[i]
            lists[i] = head.next
            return head

        heap = []
        for i in range(k):
            if lists[i] != None:
                heap.append((lists[i].val, i))
        heapq.heapify(heap)

        head = p = ListNode(-1)

        while heap:
            val, i = heapq.heappop(heap)

            p.next = popHead(i)
            p = p.next
            
            nextInLine = lists[i]
            if nextInLine != None:
                heapq.heappush(heap, (nextInLine.val, i))

        return head.next


        