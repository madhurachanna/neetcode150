"""
Add Two Numbers

You are given two non-empty linked lists, l1 and l2,
where each represents a non-negative integer.

The digits are stored in reverse order, e.g.
the number 123 is represented as 3 -> 2 -> 1 -> in the linked list.

Each of the nodes contains a single digit.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Return the sum of the two numbers as a linked list.

Example 1:
j
Input: l1 = [1,2,3], l2 = [4,5,6]
Output: [5,7,9]

Explanation: 321 + 654 = 975.

Example 2:

Input: l1 = [9], l2 = [9]
Output: [8,1]

Constraints:

1 <= l1.length, l2.length <= 100.
0 <= Node.val <= 9
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def addTwoNumbers(l1, l2):
    c = 0  # Initialize the carry value
    head = l1  # Store the head of the result linked list (which will be l1)

    while True:
        # Calculate the sum of current nodes of l1 and l2, and the carry
        sum = c + (l1.val if l1 else 0) + (l2.val if l2 else 0)
        c = int(sum / 10)  # Calculate the new carry value (sum / 10)

        # Update the current node's value with the sum mod 10
        # i.e., the digit without the carry
        l1.val = sum - c * 10

        # If both lists have been fully traversed, we are done, break the loop
        if l1.next is None and (not l2 or l2.next is None):
            break

        # Move l2 to the next node if it exists, otherwise set it to None
        l2 = l2.next if l2 and l2.next else None

        # If l1 reaches the end but l2 still has nodes, extend l1 by creating new nodes
        if l2 and l1.next is None:
            n = ListNode(0)  # Create a new node with a default value of 0
            l1.next = n  # Attach the new node to the end of l1

        # Move l1 to the next node
        l1 = l1.next

    # If there's any remaining carry after the last addition, add a new node for it
    if c:
        n = ListNode(c)
        l1.next = n

    # Return the head of the modified l1, which represents the result linked list
    return head
