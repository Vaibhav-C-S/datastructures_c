
'''

    ------- Binary Tree node structure -------
            class TreeNode :
                def __init__(self, data) :
                    self.data = data
                    self.left = None
                    self.right = None

'''

class BSTInfo:
    def __init__(self, size, is_bst, min_val, max_val):
        self.size = size
        self.is_bst = is_bst
        self.min_val = min_val
        self.max_val = max_val

def largestBST(root):
    def postorder(node):
        if not node:
            return BSTInfo(0, True, float('inf'), float('-inf'))
        
        left_info = postorder(node.left)
        right_info = postorder(node.right)
        
        if left_info.is_bst and right_info.is_bst and left_info.max_val < node.data < right_info.min_val:
            size = left_info.size + right_info.size + 1
            return BSTInfo(size, True, min(left_info.min_val, node.data), max(right_info.max_val, node.data))
        else:
            return BSTInfo(max(left_info.size, right_info.size), False, 0, 0)
    
    return postorder(root).size
