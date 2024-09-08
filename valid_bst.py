"""
Valid Binary Search Tree

Given the root of a binary tree, return true if it is a valid binary search tree,
otherwise return false.

A valid binary search tree satisfies the following constraints:

The left subtree of every node contains only nodes with keys less than the node's key.
The right subtree of every node contains only nodes with keys greater than the node's key.
Both the left and right subtrees are also binary search trees.

Example 1:

Input: root = [2,1,3]
Output: true

Example 2:

Input: root = [1,2,3]
Output: false
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def isValidBST(root):

    def dfs(pn, l_range=float("-inf"), r_range=float("inf"), is_valid=True):
        # Base case: If the current node is None, return the validity status
        if not pn:
            return is_valid

        # Case 1: Check sibling relationships
        # Ensure the left child value is less than the current node value
        is_valid = is_valid and (pn.left.val < pn.val) if pn.left else is_valid
        # Ensure the right child value is greater than the current node value
        is_valid = is_valid and (pn.right.val > pn.val) if pn.right else is_valid

        # Case 2: Check the current node's value against the allowed range
        is_valid = is_valid and pn.val > l_range and pn.val < r_range

        # Recursively validate the left and right subtrees
        # For the left subtree, the current node's value becomes the right boundary
        # For the right subtree, the current node's value becomes the left boundary
        is_valid = dfs(pn.left, l_range, pn.val, is_valid) and dfs(pn.right, pn.val, r_range, is_valid)

        # Return the final validity status
        return is_valid

    val = dfs(root)
    return val
