# Definition for a binary tree root.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def minimum(node):
            while node.left:
                node = node.left
            return node 
        def helper(root,key):
            if root is None:
                return None
            if key < root.val:
                root.left = helper(root.left,key)
            elif key > root.val:
                root.right = helper(root.right,key)
            else: 
                if root.left is None:
                    return root.right
                elif root.right is None:
                    return root.left
                else:
                    subtree_min = minimum(root.right)
                    root.val = subtree_min.val 
                    root.right = helper(root.right,subtree_min.val)
            return root
        
        return helper(root,key)


        
