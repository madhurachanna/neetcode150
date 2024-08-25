"""
Reverse a Linked List

Given the beginning of a singly linked list head, reverse the list,
and return the new beginning of the list.

Example 1:

Input: head = [0,1,2,3]
Output: [3,2,1,0]

Example 2:

Input: head = []
Output: []

Constraints:

0 <= The length of the list <= 1000.
-1000 <= Node.val <= 1000

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


def reverseList(self, head)
    if not head or head.next == None:
        return head
    pn = None
    cn = head
    nn = head.next

    while 1:
        cn.next = pn
        temp = nn.next
        nn.next = cn
        if temp == None:
            return nn
        cn = nn
        nn = temp
        pn = cn.next
