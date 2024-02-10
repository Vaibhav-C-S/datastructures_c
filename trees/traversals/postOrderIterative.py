class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        stack = []
        answer = []
        prev = None
        
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            
            root = stack[-1]
            
            if not root.right or root.right == prev:
                answer.append(root.val)
                prev = root
                stack.pop()
                root = None
            else:
                root = root.right
                
        return answer
