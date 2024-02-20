#User function Template for python3

'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:
    def getleafnodes(self,root,dfs):
        if root is None:
            return
        self.getleafnodes(root.left,dfs)
        if root.left is None and root.right is None:
            dfs.append(root.data)
        self.getleafnodes(root.right,dfs)
        
    def printBoundaryView(self, root):
        # Code here
        left = []
        right = []
        if root is None:
            return []
        elif root.left is None and root.right is None:
            return [root.data]
            
            
        if root.left:
            temp =  root.left
            while temp.left or temp.right:
                if temp.left is None and temp.right is None:
                    break
                if temp.left:
                    left.append(temp.data)
                    temp = temp.left
                elif temp.right:
                    left.append(temp.data)
                    temp = temp.right
                
        temp = root
        dfs = []
        self.getleafnodes(temp,dfs)
        if root.right:
            temp = root.right      
            while temp.left or temp.right:
                if temp.left is None and temp.right is None:
                    
                    break
                if temp.right:
                    right.append(temp.data)
                    temp = temp.right
                elif temp.left:
                    right.append(temp.data)
                    temp = temp.left
        right = right[::-1]
        
        
        return [root.data]+left + dfs + right
---------------------------------
