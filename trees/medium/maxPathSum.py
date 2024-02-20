# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxi = float('-inf')
        def helper(root):
            nonlocal maxi
            if root is None:
                return 0
            left_sum = max(0,helper(root.left))
            right_sum = max(0,helper(root.right))
            maxi  = max(maxi,root.val+left_sum+right_sum)
            return root.val + max(left_sum,right_sum)
        helper(root)
        return maxi
