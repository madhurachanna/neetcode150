"""
Evaluate Reverse Polish Notation

You are given an array of strings tokens that represents a valid
arithmetic expression in Reverse Polish Notation.

Return the integer that represents the evaluation of the expression.

The operands may be integers or the results of other operations.
The operators include '+', '-', '*', and '/'.
Assume that division between integers always truncates toward zero.
Example 1:

Input: tokens = ["1","2","+","3","*","4","-"]

Output: 5

Explanation: ((1 + 2) * 3) - 4 = 5
Constraints:

1 <= tokens.length <= 1000.
tokens[i] is "+", "-", "*", or "/",
or a string representing an integer in the range [-100, 100].

"""
def get_reverse_rpn(tokens):
    stack = []

    for ch in tokens:
        if ch == '+' or ch == '-' or ch == '*' or ch == '/':
            if (ch == '+'):
                sm = sum(stack[-2:])
            elif (ch == '-'):
                sm = stack[-2] - stack[-1]
            elif (ch == '*'):
                sm = stack[-2] * stack[-1]
            elif (ch == '/'):
                sm = int(stack[-2] / stack[-1])
            stack.pop()
            stack.pop()
            stack.append(sm)
        else:
            stack.append(int(ch))

    return stack[0]


tokens = ["1","2","+","3","*","4","-"]
tokens = ["3","5","2","*","+"]
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
op = get_reverse_rpn(tokens)
print(op)
