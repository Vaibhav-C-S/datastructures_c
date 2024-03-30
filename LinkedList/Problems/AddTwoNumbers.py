# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #time complexity and space complexity O(max(l1,l2))
        temp1 = l1
        temp2 = l2
        head = ListNode(-1)
        current = head
        c =0
        while temp1 or temp2 or c:
            s = c
            if temp1:
                s+= temp1.val
            if temp2:
                s+=temp2.val
            c = s//10
            s = s%10
            current.next = ListNode(s)
            current = current.next
            if temp1:
                temp1= temp1.next
            if temp2:
                temp2 = temp2.next
        return head.next






        
