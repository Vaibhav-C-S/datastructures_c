# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def findleftheight(root):
            node = root
            height = 0
            while node:
                node= node.left
                height += 1
            return height
        def findrightheight(root):
            node = root
            height = 0
            while node:
                node = node.right
                height +=1
            return height 
        if root is None:
            return 0
        lh = findleftheight(root)
        rh = findrightheight(root)
        if lh == rh : return (1<<lh) -1 
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
    
        
