"""
Max Water Container

You are given an integer array heights where heights[i] represents the height of the ith bar.
You may choose any two bars to form a container.
Return the maximum amount of water a container can store.

Example 1:

Input: height = [1,7,2,5,4,7,3,6]
Output: 36

Example 2:

Input: height = [2,2,2]
Output: 4

Constraints:

2 <= height.length <= 1000
0 <= height[i] <= 1000

"""

# O(n^2)
def get_max_water_container_size_2 (heights):

    max_size = 0

    for i in range(len(heights)):
        for j in range(i + 1, len(heights)):
            min_height = min(heights[j], heights[i])
            diff_index = j - i
            area = diff_index * min_height
            max_size = max(max_size, area)

    return max_size


# O(n)
def get_max_water_container_size (heights):
    i = 0
    j = len(heights) - 1
    max_size = 0

    while i < j:
        min_height = min(heights[j], heights[i])
        diff_index = j - i
        area = diff_index * min_height
        max_size = max(max_size, area)

        if (heights[i] < heights[j]):
            i += 1
        else:
            j -= 1

    return max_size



# height = [1,7,2,5,4,7,3,6]
# height = [2,2,2]
# height = [1, 1]
# op = get_max_water_container_size(height)
# print(op)
