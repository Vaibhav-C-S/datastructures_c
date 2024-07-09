from collections import deque

class Stack:
    def __init__(self, size):
        self.size = size
        self.q = deque(maxlen=self.size)

    def push(self, elem):
        if len(self.q) == self.size:
            raise OverflowError("Stack is full")
        self.q.append(elem)
        curr_size = len(self.q)
        for i in range(curr_size - 1):
            self.q.append(self.q.popleft())

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from an empty stack")
        return self.q.popleft()

    def is_empty(self):
        return not self.q

s = Stack(5)
s.push(1)
s.push(2)
s.push(3)
while not s.is_empty():
    print(s.pop())
