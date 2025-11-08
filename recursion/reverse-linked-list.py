# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def helper(node):
            if node.next == None:
                return [node, node]
            
            h, tail = helper(node.next)
            node.next = None
            tail.next = node
            return [h, node]

        if head == None:
            return None
        return helper(head)[0]
        
        