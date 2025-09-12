/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public boolean isSymmetric(TreeNode root) {
        return recursive(root, root);
    }
    public boolean recursive(TreeNode right, TreeNode left){
        if(right == null && left == null){ return true; }
        if(right == null || left == null){ return false; }
        else{
            return(
                right.val == left.val &&
                recursive(right.right, left.left) &&
                recursive(left.right, right.left)
            );
        }
    }
}