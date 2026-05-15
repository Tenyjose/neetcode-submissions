# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        # we will deifne a helper function to check
        def sameTree (p,q):
            if not p and not q:
                return True

            if not p or not q:
                return False

            if p.val != q.val:
                return False

            left_subtree = sameTree(p.left,q.left)
            right_subtree = sameTree(p.right,q.right)

            return left_subtree and right_subtree

        if not subRoot:
            return True

        if not root:
            return False

        if sameTree(root,subRoot):
            return True

        return (
            self.isSubtree(root.left, subRoot) or
            self.isSubtree(root.right, subRoot)
        )
        