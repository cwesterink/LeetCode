# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        seen = set()

        p = head
        while p != None:
            if p in seen:
                return True
            
            seen.add(p)
            p = p.next
        return False
        