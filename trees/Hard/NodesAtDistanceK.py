from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        levels = {}
        parent_track = {}
        queue = [(root, None)]  
        while queue:
            node, parent = queue.pop(0)
            if node:
                parent_track[node] = parent
                if node.left:
                    queue.append((node.left, node))
                if node.right:
                    queue.append((node.right, node))

       
        queue = [(target, 0)]
        visited = set()
        ans = []
        while queue:
            node, distance = queue.pop(0)
            visited.add(node)
            if distance == k:
                ans.append(node.val)
            elif distance > k:
                break
            else:
                if node.left and node.left not in visited:
                    queue.append((node.left, distance + 1))
                if node.right and node.right not in visited:
                    queue.append((node.right, distance + 1))
                parent = parent_track[node]
                if parent and parent not in visited:
                    queue.append((parent, distance + 1))

        return ans
