class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        

        def dfs_record(node):

            if not node:
                return [None]

            result = [node.val]
            result += dfs_record(node.left)
            result += dfs_record(node.right)
            
            return result

        visited_p = dfs_record(p)
        visited_q = dfs_record(q)

        return visited_p == visited_q