# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        queue = []
        width = 0
        if root is None: return 0
        queue = [[root,0]]
        while queue:
            current_size = len(queue)
            for i in range(current_size):
                node,number = queue.pop(0)
                if i == 0:
                    first = number
                if i == current_size-1:
                    last = number
                if node.left:
                    queue.append([node.left,2*number+1])
                if node.right:
                    queue.append([node.right,2*number+2])
            width = max(width,last - first+1)
        return width
