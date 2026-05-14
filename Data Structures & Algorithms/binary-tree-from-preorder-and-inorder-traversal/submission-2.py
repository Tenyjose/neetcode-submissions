# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        ## In preorder, the first value is always the root. 
        root_value = preorder[0]
        root = TreeNode(root_value)

        # Find the root position in inorder.
    # Everything before this index belongs to the left subtree.
    # Everything after this index belongs to the right subtree. 
        mid = inorder.index(root_value)

    # Build the left subtree.
    # preorder[1:mid + 1] gives the preorder values for the left subtree.
    # inorder[:mid] gives the inorder values for the left subtree. 
        root.left = self.buildTree(preorder[1:mid+1] , inorder[:mid])

    # Build the right subtree.
    # preorder[mid + 1:] gives the preorder values for the right subtree.
    # inorder[mid + 1:] gives the inorder values for the right subtree. 
        root.right = self.buildTree( preorder[mid+1: ], inorder[mid+1: ])

        return root
