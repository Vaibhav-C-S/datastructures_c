#User function Template for python3

# Tree Node
# class Node:
#     def __init__(self, val):
#         self.right = None
#         self.data = val
#         self.left = None

class Solution:
    
    #Function to return a list of nodes visible from the top view 
    #from left to right in Binary Tree.
    def topView(self,root):
        
        # code here
        vertical_traversal ={}
        queue = [[root,0]]
        while queue:
            node,x = queue.pop(0)
            if x in vertical_traversal:
                pass
            else:
                vertical_traversal[x] = node.data
            if node.left:
                queue.append([node.left,x-1])
            if node.right:
                queue.append([node.right,x+1])
        
        top_view = []
        m,n = min(vertical_traversal),max(vertical_traversal)
        for i in range(m,n+1):
            top_view.append(vertical_traversal[i])
        return top_view
