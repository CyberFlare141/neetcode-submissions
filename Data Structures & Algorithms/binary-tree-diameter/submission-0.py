# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = [0]

        def depth(node):

            if node is None:
                return 0
            
            left_depth = depth(node.left)
            right_depth = depth(node.right)

            current_diameter = left_depth + right_depth

            max_diameter[0] = max(max_diameter[0], current_diameter)
            
            return 1+max(left_depth , right_depth)

        depth(root)

        return max_diameter[0]
        