import heapq

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        for i,j in enumerate(lists):
            if j is not None:
                heapq.heappush(heap , (j.val , i , j))

        temp = ListNode(0)
        curr = temp

        while heap:
            val , tie_breaker , node = heapq.heappop(heap)

            curr.next = node
            curr = curr.next

            if node.next is not None:
                heapq.heappush(heap , (node.next.val, tie_breaker, node.next))
        

        return temp.next