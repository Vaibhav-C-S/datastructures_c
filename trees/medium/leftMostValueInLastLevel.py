class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return -1
        if root.left is None and root.right is None:
            return root.val
        queue = [root]
        left = -1
        while queue:
            current_size = len(queue)
            current_level = []
            for i in range(current_size):
                node = queue.pop(0)
                if i == 0:
                    left = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            

        return left


