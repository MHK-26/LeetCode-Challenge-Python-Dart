# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:  # Base case: If the root is empty, return None
            return None

        # Swap the left and right subtrees of the current node
        tmp = root.right
        root.right = root.left
        root.left = tmp

        # Recursively invert the left and right subtrees
        self.invertTree(root.right)  # Invert the (now swapped) right subtree
        self.invertTree(root.left)  # Invert the (now swapped) left subtree

        return root  # Return the inverted root node