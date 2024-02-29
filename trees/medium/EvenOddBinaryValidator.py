# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        queue = [(root,True)]
        while queue:
            current_size = len(queue)
            prev_max = float("-inf")
            prev_min = float("inf")
            for i in range(current_size):
                node,isEven = queue.pop(0)
                if isEven:
                    if node.val > prev_max and node.val%2 != 0:
                        prev_max = node.val
                    else:
                        return False
                else:
                    if node.val < prev_min and node.val %2 ==0:
                        prev_min = node.val
                    else:
                        return False
                if node.left:
                    queue.append((node.left,not isEven))
                if node.right:
                    queue.append((node.right,not isEven))
        return True

        
