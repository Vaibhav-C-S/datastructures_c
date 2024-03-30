class Node:
    def __init__(self,value):
        self.value = value
        self.next  = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_beginning(self,value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node

    def insert_at_end(self,value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
    def printll(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

    def delete_at_beginning(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            self.tail = None
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
    def delete_at_end(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            self.tail = None
        else:
            temp=self.head
            while temp.next.next:
                temp= temp.next
            temp.next = temp.next.next

    def insert_at_pos(self,index,value):
        node = Node(value)
        count = 0
        if index == 0:
            self.insert_at_beginning(value)
            return
        temp = self.head
        while temp:
            if count == index -1:
                break
            temp = temp.next
            count+=1
        if temp is None:
            raise "index out of range"
        node.next = temp.next
        temp.next = node

    def delete_at_pos(self,index):
        count = 0
        if index == 0:
            self.delete_at_beginning()
            return
        temp = self.head
        while temp:
            if count == index - 1:
                break
            temp = temp.next
            count += 1
        if temp is None or temp.next is None:
            raise "index out of range"
        temp.next = temp.next.next




ll = LinkedList()
ll.insert_at_beginning(2)
ll.insert_at_end(3)
ll.insert_at_beginning(1)
ll.insert_at_pos(4,4)

ll.printll()
