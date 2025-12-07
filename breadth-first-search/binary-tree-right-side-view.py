from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        queue = deque([root])
        res = []
        while len(queue) > 0:
            last = None
            for i in range(len(queue)):
                last = queue.popleft()
                if last.left is not None:
                    queue.append(last.left)
                if last.right is not None:
                    queue.append(last.right)
            res.append(last.val)
        return res


            

        

        