from os import *
from sys import *
from collections import *
from math import *

# Following is the Binary Tree node structure:
class BinaryTreeNode :
    def __init__(self, data) :
        self.data = data
        self.left = None
        self.right = None

def getTreeTraversal(root):
    # Write your code here.
    if root is None:
        return None
    stack = [[root, 1]]
    preorder = []
    inorder = []
    postorder = []
    while stack:
        node, state = stack[-1]
        if state == 1:
            preorder.append(node.data)
            stack[-1][1] += 1
            if node.left is not None:
                stack.append([node.left, 1])
        elif state == 2:
            inorder.append(node.data)
            stack[-1][1] += 1
            if node.right is not None:
                stack.append([node.right, 1])
        else:
            postorder.append(node.data)
            stack.pop()
    return inorder,preorder,postorder
