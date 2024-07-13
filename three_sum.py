"""
Three Integer Sum

Given an integer array nums, return all the triplets
[nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0,
and the indices i, j and k are all distinct.

The output should not contain any duplicate triplets.
You may return the output and the triplets in any order.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]

Output: [[-1,-1,2],[-1,0,1]]

Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].

Example 2:

Input: nums = [0,1,1]

Output: []

Explanation: The only possible triplet does not sum up to 0.

Example 3:

Input: nums = [0,0,0]

Output: [[0,0,0]]

Explanation: The only possible triplet sums up to 0.

Constraints:

3 <= nums.length <= 1000
-10^5 <= nums[i] <= 10^5
"""


def three_sum (nums):
    sum_groups = []
    used_indexes = {}

    # Important! Helps to reduce complexity of finding duplicates
    nums.sort()

    for i in range(0, len(nums) - 2):
        if nums[i] in used_indexes:
            continue
        used_indexes[nums[i]] = True
        target = nums[i] * -1
        diff_map = {}
        p_num = None

        for j in range(i + 1, len(nums)):
            num = nums[j]
            if num in diff_map:
                gs = [nums[i], nums[diff_map[num]], nums[j]]
                if len(sum_groups) > 0 and sum_groups[-1][2] == num:
                    continue
                sum_groups.append(gs)
            else:
                diff = target - num
                diff_map[diff] = j
            p_num = num

    return sum_groups



# nums = [-1,0,1,2,-1,-4]
# nums = [0,0,0,0]
# op = three_sum(nums)
# print(op)
