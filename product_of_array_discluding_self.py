"""
Products of Array Discluding Self

Given an integer array nums, return an array output where output[i]
is the product of all the elements of nums except nums[i].

Each product is guaranteed to fit in a 32-bit integer.

Follow-up: Could you solve it in
O(n) time without using the division operation?

Example 1:

Input: nums = [1,2,4,6]

Output: [48,24,12,8]
Example 2:

Input: nums = [-1,0,1,2,3]

Output: [0,-6,0,0,0]
Constraints:

2 <= nums.length <= 1000
-20 <= nums[i] <= 20
"""

# With divison operation
# O(n)
def product_of_array (nums):

    # Find the product of all the numbers:
    total_product = None
    does_contain_zero = False
    zeros_count = 0

    # O(n)
    for j in range(0, len(nums)):
        num = nums[j]
        if (num == 0):
            does_contain_zero = True
            zeros_count += 1
            continue

        total_product = num if total_product == None else total_product*num

    # O(n)
    if zeros_count > 1:
        return [0 for num in nums]

    # O(n)
    for i in range(len(nums)):
        if (does_contain_zero):
            nums[i] = total_product if nums[i] == 0 else 0
        else:
            num = nums[i]
            nums[i] = int(total_product / nums[i])

    return nums


# nums = [1,2,4,6]
# nums = [-1,0,1,2,3]
# op = product_of_array(nums)
# print(op)
