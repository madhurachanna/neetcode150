"""
Longest Substring Without Duplicates

Given a string s, find the length of the longest substring without duplicate characters.
A substring is a contiguous sequence of characters within a string.

Example 1:

Input: s = "zxyzxyz"
Output: 3
Explanation: The string "xyz" is the longest without duplicate characters.

Example 2:

Input: s = "xxxx"
Output: 1
Constraints:

0 <= s.length <= 1000
s may consist of printable ASCII characters.
"""


def get_longest_substring_length (s):
    i = 0
    j = 0
    longest_subs_len = 0
    ch_map = {}

    while j < len(s):
        ch = s[j]

        if (not ch in ch_map):
            ch_map[ch] = j
        elif (ch in ch_map) and (ch_map[ch] >= i):
            longest_subs_len = max(longest_subs_len, j - i)
            i = ch_map[ch] + 1
            ch_map[ch] = j
        else:
            ch_map[ch] = j

        j += 1

    return max(longest_subs_len, j-i)



# s = "zxyzxyz"
# s = "xxxx"
# s = "xxlmndvjxlmno"
# s = "thequickbrownfoxjumpsoverthelazydogthequickbrownfoxjumpsovert"
# op = get_longest_substring_length(s)
# print(op)
