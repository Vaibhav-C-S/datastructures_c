#User function Template for python3

class Solution:
    def bottomView(self, root):
        # code here
        vertical_traversal ={}
        queue = [[root,0]]
        while queue:
            node,x = queue.pop(0)
            if x in vertical_traversal:
                vertical_traversal[x] = node.data
            else:
                vertical_traversal[x] = node.data
            if node.left:
                queue.append([node.left,x-1])
            if node.right:
                queue.append([node.right,x+1])
        
        bottom_view = []
        m,n = min(vertical_traversal),max(vertical_traversal)
        for i in range(m,n+1):
            bottom_view.append(vertical_traversal[i])
        return bottom_view
