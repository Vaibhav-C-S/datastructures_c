def findCeil(root, x):
    if root is None:
        return -1
    
    ceil_val = float('inf')
    while root:
        if root.data == x:
            return root.data
        elif root.data < x:
            root = root.right
        else:
            ceil_val = min(ceil_val, root.data)
            root = root.left

    return ceil_val if ceil_val != float('inf') else -1