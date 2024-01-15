//Definition for a binary tree node.
import 'dart:math';

class TreeNode {
  int val;
  TreeNode? left;
  TreeNode? right;
  TreeNode([this.val = 0, this.left, this.right]);
}

class Solution {
  int maxDepth(TreeNode? root) {
    // Base case: If the root is null, the depth is 0
    if (root == null) {
      return 0;
    }

    // Recursively calculate the depths of the left and right subtrees
    int maxLeft = maxDepth(root.left);
    int maxRight = maxDepth(root.right);

    // Determine the maximum depth between the left and right subtrees
    int max_depth =
        max(maxLeft, maxRight); //or do it with comparing the two values

    // Add 1 to account for the current root node's level
    return 1 + max_depth;
  }
}
