from os import *
from sys import *
from collections import *
from math import *

class TreeNode:
    def __init__(self, data) :
        self.data = data
        self.left = None
        self.right = None

    def __del__(self):
        if self.left:
            del self.left
        if self.right:
            del self.right

def mergeBST(root1, root2):
	# Write your code here.
    def inorder(root,inorderlist):
        if root is None:
            return
        inorder(root.left,inorderlist)
        inorderlist.append(root.data)
        inorder(root.right,inorderlist)
    inorder1 = []
    inorder2 = []
    inorder(root1,inorder1)
    inorder(root2,inorder2)
    def merge(list1,list2):
        i=j = k =  0
        ans = []
        while i < len(list1) and j <len(list2):
            if list1[i] < list2[j]:
                ans.append(list1[i])
                i+=1
            else:
                ans.append(list2[j])
                j+=1 
        while i<len(list1):
            ans.append(list1[i])
            i+=1 
        while j< len(list2):
            ans.append(list2[j])
            j+=1 
        return ans 
    merged_inorder = merge(inorder1,inorder2)
    def create_balance_bst(inorder, l, r):
        if l > r:
            return None
        mid = (l + r) // 2
        root = TreeNode(inorder[mid])
        root.left = create_balance_bst(inorder, l, mid - 1)
        root.right = create_balance_bst(inorder, mid + 1, r)
        return root

    l = 0
    r = len(merged_inorder) - 1  
    balanced_bst_root = create_balance_bst(merged_inorder, l, r)
    
    return balanced_bst_root
