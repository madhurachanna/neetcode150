"""
Validate Parentheses

You are given a string s consisting of the following characters:
'(', ')', '{', '}', '[' and ']'.

The input string s is valid if and only if:

Every open bracket is closed by the same type of close bracket.
Open brackets are closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
Return true if s is a valid string, and false otherwise.

Example 1:

Input: s = "[]"

Output: true
Example 2:

Input: s = "([{}])"
Input: s = "([]{])"

Output: true
Example 3:

Input: s = "[(])"

Output: false
Explanation: The brackets are not closed in the correct order.

Constraints:

1 <= s.length <= 1000
"""

def has_valid_parantheses(s):
    stack = []

    pm = {
        ')': '(',
        ']': '[',
        '}': '{',
    }

    # If the length of string is odd,
    # then we will have at least on closing/opening parantheses missing
    if len(s) % 2 != 0:
        return False

    for i in range(len(s) -1, -1 , -1):
        ch = s[i]
        # Add last character to the stack
        stack.append(ch)

        if len(stack) < 2:
            continue
        if not (stack[-2] in pm):
            return False
        # Check if the last two characters are same
        if stack[-1] == pm[stack[-2]]:
            stack.pop()
            stack.pop()

    return True if len(stack) <= 0 else False


# s = "([{}])"
# s = "[(])"
# op = has_valid_parantheses(s)
# print(op)
