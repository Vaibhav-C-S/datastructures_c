class Queue:
    def __init__(self,size):
        self.size = size
        self.rear,self.front = -1,0
        self.q = [None] * self.size

    def enqueue(self,elem):
        if not self.isFull():
            self.rear = (self.rear + 1) % self.size
            self.q[self.rear] = elem
        else:
            raise "stack overflow"

    def dequeue(self):
        if not self.isEmpty():
            data = self.q[self.front]
            self.front = (self.front +1) % self.size
            return data
        else:
            raise "underflow"

    def peek(self):
        if not self.isEmpty():
            return self.q[self.front]
        raise "queue empty"

    def isEmpty(self):
        return self.front > self.rear
    def isFull(self):
        return (self.rear + 1) % self.size == self.rear
q = Queue(5)
q.enqueue(1)

q.enqueue(2)

print(q.dequeue())
print(q.dequeue())