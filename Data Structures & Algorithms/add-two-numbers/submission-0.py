# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
     rl1 = None
     while l1 is not None:
        temp = l1.next
        l1.next = rl1
        rl1 = l1
        l1 = temp
     
     rl2 = None
     while l2 is not None:
        temp = l2.next
        l2.next=rl2
        rl2 = l2
        l2=temp
    
     str1 = []
     while rl1 is not None:
         str1.append(str(rl1.val))
         rl1 = rl1.next
     str11 = "".join(str1)

     str2=[]
     while rl2 is not None:
         str2.append(str(rl2.val))
         rl2 = rl2.next
     str22 = "".join(str2)

     int1 = int(str11)
     int2 = int(str22)

     total = int1 + int2

     totalstr = str(total)[::-1]

     result = ListNode(0)
     curr = result

     for i in totalstr:
        curr.next = ListNode(int(i))
        curr = curr.next

     return result.next
     