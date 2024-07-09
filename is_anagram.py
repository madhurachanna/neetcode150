"""
Is Anagram

Given two strings s and t, return true if the two strings are anagrams of each other,
otherwise return false.

An anagram is a string that contains the exact same characters as another string,
but the order of the characters can be different.

Example 1:

Input: s = "racecar", t = "carrace"

Output: true
Example 2:

Input: s = "jar", t = "jam"

Output: false
Constraints:

s and t consist of lowercase English letters.

"""

# O(n)
def is_anagram(s, t):
    s_ch_map = {}

    if (len(s) != len(t)):
        return False

    # O(n)
    # Add letters along with number of occurances to ch_map
    for ch in s:
        if (ch in s_ch_map):
            s_ch_map[ch] += 1
        else:
            s_ch_map[ch] = 1

    # O(n)
    # Check if the letters exists
    for ch in t:
        if ( not (ch in s_ch_map) or s_ch_map[ch] <= 0 ):
            return False

        s_ch_map[ch] -= 1

    return True

# s = "racecar"
# t = "carrace"
# s = "jar"
# t = "jam"
# op = anagram(s, t)
# print(op)
