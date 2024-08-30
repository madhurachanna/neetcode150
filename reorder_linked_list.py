"""
Reorder Linked List

You are given the head of a singly linked-list.
The positions of a linked list of length = 7 for example,
can intially be represented as:

[0, 1, 2, 3, 4, 5, 6]

Reorder the nodes of the linked list to be in the following order:

[0, 6, 1, 5, 2, 4, 3]

Notice that in the general case for a list of length = n
the nodes are reordered to be in the following order:

[0, n-1, 1, n-2, 2, n-3, ...]

You may not modify the values in the list's nodes,
but instead you must reorder the nodes themselves.

Example 1:

Input: head = [2,4,6,8]
Output: [2,8,4,6]

Example 2:

Input: head = [2,4,6,8,10]
Output: [2,10,4,8,6]
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def reorderList(head):
    # Slow-Fast pointer
    # Since we don't know about the lenght of linked-list,
    # We can find both mid and the last point in one iteration
    sp = head
    fp = head.next
    while fp and fp.next:
        sp = sp.next # Take one step
        fp = fp.next.next # Take two steps

    cn = sp.next
    sp.next = None
    pn = None

    # Reverse 2nd Half
    while cn != None:
        temp = cn.next
        cn.next = pn
        pn, cn = cn, temp

    head2 = pn
    cn = head

    # Merge
    while head2:
        p1, p2 = cn.next, head2.next
        cn.next = head2
        head2.next = p1
        cn, head2 = p1, p2
