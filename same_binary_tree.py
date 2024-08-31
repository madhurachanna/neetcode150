"""
Same Binary Tree

Given the roots of two binary trees p and q,
return true if the trees are equivalent, otherwise return false.

Two binary trees are considered equivalent if they share
the exact same structure and the nodes have the same values.

Example 1:

Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:

Input: p = [4,7], q = [4,null,7]
Output: false

Example 3:

Input: p = [1,2,3], q = [1,3,2]
Output: false
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def isSameTree(p, q):
    def isSameT (p, q):

        if not p and not q:
            return True

        if not p or not q:
            return False

        if p.val != q.val:
            return False

        l = isSameT(p.left, q.left)
        r = isSameT(p.right, q.right)

        return l and r

    return isSameT(p,q)
