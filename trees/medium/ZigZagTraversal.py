# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        stack1 = []
        stack2 = []
        result =[]
        if root is None:
            return []
        stack1.append(root)
        
        while stack1 or stack2:
            temp1 =[]
            while stack1:
                node = stack1.pop()
                temp1.append(node.val)
                if node.left:
                    stack2.append(node.left)
                if node.right:
                    stack2.append(node.right)
            
            if temp1:
                result.append(temp1)
            temp1 = []
            while stack2:
                node = stack2.pop()
                temp1.append(node.val)
                if node.right:
                    stack1.append(node.right)
                if node.left:
                    stack1.append(node.left)
            if temp1:
                result.append(temp1)
        return result
