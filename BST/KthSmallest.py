# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.result=None
        self.count =0
        def inorder(root,k):
            if root is not None:
                inorder(root.left,k)
                self.count+=1
                if self.count == k:
                    self.result = root.val
                    
                inorder(root.right,k)
            return self.result
        return inorder(root,k)
