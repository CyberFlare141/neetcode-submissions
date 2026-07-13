# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        #Reverse the list
        prev = None
        curr = head
        while curr is not None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        reverse = prev
        start = reverse
        
        if n == 1:
            reverse = reverse.next
        else:
            start = reverse
            for i in range(n - 2):
                start = start.next
                
            start.next = start.next.next

       #again                 
        prev2 = None
        curr1 = reverse
        while curr1 is not None:
            temp = curr1.next
            curr1.next = prev2
            prev2 = curr1
            curr1 = temp

        return prev2
             
             
