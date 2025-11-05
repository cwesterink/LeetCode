# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        return self.validator(root, None, None)
    
    def validator(self, root, minVal, maxVal):
        if (root == None):
            return True
        if (maxVal != None and root.val >= maxVal) or (minVal != None and root.val <= minVal):
            return False
        
        return self.validator(root.left, minVal, root.val) and self.validator(root.right, root.val, maxVal)