class Stack:
    def  __init__(self,size):
        self.s = [None] * size
        self.top = -1
        self.size = size
    def push(self,elem):
        if not self.isFull():
            self.top += 1
            self.s[self.top] = elem

        else:
            raise "overflow exception"

    def pop(self):
        if not self.isEmpty():
            data = self.s[self.top]
            self.top -=1
            return data
        else:
            raise "underflow exception"

    def top_elem(self):
        if self.top != -1:
            return self.s[self.top]
        raise "stack empty"

    def isFull(self):
        return (self.top + 1) == self.size

    def isEmpty(self):
        return self.top == -1

stack = Stack(5)
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())

print(stack.top_elem())


