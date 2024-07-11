"""
Is Palindrome
Given a string s, return true if it is a palindrome, otherwise return false.

A palindrome is a string that reads the same forward and backward.
It is also case-insensitive and ignores all non-alphanumeric characters.

Example 1:

Input:
s = "Was it a car or a cat I saw?"

Output: true

Explanation: After considering only alphanumerical characters we have
"wasitacaroracatisaw", which is a palindrome.

Example 2:

Input:
s = "tab a cat"

Output: false
Explanation: "tabacat" is not a palindrome.

Constraints:

1 <= s.length <= 1000
s is made up of only printable ASCII characters.
"""
def is_palindrome_valid (s):

    i = 0
    j = len(s) - 1

    while i < j:
        ord_ch1 = ord(s[i].lower())
        if (not ((ord_ch1 > 48 and ord_ch1 <= 57) or (ord_ch1 > 97 and ord_ch1 <= 122))):
            i += 1
            continue
        ord_ch2 = ord(s[j].lower())
        if (not ((ord_ch2 > 48 and ord_ch2 <= 57) or (ord_ch2 > 97 and ord_ch2 <= 122))):
            j -= 1
            continue
        if (s[i].lower() != s[j].lower()):
            return False
        i += 1
        j -= 1

    return True



# s = "Was it a car or a cat I saw?"
# s = "tab a cat"
# op = is_palindrome_valid(s)
# print(op)
