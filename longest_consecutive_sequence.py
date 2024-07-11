"""
Longest Consecutive Sequence

Given an array of integers nums, return the length of the longest
consecutive sequence of elements.

A consecutive sequence is a sequence of elements in which each element is
exactly 1 greater than the previous element.

You must write an algorithm that runs in O(n) time.

Example 1:

Input: nums = [2,20,4,10,3,4,5]

Output: 4
Explanation: The longest consecutive sequence is [2, 3, 4, 5].

Example 2:

Input: nums = [0,3,2,5,4,6,1,1]

Output: 7
Constraints:

0 <= nums.length <= 1000
-10^9 <= nums[i] <= 10^9
"""
import heapq

# Using heaps
# O(n) + O(nlogn) = O(nlogn)
def get_lcs_1 (nums):
    # O(n)
    heapq.heapify(nums)

    lsl = 0
    csl = 0
    pnum = None

    # O(n) x O(logn) = O(nlogn)
    # O(n)
    for i in range(len(nums)):
        # O(logn)
        num = heapq.heappop(nums)
        if (pnum == None):
            pnum = num
            csl += 1
            continue
        if (num == pnum):
            pnum = num
            continue
        if (num == pnum + 1):
            pnum = num
            csl += 1
            continue
        pnum = num
        lsl = max(lsl, csl)
        csl = 1

    return max(lsl, csl)

# Using sort
# Faster
# O(n) + O(nlogn) = O(nlogn)
def get_lcs (nums):

    lsl = 0
    csl = 0
    pnum = None

    # O(nlogn)
    nums.sort()

    # O(n)
    for num in nums:
        if (pnum == None):
            pnum = num
            csl += 1
            continue
        if (num == pnum):
            pnum = num
            continue
        if (num == pnum + 1):
            pnum = num
            csl += 1
            continue
        pnum = num
        lsl = max(lsl, csl)
        csl = 1

    return max(lsl, csl)


# nums = [2,20,4,10,3,4,5]
# nums = [0,3,2,5,4,6,1,1]
# nums = [0, 0]
# nums=[9,1,4,7,3,-1,0,5,8,-1,6]
# op = get_lcs(nums)
# print(op)
