"""
Palindrome Partitioning

Given a string s, split s into substrings where every substring is a palindrome.
Return all possible lists of palindromic substrings.

You may return the solution in any order.

Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

Example 2:

Input: s = "a"
Output: [["a"]]
"""


def palindrome(s):
    for i in range(len(s) // 2):
        if s[i] != s[-i - 1]:
            return False
    return True


# lt = [[], [], []]

res = []
cl = []
i = 0

def partition(s, i, j, count):
    # if count > 10:
    #     return
    print('i, j',i,j, count)
    if (s == ""):
        res.append(cl.copy())
        return

    l = s[:i]
    r = s[i:]

    print('l, r', l, r)

    if (palindrome(l)):
        cl.append(l)
        partition(r, i, i + len(r), count + 1)

    cl.pop()
    print('r append or not', r)
    if r and palindrome(r):
        cl.append(r)
        partition(r, i +1, len(s), count)



partition("bdd", 1, 2, 0)
print('res', res)
