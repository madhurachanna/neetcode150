from typing import List

# Using additonal List
# Similarly, we can use 3 Linked list of 0's 1's and 2's,
# and attach tail of one Linked List to Head of another
def sort_nums(nums: List) -> None:

    nums2 = [1]*len(nums)

    i = 0
    j = len(nums2) - 1

    for num in nums:
        if num == 0:
            nums2[i] = 0
            i += 1
        elif num == 2:
            nums2[j] = 2
            j -= 1

# Counting each numbers and modifying List
def sort_nums_counts(nums: List) -> None:
    counts = { 0: 0, 1: 0, 2: 0}

    for num in nums:
        counts[num] += 1

    for i in range(counts[0]):
        nums[i] = 0

    for i in range(counts[0], counts[0] + counts[1]):
        nums[i] = 1

    for i in range(counts[0] + counts[1], counts[0] + counts[1] + counts[2]):
        nums[i] = 2




sort_nums([2,0,1])
