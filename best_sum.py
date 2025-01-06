#!/usr/bin/env python3

all_combinations = []
best_combination = []

def best_sum(target, nums, lt):
    if target == 0:
        all_combinations.append(lt.copy())
        if len(lt) > len(best_combination):
            best_combination = lt.copy()
        return
    if target < 0:
        # lt.pop()
        return

    print('---', target, nums, lt)

    for num in nums:
        rem = target - num
        lt.append(num)
        print(rem, lt, num)
        x = best_sum(rem, nums, lt)
        lt.pop()


op = best_sum(7, [5, 3, 4, 7], [])
print(all_combinations)
print(best_combination)
