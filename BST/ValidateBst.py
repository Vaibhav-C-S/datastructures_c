class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(root, left, right):
            if root is None:
                return True
            if not (left < root.val < right):
                return False
            l = helper(root.left, left, root.val)
            r = helper(root.right, root.val, right)
            return l and r
        
        left = float('-inf')
        right = float('inf')
        return helper(root, left, right)
