# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSame(self, r:Optional[TreeNode],s:Optional[TreeNode]) -> bool:
            if not r and not s:
                # Base case: Both trees are empty, considered identical.
                return True
            if not r or not s or r.val != s.val:
                # Base case: One tree is empty or values differ, not identical.
                return False
            # Check children recursively if root values match.
            return self.isSame(r.left, s.left) and self.isSame(r.right, s.right)
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

            if not subRoot:
                # Base case: Empty subRoot always exists within any tree.
                return True
            if not root:
                # Base case: Subtree cannot exist in an empty tree.
                return False
            # Check for direct match (subRoot is identical to root subtree).
            if self.isSame(root, subRoot):
                return True
            # Recursively search for subRoot in root's children.
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

                