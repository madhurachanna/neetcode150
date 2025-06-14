"""
Unique Paths

There is a robot on an m x n grid. The robot is initially located at the top-left
corner (i.e., grid[0][0]). The robot tries to move to the bottom-right
corner (i.e., grid[m - 1][n - 1]).
The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths
that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109
"""

# Find all the paths recursively in forward direction
# Exceedes Time Limit for large values of m and n
def unique_paths_1(m: int, n: int) -> int:
    def dfs(m, n, i = 0, j = 0):
        if i >= m or j >= n:
            return 0
        if i == m - 1 and j == n - 1:
            return 1

        return dfs(m, n, i + 1, j) + dfs(m, n, i, j + 1)

    op = dfs(m, n, 0 , 0)
    return op


# Solving using recursion in backward direction
# Slower due to re-computations
def unique_paths_2(m: int, n: int, i = 0, j = 0) -> int:
    if i == m - 1 or j == n - 1:
        return 1
    return unique_paths_2(m , n, i + 1, j) + unique_paths_2(m, n, i, j + 1)

# Solving using dp in backward direction
def unique_paths(m: int, n: int) -> int:
    matrix = [[ 1
                if r == m - 1 or c == n - 1
                else 0 for c in range(n)
                ] for r in range(m)
              ]

    for row in range(m - 2, -1, -1):
        for col in range(n - 2, -1, -1):
            matrix[row][col] = matrix[row + 1][col] + matrix[row][col + 1]

    return matrix[0][0]

op = unique_paths(23, 12)
print(op)
