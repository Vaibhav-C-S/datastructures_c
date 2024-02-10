# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None: return 0
        left = self.maxDepth(root.left)
        right =  self.maxDepth(root.right)   
    

        return 1 + max(left,right)       

-------
time = O(n)
space = auxillary O(n)
