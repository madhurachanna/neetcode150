#!/usr/bin/env python3

"""
Write a function "howSum(targetSum, numbers)' that takes in a targetSum
and an array of numbers as arguments. The function should return an array containing
any combination of elements that add up to exactly the targetSum. If there is no
combination that adds up to the targetSum, then return null.
If there are multiple combinations possible, you may return any single one.
"""

def how_sum(t, lt, memo = {}):
    if t == 0:
        return True,
    if t < 0:
        return False

    for l in lt:
        rem = t - l
        x = False
        if rem in memo:
            x = memo[rem]
        else:
            x = can_sum(rem, lt, memo)
            memo[rem] = x
        if x == True:
            return True

    return False


# op = can_sum(7, [5, 3, 4, 7])
# op = can_sum(7, [2, 4])
op = how_sum(300, [7, 14])
print("op = ", op)
