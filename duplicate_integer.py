"""
Duplicate Integer

Given an integer array nums, return true if any value appears more than once in the array,
otherwise return false.

Example 1:

Input: nums = [1, 2, 3, 3]

Output: true
Example 2:

Input: nums = [1, 2, 3, 4]

Output: false
"""

# O(n)
def deuplicate_integer(nums):
    exist_map = {}

    # O(n)
    for num in nums:
        if (num in exist_map):
            return True
        exist_map[num] = True

    return False

# nums = [1, 2, 3, 3]
# nums = [1, 2, 3, 4]
# op =  deuplicate_integer(nums)
# print(op)
