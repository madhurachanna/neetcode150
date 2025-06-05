#!/usr/bin/env python3

"""
Combinations of a Phone Number

You are given a string digits made up of digits from 2 through 9 inclusive.

Each digit (not including 1) is mapped to a set of characters as shown below:

A digit could represent any one of the characters it maps to.

Return all possible letter combinations that digits could represent.
You may return the answer in any order.

Example 1:

Input: digits = "34"

Output: ["dg","dh","di","eg","eh","ei","fg","fh","fi"]
Example 2:

Input: digits = ""

Output: []
"""


# def letter_combinations_2(digits):
#     number_letter = {2: ["a", "b", "c"], 3: ["d", "e", "f"]}
#     maps = [["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]]

#     res = maps[0]

#     for i in range(1, len(maps)):
#         cr = []
#         print("i", i)
#         for j in range(0, len(res)):
#             for k in range(0, len(maps[i])):
#                 ch = res[j] + maps[i][k]
#                 print("ch -> ", ch)
#                 cr.append(ch)
#         res = cr
#     print("res = ", res, cr)
#     return res


def letter_combinations(digits):
    number_letter = {2: ["a", "b", "c"], 3: ["d", "e", "f"]}
    maps = [["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]]

    r = []
    c = []

    lt = maps

    def dfs(i=0):

        print("st1", lt[i], i)

        if i == len(lt) - 1:
            print("base-case")
            return lt[i].copy()

        res = []

        for ch in lt[i]:
            ll = dfs(i + 1)

            print("ll", ll, ch)

            for j in range(len(ll)):
                ll[j] = ll[j] + ch

            print("new ll", ll)

            # res.append(ll)
            res += ll
            ll = []

        print("res ", res)

        return res

    op = dfs(0)
    # return ("opop -> ", op, maps)
    return op


op = letter_combinations(23)
print("op -> ", op)
