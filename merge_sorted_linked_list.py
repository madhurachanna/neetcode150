"""
Merge Two Sorted Linked Lists

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted linked list and return the head of the new sorted linked list.

The new list should be made up of nodes from list1 and list2.

Example 1:

Input: list1 = [1,2,4], list2 = [1,3,5]
Output: [1,1,2,3,4,5]

Example 2:

Input: list1 = [], list2 = [1,2]
Output: [1,2]

Example 3:

Input: list1 = [], list2 = []
Output: []
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Time complexity: O(n + m) where n and m are the lengths of list1 and list2
# Space complexity: O(1) - constant space usage

def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    # If one of the lists is empty, return the other list (base case)
    if list1 is None:
        return list2
    elif list2 is None:
        return list1

    # Ensure that list1 has the smaller starting value, swap if necessary
    if list2.val < list1.val:
        list1, list2 = list2, list1

    # Head of the merged list will be the start of list1
    head = list1

    # Loop until one of the lists is fully merged
    while list1 and list2:
        # If list1 reaches the end, attach the remainder of list2 and return the merged list
        if list1.next is None:
            list1.next = list2
            return head

        # If list2's value should be inserted before the next list1 value
        if list2.val <= list1.next.val:
            # Save the next node in list1 temporarily
            temp = list1.next
            # Insert list2's current node into list1
            list1.next = list2
            # Move list1 forward to list2's current position
            list1 = list2
            # Continue merging the next node in list2
            list2 = temp
        else:
            # If list1's next value is still smaller, simply advance list1
            list1 = list1.next

    # Return the head of the merged list
    return head
