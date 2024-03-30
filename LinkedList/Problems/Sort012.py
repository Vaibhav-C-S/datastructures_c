
#User function Template for python3 2pass
'''
    Your task is to segregate the list of 
    0s,1s and 2s.
    
    Function Arguments: head of the original list.
    Return Type: head of the new list formed.

    {
        # Node Class
        class Node:
            def __init__(self, data):   # data -> value stored in node
                self.data = data
                self.next = None
    }



'''

#time complexity o(2n) and space is o(1)
class Solution:
    #Function to sort a linked list of 0s, 1s and 2s.
    def segregate(self, head):
        #code here
        count = [0] * 3
        temp = head
        while temp:
            count[temp.data]+=1
            temp = temp.next
        temp = head
        while count[0]:
            temp.data = 0
            count[0]-=1
            temp = temp.next
        while count[1]:
            temp.data =1
            count[1]-=1
            temp = temp.next
        while count[2]:
            temp.data = 2
            count[2] -=1
            temp = temp.next
        return head
    





















--------------------------------------------------------------------#1pass
#User function Template for python3
'''
	Your task is to segregate the list of 
	0s,1s and 2s.
	
	Function Arguments: head of the original list.
	Return Type: head of the new list formed.

	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}

'''
class Solution:
    #Function to sort a linked list of 0s, 1s and 2s.
    def segregate(self, head):
        #code here
        zerohead = Node(-1)
        dummyzerohead = zerohead
        onehead = Node(-1)
        dummyonehead = onehead
        twohead = Node(-1)
        dummytwohead = twohead
        temp = head
        while temp:
            if temp.data == 0 :
                dummyzerohead.next = temp
                dummyzerohead = dummyzerohead.next
            elif temp.data  == 1:
                dummyonehead.next = temp
                dummyonehead = dummyonehead.next
            else:
                dummytwohead.next = temp
                dummytwohead = dummytwohead.next
                
            temp = temp.next
            
        dummyzerohead.next = onehead.next
        dummyonehead.next = twohead.next
        return zerohead.next



