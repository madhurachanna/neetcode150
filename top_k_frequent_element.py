"""
Top K Elements in List

Given an integer array nums and an integer k,
return the k most frequent elements within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order.

Example 1:

Input: nums = [1,2,2,3,3,3], k = 2

Output: [2,3]

Example 2:

Input: nums = [7,7], k = 1

Output: [7]
Constraints:

1 <= nums.length <= 10^4.
-1000 <= nums[i] <= 1000
1 <= k <= number of distinct elements in nums.
"""

def get_top_k_elements (nums, k):
    freqency_map = {}

    for num in nums:
        freqency_map[num] = (freqency_map[num] + 1) if num in freqency_map else 1

    heap = []

    for key in freqency_map.keys():
        heapq.heappush(heap, (freqency_map[key], key))

    heap = heapq.nlargest(k, heap)

    heap = heap[(len(heap) - k) :]
    x = [t[1] for t in heap ]

    return x

# nums = [1,2,2,3,3,3,3]
# k = 2
# nums = [3,0,1,0]
# k = 1
# op = get_top_k_elements(nums, k)
# print(op)
