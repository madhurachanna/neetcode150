"""
Anagram Groups

Given an array of strings strs, group all anagrams together into sublists.
You may return the output in any order.

An anagram is a string that contains the exact same characters as another string,
but the order of the characters can be different.

Example 1:

Input: strs = ["act","pots","tops","cat","stop","hat"]

Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
Example 2:

Input: strs = ["x"]

Output: [["x"]]
Example 3:

Input: strs = [""]

Output: [[""]]
Constraints:

1 <= strs.length <= 1000.
0 <= strs[i].length <= 100
strs[i] is made up of lowercase English letters.
"""
from is_anagram import is_anagram

def get_anagram_groups(strs):
    used_index_map = {}
    anagram_groups = []

    for i in range(len(strs)):
        word = strs[i]
        group_list = [word]

        # If the word is already part of anagram group, continue to next word
        if (i in used_index_map):
            continue

        # Check for the other words that can be anagram with the current word
        for j in range(i + 1, len(strs)):
            if is_anagram(word, strs[j]):
                group_list.append(strs[j])
                used_index_map[j] = True


        anagram_groups.append(group_list)


    return anagram_groups


strs = ["act","pots","tops","cat","stop","hat"]
strs = ["x"]
op = get_anagram_groups(strs)
print(op)
