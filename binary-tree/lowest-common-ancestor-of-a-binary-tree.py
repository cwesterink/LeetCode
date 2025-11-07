# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        a, b = p.val, q.val

        def helper(node):
            if node == None:
                return None

            val= node.val
            if val==a or val==b:
                return node

            resL = helper(node.left)
            resR = helper(node.right)

            if resR != None and resL != None:
                return node

            if resR != None:
                return resR
            return resL

        return helper(root)
                


        