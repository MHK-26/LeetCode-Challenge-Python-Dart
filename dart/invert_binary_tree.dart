class TreeNode {
  int? val;
  TreeNode? left;
  TreeNode? right;

  TreeNode([this.val, this.left, this.right]);
}

class Solution {
  // Function to invert a binary tree by swapping its left and right subtrees
  TreeNode? invertTree(TreeNode? root) {
    // Base case: If the root is empty, return null
    if (root == null) {
      return null;
    }

    // Swap the left and right subtrees
    TreeNode? tmp = root.right; // Temporary variable to hold the right subtree
    root.right = root.left; // Assign the left subtree to the right
    root.left = tmp; // Assign the saved right subtree to the left

    // Recursively invert the left and right subtrees
    invertTree(root.right); // Invert the (now swapped) right subtree
    invertTree(root.left); // Invert the (now swapped) left subtree

    // Return the inverted root node
    return root;
  }
}
