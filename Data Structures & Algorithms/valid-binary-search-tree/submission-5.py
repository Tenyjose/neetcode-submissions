# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, low, high):
            if not node:
                return True
            
            if node.val <= low or node.val >= high:
                return False
            
            left_valid = dfs(node.left, low, node.val)
            right_valid = dfs(node.right, node.val, high)
            
            return left_valid and right_valid
        
        return dfs(root, float('-inf'), float('inf'))
