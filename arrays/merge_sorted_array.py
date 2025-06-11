"""
Merge Sorted Array

You are given two integer arrays nums1 and nums2, sorted in non-decreasing order,
and two integers m and n, representing the number of elements in nums1 and nums2
respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function,
but instead be stored inside the array nums1. To accommodate this,
nums1 has a length of m + n, where the first m elements denote the elements that
should be merged, and the last n elements are set to 0 and should be ignored.
nums2 has a length of n.

Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming
from nums1.
"""

from typing import List

def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    i = m - 1
    j = n - 1
    k = len(nums1) - 1

    while k >= 0 and j >= 0:
        # Get the max value
        if i >= 0 and (j < 0 or nums1[i] >= nums2[j]):
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1

# Swap, sort and merge (Not efficient)
def merge_2(nums1: List[int], m: int, nums2: List[int], n: int) -> None:

    j = 0
    i = 0
    while i < len(nums1):
        while j < n:
            if i >= m:
                nums1[i] = nums2[j]
                j += 1
                i += 1
            else:
                if nums1[i] <= nums2[j]:
                    i += 1
                    break
                if nums1[i] > nums2[j]:
                    nums1[i], nums2[j] = nums2[j], nums1[i]
                    i += 1

                    # Sort num2s array:
                    k = j
                    while k < n or nums2[k] > nums2[k + 1]:
                        nums2[k],  nums2[k + 1] = nums2[k + 1], nums2[k]
                        k += 1
                    break


merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3)
