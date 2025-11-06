# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        lo = min(p.val, q.val)
        hi = max(p.val, q.val)

        def helper(node):
            curr = node.val
            if lo == curr or hi == curr:
                return node
            
            if lo < curr and curr < hi:
                return node
            print(curr, lo, hi)

            if curr < lo:
                return helper(node.right)
            else:
                return helper(node.left)

        return helper(root)




        