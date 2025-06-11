"""
Find the Duplicate Number
Given an array of integers nums containing n + 1 integers where each integer
is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and using
only constant extra space.

Example 1:

Input: nums = [1,3,4,2,2]
Output: 2
"""
from typing import List

def find_duplicate(nums: List[int]) -> int:
    slow = nums[0]
    fast = nums[nums[0]]

    while slow != fast:
        slow = nums[slow]
        fast = nums[nums[fast]]

    fast = 0

    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return slow

op = find_duplicate(nums = [6, 2, 9, 4, 7, 1, 8, 3, 7, 5])
# op = find_duplicate(nums = [1,3,4,2,2])
# op = find_duplicate(nums = [3,1,3,4,2])
print(op)
