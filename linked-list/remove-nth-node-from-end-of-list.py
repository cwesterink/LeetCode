# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def helper(p):
            if p == None:
                return 0

            ll = helper(p.next)
            if (ll== n):
                print(p)
                p.next = p.next.next
            return 1 + ll
        
        if head.next == None:
            return None
        
        l = helper(head)
        if l == n:
            return head.next

        return head

    
        

        