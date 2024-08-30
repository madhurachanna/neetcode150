"""
Invert a Binary Tree

You are given the root of a binary tree root.
Invert the binary tree and return its root.

Example 1:

Input: root = [1,2,3,4,5,6,7]
Output: [1,3,2,7,6,5,4]

Example 2:
j
Input: root = [3,2,1]
Output: [3,1,2]

Example 3:

Input: root = []
Output: []
"""

def invertTree(root):
    def reverseTree(pn):
        if not pn:
            return

        pn.left, pn.right = pn.right, pn.left

        if pn.left:
            reverseTree(pn.left)
        if pn.right:
            reverseTree(pn.right)

    reverseTree(root)
    return root
