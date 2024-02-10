# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        answer = []
        def helper(root,answer):
            if root is None:
                return
            helper(root.left,answer)
            answer.append(root.val)
            helper(root.right,answer)
        helper(root,answer)
        return answer
        
