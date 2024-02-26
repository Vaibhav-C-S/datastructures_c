# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        child = 0
        if root.left:
            child+= root.left.val
        if root.right:
            child+= root.right.val
        
        if child == root.val:
            return True
        else:
            return False
        l = self.checkTree(root.left)
        r = self.checkTree(root.right)
        return l and r
        
