#time is o(2n) and space is o(1)
def isPalindrome(self, head):
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        #now slow is pointing the middle
        #from slow, we shall now reverse the list
        before = None
        temp = slow
        while temp is not None:
            after = temp.next
            temp.next = before
            before = temp
            temp = after
        #comparing both halves

        right = before
        left = head
        while right is not None:
            if (left.data == right.data):
                left = left.next
                right = right.next
            else:
                return False
        return True
----------------------------------------
class Solution:
    def isPalindrome(self, head):
        if head.next is None:
            return True
        #code here
        slow = head
        fast = head
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        anotherhead = slow.next
        slow.next = None
        before = None
        temp = anotherhead
        after = temp.next
        while temp:
            after = temp.next
            temp.next = before
            before = temp
            temp = after
        
        anotherhead = before
        while head and anotherhead:
            if head.data != anotherhead.data:
                return False
            head = head.next
            anotherhead = anotherhead.next
        return True
