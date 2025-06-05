from typing import List

# Works But not revsersing in-place
def np(nums: List[int]) -> None:
    # Find i so that nums[i] < nums[i + 1]
    index1 = 0
    for i in range(len(nums) - 1, 0, -1):
       if nums[i] > nums[i - 1]:
           index1 = i-1
           break

    # Find smallest number greater than nums[i]
    index2 = index1
    for i in range(index1, len(nums)):
        if nums[i] > nums[index1]:
            if nums[i] < nums[index2] or index2 == index1:
                index2 = i

    if index2 == 0:
        nums.reverse()
    else:
        # Swap those numbers
        nums[index1], nums[index2] = nums[index2], nums[index1]
        nums2 = nums[index1 + 1:]
        nums2.reverse()
        nums = nums[:index1 + 1] + nums2

# Reversing in place
def np2(nums: List[int]) -> None:
    # Find i so that nums[i] < nums[i + 1]
    index1 = 0
    for i in range(len(nums) - 1, 0, -1):
       if nums[i] > nums[i - 1]:
           index1 = i-1
           break

    # Find smallest number greater than nums[i]
    index2 = index1
    for i in range(len(nums) - 1, index1, - 1 ):
        if nums[i] > nums[index1]:
            if nums[i] < nums[index2] or index2 == index1:
                index2 = i

    if index2 == 0:
        nums.reverse()
    else:
        # Swap those numbers
        nums[index1], nums[index2] = nums[index2], nums[index1]

        # Reverse the rest
        index2 = len(nums) - 1
        index1 = index1 + 1

        while index1 < index2:
            nums[index1], nums[index2] = nums[index2], nums[index1]
            index1 += 1
            index2 -= 1

op = np([1,3,2])
np2([2,3,1,3,3])
print(op)
