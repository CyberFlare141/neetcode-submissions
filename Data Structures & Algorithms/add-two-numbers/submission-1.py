# Another approach.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    
     str1 = []
     while l1 is not None:
         str1.append(str(l1.val))
         l1 = l1.next
     str11 = "".join(str1)

     str2=[]
     while l2 is not None:
         str2.append(str(l2.val))
         l2 = l2.next
     str22 = "".join(str2)

     rstr11 = str11[::-1]
     rstr22 = str22[::-1]

     int1 = int(rstr11)
     int2 = int(rstr22)

     total = int1 + int2

     totalstr = str(total)[::-1]

     result = ListNode(0)
     curr = result

     for i in totalstr:
        curr.next = ListNode(int(i))
        curr = curr.next

     return result.next
     