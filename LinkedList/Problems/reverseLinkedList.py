# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
---------------------------------------------------
#function Template for python3

"""
# Node Class

class node:
    def __init__(self, val):
        self.data = val
        self.next = None

"""

class Solution:
    #Function to reverse a linked list.
    def reverseList(self, head):
        # Code here
        temp = head
        after = temp.next
        before = None
        while temp:
            after = temp.next
            temp.next = before
            before = temp
            temp = after
        return before



---------------------------------------------------
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        newhead = self.reverseList(head.next)
        front = head.next
        front.next = head
        head.next = None
        return newhead
------------------------------------------
