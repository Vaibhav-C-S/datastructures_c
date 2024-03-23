
class Solution:
    def getleftchild(self,index):
        return 2*index + 1
    def getrightchild(self,i):
        return 2*i +2
    def getparent(self,i):
        return (i-1)//2
    def hasleftchild(self,i):
        return self.getleftchild(i) < self.size
    def hasrightchild(self,i):
        return self.getrightchild(i) < self.size
    def hasparent(self,i):
        return self.getparent(i) >= 0
    def isMaxHeap(self,arr,n):
        # Your code goes here          
        self.size = len(arr)
        for i in range((n-1//2)):
            if self.hasleftchild(i) and arr[self.getleftchild(i)] > arr[i]:
                return False
            if self.hasrightchild(i) and arr[self.getrightchild(i)] > arr[i]:
                return False
        return True
                



#{ 
 # Driver Code Starts
if __name__ =='__main__':
    t= int(input())
    for tcs in range(t):
        n=int(input())
        arr=[int(x) for x in input().split()]
        ob=Solution()
        print(int(ob.isMaxHeap(arr,n)))
# } Driver Code Ends
