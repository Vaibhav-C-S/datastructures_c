'''
    Following is the class structure of the BinaryTreeNode class:

    class BinaryTreeNode:
        def __init__(self, data):

            self.data = data
            self.left = None
            self.right = None

'''
from typing import List
def allRootToLeaf(root) -> List[str]:

    result=[]
    path=[]
    root_to_leaf_path(root,path,result)

    return result

def root_to_leaf_path(root,path,result):

    if root is None:

        return 
    path.append(str(root.data))

    root_to_leaf_path(root.left,path,result)
    if root.left is None and root.right is None:

        result.append(" ".join(path))

    root_to_leaf_path(root.right,path,result)
    path.pop()
