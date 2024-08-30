"""
Remove Node From End of Linked List

You are given the beginning of a linked list head, and an integer n.

Remove the nth node from the end of the list and return the beginning of the list.

Example 1:

Input: head = [1,2,3,4], n = 2
Output: [1,2,4]

Example 2:

Input: head = [5], n = 1
Output: []

Example 3:

Input: head = [1,2], n = 2
Output: [2]
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


def removeNthFromEnd(head, n):

    # Find the lenght of the linked list
    ln = 0
    cn = head
    while cn:
        ln += 1
        cn = cn.next

    dn = ln - n + 1
    cn = head
    i = 1

    # When dn is 1, just return the cn.next or head.next
    if dn == 1:
        return head.next if head and head.next else None

    while cn:
        print(i, dn - 1, cn.val)
        if i == dn - 1:
            # Set cn.next = None if its end of the list or just replace with node
            cn.next = cn.next.next if cn.next and cn.next.next else None
            return head
        i += 1
        cn = cn.next

    return head
