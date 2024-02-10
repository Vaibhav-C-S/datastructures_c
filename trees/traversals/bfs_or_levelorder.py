
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        queue = []
        result = []
        if root is None:
            return []
        queue = [root]
        while queue:
            current_size = len(queue)
            current_level = []
            for _ in range(current_size):
                node = queue.pop(0)
                current_level.append(node.val)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            print(current_level)
            result.append(current_level)
        return result
        
