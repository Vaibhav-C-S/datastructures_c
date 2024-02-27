class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def helper(bound, preorder, i):
            if i[0] >= len(preorder) or preorder[i[0]] > bound:
                return None
            
            root = TreeNode(preorder[i[0]])
            i[0] += 1
            root.left = helper(root.val, preorder, i)
            root.right = helper(bound, preorder, i)
            return root
        
        return helper(float('inf'), preorder, [0])
