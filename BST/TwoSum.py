# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    
    def __init__(self, root: Optional[TreeNode],reverse = False):
        self.stack = []
        self.reverse = reverse
        self.pushAll(root)
        

    def next(self) -> int:
        temproot = self.stack.pop()
        if self.reverse == False:
            self.pushAll(temproot.right)
            return temproot.val
        else:
            self.pushAll(temproot.left)
            return temproot.val
    def hasNext(self) -> bool:
        return len(self.stack) != 0
    
    def pushAll(self,root):
        temp = root
        
        while temp:
            self.stack.append(temp)
            if self.reverse == False :
                temp = temp.left
            else:
                temp = temp.right

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        root1= BSTIterator(root)
        root2 = BSTIterator(root,True)
        l = root1.next()
        r = root2.next()
        while l<r:
            if(l+r) < k:
                l = root1.next()
            elif (l+r) > k:
                r = root2.next()
            else:
                return True
        return False
            
