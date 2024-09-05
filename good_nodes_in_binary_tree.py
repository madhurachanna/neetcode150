"""
Count Good Nodes in Binary Tree

Within a binary tree, a node x is considered good if the path
from the root of the tree to the node x contains no nodes with a
value greater than the value of node x

Given the root of a binary tree root, return the number of good nodes within the tree.

Example 1:

Input: root = [2,1,1,3,null,1,5]
Output: 3

Example 2:

Input: root = [1,2,-1,3,4]
Output: 4
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def goodNodes(root):
    gn = 0
    def dfs(pn, rpn = None):
        if (pn == None):
            return

        # Replace current good node
        if ((rpn <= pn.val)):
            rpn = pn.val
            gn += 1

        if pn.left:
            dfs(pn.left, rpn)
        if pn.right:
            dfs(pn.right, rpn)

    dfs(root, root.val if root else None)
    return gn
