from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        inorder = []
        cur = root
        while cur:
            if cur.left is None:
                inorder.append(cur.val)
                cur = cur.right
            else:
                prev = cur.left
                while prev.right and prev.right is not cur:
                    prev = prev.right
                if prev.right is None:
                    prev.right = cur
                    cur = cur.left
                else:
                    prev.right = None
                    inorder.append(cur.val)
                    cur = cur.right
        return inorder
