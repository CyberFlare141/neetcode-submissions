# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
            
        result = []
        queue = collections.deque([root])
        while len(queue) > 0:
            
            level_size = len(queue)
            current_row = []
            
            for i in range(level_size):
                node = queue.popleft()
                current_row.append(node.val)             
                if node.left != None:
                    queue.append(node.left)
                if node.right != None:
                    queue.append(node.right)
            result.append(current_row) 
                       
        return result        