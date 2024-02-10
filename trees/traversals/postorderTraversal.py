# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        answer = []
        def helper(root,answer):
            if root is None:
                return
            helper(root.left,answer)
            
            helper(root.right,answer)
            answer.append(root.val)
        helper(root,answer)
        return answer
        
