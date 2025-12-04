# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        inorderIndexMap = {}
        x = [0]
        for i, val in enumerate(inorder):
            inorderIndexMap[val] = i

        def buildFromRange(a, b):
            if a == b:
                return None
            
            val = preorder[x[0]]
            x[0] += 1
            res = TreeNode(val)
            split = inorderIndexMap[val]

            res.left = buildFromRange(a, split)
            res.right = buildFromRange(split+1, b)

            return res

        return buildFromRange(0, len(preorder))


        