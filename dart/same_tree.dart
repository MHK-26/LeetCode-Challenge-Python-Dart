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
}
