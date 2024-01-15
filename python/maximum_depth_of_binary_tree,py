# Function to calculate the maximum depth of a binary tree
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Base case: If the root is empty, the depth is 0
        if not root:
            return 0

        # Recursively calculate the depths of the left and right subtrees
        max_left = self.maxDepth(root.left)
        max_right = self.maxDepth(root.right)

        # Determine the maximum depth between the left and right subtrees
        # max_depth = max(max_left, max_right)
        if max_left >= max_right:
            max_depth = max_left
        else:
            max_depth = max_right


        # Add 1 to account for the current root node's level
        return 1 + max_depth