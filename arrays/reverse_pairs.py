"""
Reverse Pairs

Given an integer array nums, return the number of reverse pairs in the array.

A reverse pair is a pair (i, j) where:

0 <= i < j < nums.length and
nums[i] > 2 * nums[j].


Example 1:

Input: nums = [1,3,2,3,1]
Output: 2
Explanation: The reverse pairs are:
(1, 4) --> nums[1] = 3, nums[4] = 1, 3 > 2 * 1
(3, 4) --> nums[3] = 3, nums[4] = 1, 3 > 2 * 1

"""
from typing import List

def reversePairs(nums: List[int]) -> int:
    def merge(l, r):
        a = []
        # Count the pairs
        i = j = count = 0
        while i < len(l) and j < len(r):
            if l[i] > 2 * r[j]:
                count += len(l) - i
                j += 1
            else:
                i += 1

        # Merge the lists
        i = j = 0
        while i < len(l) or j < len(r):
            if j >= len(r) or ( i < len(l) and l[i] < r[j]):
                a.append(l[i])
                i += 1
            else:
                a.append(r[j])
                j += 1

        return a, count

    def merge_sort(nums):
        if (len(nums) < 2):
            return nums, 0
        m = len(nums) // 2
        # Instead of slicing we can use indexes  to improve performance
        l, c1 = merge_sort(nums[:m])
        r, c2 = merge_sort(nums[m:])
        a, c3 = merge(l, r)
        return a, (c1 + c2 + c3)

    a, c = merge_sort(nums)
    return c
