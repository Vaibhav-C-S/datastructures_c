# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        def helper(p,q):
            if p is None or q is None:
                return p==q
            return p.val == q.val and helper(p.left,q.right) and helper(p.right,q.left)
        
        return helper(root,root)
        
        
