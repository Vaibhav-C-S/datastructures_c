# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def height(root):
            if root is None:
                return 0
            left = height(root.left)
            right = height(root.right)
            return 1+ max(left,right)
        if root is None:
            return True
        left = height(root.left)
        right = height(root.right)
        if abs(left - right) > 1:
            return False
        else:
            return  self.isBalanced(root.left) and self.isBalanced(root.right)

# time = O(n) * O(n) which is o(n^2) as o(n) to check height at each node, o(n) to call and use the height function
# -----------------------------------------
# not efficient,use o(n),elimate height funciton from above
# concept: use the height function only, but instead return -1 if tree is unbalanced and the original height is balanced,can be done using two check conditions
# if left == -1 or right == -1: return -1
# if abs(left - right) > 1: return -1
# and finally
# return height(root) != -1 
# ---------------------------
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def height(root):
            if root is None:
                return 0
            left = height(root.left)
            right = height(root.right)
            if left == -1 or right == -1: return -1
            if abs(left - right) > 1: return -1
            return 1 + max(left,right)
        return height(root) != -1 
        
