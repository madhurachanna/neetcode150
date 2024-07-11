"""
Valid Sudoku

You are given a a 9 x 9 Sudoku board board.
A Sudoku board is valid if the following rules are followed:

Each row must contain the digits 1-9 without duplicates.
Each column must contain the digits 1-9 without duplicates.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.
Return true if the Sudoku board is valid, otherwise return false

Note: A board does not need to be full or be solvable to be valid.

Example 1:

Input:
board =
     0   1   2   3   4   5   6   7   8
[0 ["1","2",".",".","3",".",".",".","."],
 1 ["4",".",".","5",".",".",".",".","."],
 2 [".","9","8",".",".",".",".",".","3"],

 3 ["5",".",".",".","6",".",".",".","4"],
 4 [".",".",".","8",".","3",".",".","5"],
 5 ["7",".",".",".","2",".",".",".","6"],

 6 [".",".",".",".",".",".","2",".","."],
 7 [".",".",".","4","1","9",".",".","8"],
 8 [".",".",".",".","8",".",".","7","9"]]

Output: true

Example 2:

Input: board =
[["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","1",".",".",".",".",".","3"],

 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],

 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]

Output: false
Explanation: There are two 1's in the top-left 3x3 sub-box.

Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit 1-9 or '.'.

"""

def is_sudoku_valid (board):
    print(board)
    # validate rows
    for row in board:
        nums_present = {}
        for num in row:
            if num != ".":
                if (num in nums_present):
                    print("Returning while row validation")
                    return False
                nums_present[num] = True


    # validate cols
    for i in range(0, 9):
        nums_present = {}
        for row in board:
            num = row[i]
            if num != ".":
                if (num in nums_present):
                    print("Returning while col validation")
                    return False
                nums_present[num] = True


    # validate cube
    for i in range(0, 7, 3):
        rows = board[i: i + 3]
        nums_present = {}
        for j in range(0, 9):
            if (j % 3 == 0):
                nums_present = {}

            for row in rows:
                num = row[j]
                if num != ".":
                    if (num in nums_present):
                        print("Returning while cube validation", num)
                        return False
                    nums_present[num] = True

        print(i)

    return True


# board =[
#     ["1","2",".",".","3",".",".",".","."],
#     ["4",".",".","5",".",".",".",".","."],
#     [".","9","8",".",".",".",".",".","3"],
#     ["5",".",".",".","6",".",".",".","4"],
#     [".",".",".","8",".","3",".",".","5"],
#     ["7",".",".",".","2",".",".",".","6"],
#     [".",".",".",".",".",".","2",".","."],
#     [".",".",".","4","1","9",".",".","8"],
#     [".",".",".",".","8",".",".","7","9"]]

board = [
    ["1","2",".",".","3",".",".",".","."],
    ["4",".",".","5",".",".",".",".","."],
    [".","9","1",".",".",".",".",".","3"],
    ["5",".",".",".","6",".",".",".","4"],
    [".",".",".","8",".","3",".",".","5"],
    ["7",".",".",".","2",".",".",".","6"],
    [".",".",".",".",".",".","2",".","."],
    [".",".",".","4","1","9",".",".","8"],
    [".",".",".",".","8",".",".","7","9"]]


op = is_sudoku_valid(board)
print("op = ", op)
