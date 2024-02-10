class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        answer = []
        def helper(root,answer):
            if root is None:
                return
            answer.append(root.val)
            helper(root.left,answer)
            helper(root.right,answer)
        helper(root,answer)
        return answer
