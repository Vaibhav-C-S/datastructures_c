'''
    Following is the structure of Tree Node

    class TreeNode:

        def __init__(self, val):
            self.val = val
            self.left = None
            self.right = None
'''
from typing import List

def postorderTraversal(root) -> List[int]:
	# Write your code here.
    stack1 = []
    stack2 = []
    postOrder = []
    if root is None: return []
    stack1 = [root]
    while stack1:
        node = stack1.pop()
        if node.left is not None:
            stack1.append(node.left)
        if node.right is not None:
            stack1.append(node.right)
        stack2.append(node)
    while stack2:
        postOrder.append(stack2.pop().val)
    return postOrder
