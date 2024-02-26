class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None
        
        inorderHash = {val: idx for idx, val in enumerate(inorder)}
        
        def helper(l, r):
            if l > r:
                return None
            root = TreeNode(postorder.pop())
            mid = inorderHash[root.val]
            root.right = helper(mid + 1, r)
            root.left = helper(l, mid - 1)
            return root
        
        root = helper(0, len(inorder) - 1)
        return root
