"""
Longest Repeating Substring With Replacement

You are given a string s consisting of only uppercase english characters and an integer k.
You can choose up to k characters of the string and replace
them with any other uppercase English character.
After performing at most k replacements,
return the length of the longest substring which contains only one distinct character.

Example 1:

Input: s = "XYYX", k = 2
Output: 4
Explanation: Either replace the 'X's with 'Y's, or replace the 'Y's with 'X's.

Example 2:

Input: s = "AAABABB", k = 1
Output: 5

Constraints:

1 <= s.length <= 1000
0 <= k <= s.length
"""


def get_longest_subs(s, k):

    # Find the most repetative letter
    cm = {}
    ml = 0

    i = 0
    j = 0

    while j < len(s):
        ch = s[j]
        cm[ch] = cm[ch] + 1 if ch in cm else 1

        mv = max(cm, key=cm.get) # Character with most frequency
        wl = j - i + 1 # Window Length

        # Condition wl - mv <= k -> Will check if the substring is valid
        # If the value is > k, it means we can't replace any more characters

        # Move the i-th pointer
        if ((j - i + 1 - cm[mv]) > k):
            cm[s[i]] -= 1
            i += 1

        ml = max(ml, j - i + 1)
        j += 1

    return ml



# s = "AAABABB"
# k = 1
# s = "XYYX"
# k = 2
# s="AABABBA"
# k=1 # 4
# op = get_longest_subs(s, k)
# print(op)
