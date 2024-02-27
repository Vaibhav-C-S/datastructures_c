def findFloor(root, x):
    if root is None:
        return -1
    
    floor_val = -1  # Initialize to a default value
    while root:
        if root.data == x:
            return root.data
        elif root.data > x:
            root = root.left
        else:
            floor_val = max(floor_val, root.data)
            root = root.right

    return floor_val