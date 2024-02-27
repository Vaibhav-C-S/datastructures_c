'''
class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None
'''

def minVal(root):
    # Write your code here.
    if root is None:
        return -1
    temp = root
    while temp.left:
        temp = temp.left 
    return temp.data
