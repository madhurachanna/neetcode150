"""
Binary Search
You are given an array of distinct integers nums,
sorted in ascending order, and an integer target.

Implement a function to search for target within nums.
If it exists, then return its index, otherwise, return -1.

Your solution must run in
O(logn) time.

Example 1:

Input: nums = [-1,0,2,4,6,8], target = 4

Output: 3

Example 2:

Input: nums = [-1,0,2,4,6,8], target = 3

Output: -1

Constraints:

1 <= nums.length <= 10000.
-10000 < nums[i], target < 10000
"""

def b_search(nums, target):
    i = 0
    j = len(nums) - 1
    m = int((j - i) / 2)

    if nums[i] == target:
        return i
    elif nums[j] == target:
        return j

    while (j - i) > 1 :
        m = int((j - i) / 2)
        m = i + m
        if (nums[m] == target):
            return m
        if nums[m] > target:
            j = m
        else:
            i = m
    return -1


# Code improvement
def binary_search(nums, target):
    i = 0
    j = len(nums) - 1

    while i <= j:
        # m is always integer
        m = i + (j - i) // 2  # Calculate mid-point

        if nums[m] == target:
            return m
        elif nums[m] < target:
            i = m + 1
        else:
            j = m - 1

    return -1  # Target not found


nums = [-1,0,2,4,6,8]
target = 4
target = 3
op = b_search(nums, target)
print(op)
