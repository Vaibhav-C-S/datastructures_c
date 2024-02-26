# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        parent_track = {}
        queue = [(root,None)]
        target = None
        while queue:
            node,parent = queue.pop(0)
            if node.val == start:
                target = node
            if node:
                parent_track[node] = parent
                if node.left:
                    queue.append((node.left,node))
                if node.right:
                    queue.append((node.right,node))
        if target is None:
            return 0
        queue = [(target,0)]
        visited = set()
        max_distance = 0
        while queue:
            node,k = queue.pop(0)
            visited.add(node)
            max_distance= max(max_distance,k)
            if node.left and node.left not in visited:
                queue.append((node.left,k+1))
            if node.right and node.right not in visited:
                queue.append((node.right,k+1))
                
            parent = parent_track[node]
            if parent and parent not in visited:
                queue.append((parent,k+1))
               
    
        return max_distance
        
