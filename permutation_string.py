"""
Permutation String

You are given two strings s1 and s2.

Return true if s2 contains a permutation of s1, or false otherwise.
That means if a permutation of s1 exists as a substring of s2, then return true.

Both strings only contain lowercase letters.

Example 1:

Input: s1 = "abc", s2 = "lecabee"

Output: true
Explanation: The substring "cab" is a permutation of "abc" and is present in "lecabee".

Example 2:

Input: s1 = "abc", s2 = "lecaabee"

Output: false
Constraints:

1 <= s1.length, s2.length <= 1000

"""

def is_permutation_string_2 (s1, s2):
    s1m = {}
    i = 0
    j = 0

    for ch in s1:
        s1m[ch] = s1m[ch] + 1 if ch in s1m else 1

    while i < len(s2):
        ch = s2[i]
        if not ch in s1m:
            i += 1
            continue

        s2m = {}
        j = i - 1

        while 1:
            j += 1
            # Expensive process
            if s1m == s2m:
                return True

            if j >= len(s2):
                break

            if not s2[j] in s1m:
                break

            s2m[s2[j]] = s2m[s2[j]] + 1 if s2[j] in s2m else 1
            if s2m[s2[j]] > s1m[s2[j]]:
                break

        i += 1

    return False


# O(n)
def is_permutation_string (s1, s2):
    s1m = {}
    s2m = {}
    target = len(s1)
    matches = 0

    # s1 cannot be a subset of s2
    if len(s1) > len(s2):
        return False

    # O(n)
    for ch in s1:
        s1m[ch] = s1m[ch] + 1 if ch in s1m else 1

    # O(n) -> Practically len(s1) or target
    for i in range(target):
        ch = s2[i]
        s2m[ch] = s2m[ch] + 1 if ch in s2m else 1
        if (ch in s1m) and s1m[ch] >= s2m[ch]:
            matches += 1

    # Start the sliding window
    i = 0
    while 1:
        # Return early if there is already a match
        if matches == target:
            return True

        # Return if window reaches the end
        if i + target >= len(s2):
            break

        # Remove 1st character from current window
        ch = s2[i]
        s2m[ch] = max(0, s2m[ch] - 1)
        if (ch in s1m) and s1m[ch] > s2m[ch]:
            matches -= 1

        # Add next character after the window
        ch = s2[i + target]
        s2m[ch] = s2m[ch] + 1 if ch in s2m else 1
        if (ch in s1m) and s1m[ch] >= s2m[ch]:
            matches += 1

        i += 1

    return False



# s1 = "abc"
# s2 = "lecabee"
# s1 = "abc"
# s2 = "lecaabee"
# s1="adc"
# s2="dcda"
# s1 = "abcdxabcde"
# s2 = "abcdeabcdx"
# op = is_permutation_string(s1, s2)
# print(op)
