from typing import List

# Optimized using Kadane's Algorithm
def max_subarray(nums: List) -> int:
    max_sum = -100000
    sum = 0

    for num in nums:
        sum += num
        max_sum = max(max_sum, sum)
        # Reset sum if the sum < 0
        if sum < 0:
            sum = 0
    return max_sum

# Recursive approach
def max_subarray_rec(nums: List) -> int:
    num_len = len(nums)
    if num_len == 0:
        return 0
    if num_len == 1:
        return nums[0]
    return max(
        sum(nums),
        max_subarray_rec(nums[:num_len - 1]),
        max_subarray_rec(nums[1: num_len]))


# op = max_subarray([-2,1,-3,4,-1,2,1,-5,4])
# op = max_subarray([5,4,-1,7,8])
# op = max_subarray_rec([5,4,-1,7,8])
op = max_subarray_rec([-2,1,-3,4,-1,2,1,-5,4])
print(op)
