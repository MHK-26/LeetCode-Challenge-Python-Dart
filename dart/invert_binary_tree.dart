class TreeNode {
  int? val;
  TreeNode? left;
  TreeNode? right;

  TreeNode([this.val, this.left, this.right]);
}

class Solution {
  TreeNode? invertTree(TreeNode? root) {
    if (root == null) {
      return null;
    }

    TreeNode? tmp = root.right;
    root.right = root.left;
    root.left = tmp;

    invertTree(root.right);
    invertTree(root.left);

    return root;
  }
}
