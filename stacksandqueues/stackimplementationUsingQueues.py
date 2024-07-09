from collections import deque

class StackUsingQueues:
    def __init__(self, size):
        self.size = size
        self.q1 = deque(maxlen=self.size)
        self.q2 = deque(maxlen=self.size)

    def push(self, elem):
        if len(self.q1) == self.size:
            raise OverflowError("Stack is full")
        self.q2.append(elem)
        while self.q1:
            self.q2.append(self.q1.popleft())
        while self.q2:
            self.q1.append(self.q2.popleft())

    def pop(self):
        if not self.q1:
            raise IndexError("Pop from an empty stack")
        return self.q1.popleft()

    def is_empty(self):
        return not self.q1

s = StackUsingQueues(5)
s.push(2)
s.push(3)
s.push(4)

while not s.is_empty():
    print(s.pop())
