class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def helper(root,right,level):
            if root is None:
                return
            if level == len(right):
                right.append(root.val)
            helper(root.right,right,level+1)
            helper(root.left,right,level+1)
        right = []
        helper(root,right,0)
        return right
