class Minheap:
    def __init__(self,capacity):
        self.size = 0
        self.capacity = capacity
        self.storage = [0] * capacity

    def getleftchild(self,index):
        return 2*index + 1
    def getrightchld(self,i):
        return 2*i +2
    def getparent(self,i):
        return (i-1)//2
    def hasleftchild(self,i):
        return self.getleftchild(i) < self.size
    def hasrightchild(self,i):
        return self.getrightchld(i) < self.size
    def hasparent(self,i):
        return self.getparent(i) >= 0
    def insert(self,value):
        if self.size == self.capacity:
            raise "heap is full"
        self.storage[self.size] = value
        self.size+=1
        #self.heapifyUpIterative()
        self.heapifyUpRecursive(self.size -1)
    def heapifyUpRecursive(self,index):
        if self.hasparent(index) and self.storage[self.getparent(index)] > self.storage[index]:
            self.storage[self.getparent(index)], self.storage[index] = self.storage[index], self.storage[self.getparent(index)]
            self.heapifyUpRecursive(self.getparent(index))

    def heapifyUpIterative(self):
        index = self.size -1
        while self.hasparent(index) and self.storage[self.getparent(index)] > self.storage[index]:
            self.storage[self.getparent(index)], self.storage[index] =self.storage[index] ,self.storage[self.getparent(index)]
            index = self.getparent(index)
    def removeMin(self):
        if self.size<0:
            raise "heap is the empzy"
        data = self.storage[0]
        self.storage[0] = self.storage[self.size - 1]
        self.size -=1
        #self.heapifyDownIterative()
        self.heapifyDownRecursive(0)
        return data
    def heapifyDownRecursive(self,index):
        if self.hasleftchild(index):
            smallerChild = self.getleftchild(index)
            if self.hasrightchild(index) and self.storage[self.getrightchld(index)] < self.storage[self.getleftchild(index)]:
                smallerChild = self.getrightchld(index)
            if self.storage[smallerChild] < self.storage[index]:
                self.storage[smallerChild],self.storage[index] = self.storage[index],self.storage[smallerChild]
                self.heapifyDownRecursive(smallerChild)
            else:
                return



    def heapifyDownIterative(self):
        index = 0
        while self.hasleftchild(index):
            smallerChild = self.getleftchild(index)
            if self.hasrightchild(index) and self.storage[self.getrightchld(index)] < self.storage[self.getleftchild(index)]:
                smallerChild = self.getrightchld(index)
            if self.storage[smallerChild] < self.storage[index]:
                self.storage[smallerChild],self.storage[index] = self.storage[index],self.storage[smallerChild]
            else:
                break
            index = smallerChild

heap = Minheap(7)
heap.insert(2)
heap.insert(1)
heap.insert(5)
heap.insert(0)
print(heap.removeMin())
print(heap.removeMin())
print(heap.removeMin())

