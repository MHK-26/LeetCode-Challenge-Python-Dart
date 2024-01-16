//Definition for a binary tree node.
class TreeNode {
  int val;
  TreeNode? left;
  TreeNode? right;
  TreeNode([this.val = 0, this.left, this.right]);
}

class Solution {
  bool isSameTree(TreeNode? p, TreeNode? q) {
    if (p == null && q == null) {
      return true; // Both trees are empty
    }
    if (p == null || q == null || p.val != q.val) {
      return false; // Early termination for mismatches
    }

    // Optimize recursive calls for potential tail recursion:
    return isSameTree(p.right, q.right) && isSameTree(p.left, q.left);
  }

  bool isSubtree(TreeNode? root, TreeNode? subRoot) {
    if (subRoot == null) {
      return true;
    } //Base case: Empty subRoot always exists within any tree.

    if (root == null) {
      return false;
    } // Base case: Subtree cannot exist in an empty tree.

    if (isSameTree(root, subRoot)) {
      return true;
    } else {
      return isSubtree(root.left, subRoot) ||
          isSubtree(root.right,
              subRoot); //Check for direct match (subRoot is identical to root subtree).
    }
  }
}
