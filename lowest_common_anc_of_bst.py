"""
Lowest Common Ancestor in Binary Search Tree

Given a binary search tree (BST) where all node values are unique,
and two nodes from the tree p and q,
return the lowest common ancestor (LCA) of the two nodes.

The lowest common ancestor between two nodes p and q is the lowest node
in a tree T such that both p and q as descendants.
The ancestor is allowed to be a descendant of itself.

Example 1:

Input: root = [5,3,8,1,4,7,9,null,2], p = 3, q = 8
Output: 5

Example 2:

Input: root = [5,3,8,1,4,7,9,null,2], p = 3, q = 4
Output: 3

Explanation: The LCA of nodes 3 and 4 is 3, since a node can be a descendant of itself.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def lowestCommonAncestor(root, p, q):

    def ca (pn, p, q):

        if pn == None:
            return [False, None]

        # If p and q exists in different branches, the parent is the common ancestor
        foundAnc = (p <= pn.val and q >= pn.val)

        if foundAnc:
            return [True, pn]
        elif p < pn.val:
            # p, q exists on the left side of the node
            [foundAnc, pn] = ca(pn.left, p, q)
        else:
            # p, q exists on the right side of the node
            [foundAnc, pn] = ca(pn.right, p, q)

        return [foundAnc, pn]

    op = ca(root, min(p.val, q.val), max(p.val, q.val))

    return op[1]
