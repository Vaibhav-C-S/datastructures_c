# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxi = -1
        
        def height(root, maxi):
            
            if root is None:
                return 0
            left = height(root.left, maxi)
            right = height(root.right, maxi)
            self.maxi = max(self.maxi, left + right)
            return 1 + max(left, right)
        
        height(root, self.maxi)
        return self.maxi
----------------
this is O(n),o(n2) would be calling the height funciton every time
------------

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        maxi = -1
        
        def height(root):
            nonlocal maxi
            if root is None:
                return 0
            left = height(root.left)
            right = height(root.right)
            maxi = max(maxi, left + right)
            return 1 + max(left, right)
        
        height(root)
        return maxi

----------
use of nonlocal ,only for python3
