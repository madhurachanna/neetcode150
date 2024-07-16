"""
Trapping Rain Water

You are given an array non-negative integers heights which represent an elevation map.
Each value heights[i] represents the height of a bar, which has a width of 1.

Return the maximum area of water that can be trapped between the bars.

Example 1:

Input: height = [0,2,0,3,1,0,1,3,2,1]
Output: 9

Constraints:

1 <= height.length <= 1000
0 <= height[i] <= 1000
"""


# O(n)
def get_trapped_rain_water (height):
    i = 0
    j = len(height) - 1
    lmax = 0
    rmax = 0
    trapped_water_area = 0
    is_left_index = True

    while i < j:
        if is_left_index:
            cur_area = lmax - height[i]
        else:
            cur_area = rmax - height[j]
        if cur_area > 0:
            trapped_water_area += cur_area

        lmax = max(lmax, height[i])
        rmax = max(rmax, height[j])

        if (height[i] < height[j]):
            is_left_index = True
            i += 1
        else:
            is_left_index = False
            j -= 1

    return trapped_water_area


# height = [0,2,0,3,1,0,1,3,2,1]
op = get_trapped_rain_water(height)
print("op = ", op)
