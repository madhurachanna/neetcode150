#!/usr/bin/env python3


def can_sum(t, lt, memo = {}):
    if t == 0:
        return True
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
op = can_sum(300, [7, 14])
print("op = ", op)
