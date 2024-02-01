class Stack:
    def __init__(self,capacity):
        self.capacity = capacity
        self.top = -1
        self.size = 0
        self.stack =[None ] * self.capacity
    def pop(self):
        if self.isempty():
            raise "cannot pop from empty stack"
        else:
            popped_value = self.topelement()
            self.top-=1
            self.size -=1
            return  popped_value

    def push(self,value):
        if self.capacity == self.size:
            raise "cannot push into a already full stack"
        else:
            self.top+=1
            self.stack[self.top] = value
            self.size +=1

    def isempty(self):
        if self.top == -1:
            return True
        return False

    def topelement(self):
        return self.stack[self.top]

    def printstack(self):
        while self.top != -1:
            print(self.pop())

    def printStackKeepOrginal(self):
        tempStack = Stack(self.capacity)
        while not self.isempty():
            value = self.pop()
            print(value)
            tempStack.push(value)

        while not tempStack.isempty():
            self.push(tempStack.pop())

s =Stack(5)
s.push(2)
s.push(3)
s.push(5)
s.push(1)
s.push(3)

s.printStackKeepOrginal()
print(s.stack)
