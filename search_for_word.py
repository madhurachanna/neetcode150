"""
Search for Word

Given a 2-D grid of characters board and a string word,
return true if the word is present in the grid, otherwise return false.

For the word to be present it must be possible to form it with a path
in the board with horizontally or vertically neighboring cells.
The same cell may not be used more than once in a word.

Example 1:

Input:
board = [
  ["A","B","C","D"],
  ["S","A","A","T"],
  ["A","C","A","E"]
],
word = "CAT"

Output: true

Example 2:

Input:
board = [
  ["A","B","C","D"],
  ["S","A","A","T"],
  ["A","C","A","E"]
],
word = "BAT"

Output: false
"""


def exist(board, word):
    # If the word is longer than the number of cells in the board, it's impossible to find the word
    if len(word) > len(board) * len(board[0]):
        return False

    # Helper function to perform recursive backtracking to search the word
    def crawl(index, i, j, used_cell):
        """
        index: current position in the word
        i, j: current cell coordinates on the board
        used_cell: a dictionary that tracks visited cells in the current path to avoid reuse
        """
        print(
            used_cell, word[:index]
        )  # Print the used cells and current part of the word being matched

        # If we have matched the entire word, return True
        if index >= len(word):
            return True

        found = False  # Flag to track if the word has been found

        # Move Right
        if (
            (j + 1 < len(board[i]))
            and (board[i][j + 1] == word[index])
            and (not found)
            and ((i, j + 1) not in used_cell)
        ):
            print("Going Right")
            used_cell[(i, j + 1)] = True  # Mark the cell as used
            found = crawl(
                index + 1, i, j + 1, used_cell
            )  # Recursively crawl to the right
        if (i, j + 1) in used_cell:  # Unmark the cell if the path was unsuccessful
            del used_cell[(i, j + 1)]

        # Move Left
        if (
            (j - 1 > -1)
            and (board[i][j - 1] == word[index])
            and (not found)
            and ((i, j - 1) not in used_cell)
        ):
            print("Going Left")
            used_cell[(i, j - 1)] = True  # Mark the cell as used
            found = crawl(
                index + 1, i, j - 1, used_cell
            )  # Recursively crawl to the left
        if (i, j - 1) in used_cell:  # Unmark the cell if the path was unsuccessful
            del used_cell[(i, j - 1)]

        # Move Down: Check if the cell below matches the current character in the word
        if (
            (i + 1 < len(board))
            and (board[i + 1][j] == word[index])
            and (not found)
            and ((i + 1, j) not in used_cell)
        ):
            print("Going Down")
            used_cell[(i + 1, j)] = True  # Mark the cell as used
            found = crawl(index + 1, i + 1, j, used_cell)  # Recursively crawl downwards
        if (i + 1, j) in used_cell:  # Unmark the cell if the path was unsuccessful
            del used_cell[(i + 1, j)]

        # Move Up: Check if the cell above matches the current character in the word
        if (
            (i - 1 > -1)
            and (board[i - 1][j] == word[index])
            and (not found)
            and ((i - 1, j) not in used_cell)
        ):
            print("Going Up")
            used_cell[(i - 1, j)] = True  # Mark the cell as used
            found = crawl(index + 1, i - 1, j, used_cell)  # Recursively crawl upwards
        if (i - 1, j) in used_cell:  # Unmark the cell if the path was unsuccessful
            del used_cell[(i - 1, j)]

        return found  # Return whether the word has been found or not

    # Iterate through the board to find the starting letter of the word
    for i in range(len(board)):
        for j in range(len(board[i])):
            ch = board[i][j]
            if ch == word[0]:  # If we find the first letter of the word
                print("Starting at", ch, i, j)
                # Begin crawling from the first letter and check if the word exists
                found_word = crawl(1, i, j, {(i, j): True})
                print("Found word:", found_word)
                if found_word:
                    return True  # If the word is found, return True

    return False  # If the word is not found, return False
