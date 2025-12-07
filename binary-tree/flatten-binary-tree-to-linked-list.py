# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def helper(tree, end):
            if tree.right is not None:
                end = helper(tree.right, end)

            if tree.left is not None:
                end = helper(tree.left, end)
                tree.left = None
            tree.right = end
            return tree
            
        if root is None:
            return
        helper(root, None)
        