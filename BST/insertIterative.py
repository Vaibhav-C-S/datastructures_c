# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node = TreeNode(val)
        if root is None:
            root = node
            return root
        temp = root

        while True:
            if temp.val == val:
                break
            if val < temp.val:
                if temp.left is None:
                    temp.left = node
                    break
                temp = temp.left
            else: #val > temp.val:
                if temp.right is None:
                    temp.right = node
                    break
                temp = temp.right
        return root
