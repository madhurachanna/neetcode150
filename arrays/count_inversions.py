"""
Count inversions in an array
Given an array of N integers, count the inversion of the array (using merge-sort).

What is an inversion of an array? Definition: for all i & j < size of array,
if i < j then you have to find pair (A[i],A[j]) such that A[j] < A[i].
"""

def merge (l, r):
    a = []
    i = j = 0
    count = 0
    while i < len(l) or j < len(r):
        if i >= len(l) or j < len(r) and  l[i] > r[j]:
            a.append(r[j])
            count += len(l) - i
            j += 1
        else:
            a.append(l[i])
            i += 1
    return a, count


def number_of_inversions (nums):
    if len(nums) <= 1:
        return nums, 0
    q = int(len(nums) // 2)
    l, c1 = number_of_inversions(nums[:q])
    r, c2 = number_of_inversions(nums[q:])
    a, c3 = merge(l, r)
    return a, (c1 + c2 + c3)


# op = number_of_inversions([2, 3, 7, 1, 3, 5])
op = number_of_inversions([-10, -5, 6, 11, 15, 17])
# op = number_of_inversions([5, 4, 3, 2, 1])
# op = number_of_inversions([7, 5, 3, 8, 2, 6, 4, 1])
print(op)
