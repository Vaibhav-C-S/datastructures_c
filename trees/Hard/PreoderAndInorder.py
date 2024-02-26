class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        inorderHash = {}
        for i,j in enumerate(inorder):
            inorderHash[j] = i
        def helper(l,r):
            if l > r:
                return None
            root = TreeNode(preorder.pop(0))
            mid = inorderHash[root.val]
            root.left = helper(l,mid-1)
            root.right = helper(mid+1,r)
            return root
        root = helper(0,len(inorder)-1)
        return root
