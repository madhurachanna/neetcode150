"""
Search 2D Matrix

You are given an m x n 2-D integer array matrix and an integer target.

Each row in matrix is sorted in non-decreasing order.
The first integer of every row is greater than the last integer of the previous row.
Return true if target exists within matrix or false otherwise.

Can you write a solution that runs in O(log(m * n)) time?

Example 1:
Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 10
Output: true

Example 2:
Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 15
Output: false

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-10000 <= matrix[i][j], target <= 10000
"""

def search_matrix (matrix, target):
    # Find row
    rw = None

    for row in matrix:
        if target >= row[0] and target <= row[-1]:
            rw = row
            break

    if rw == None:
        return False

    i = 0
    j = len(rw) - 1

    # Binary Search
    while i <= j:
        m = i + (j - i) // 2

        if rw[m] == target:
            return True
        if rw[m] > target:
            j = m - 1
        else:
            i = m + 1

    return False

matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]]
target = 10
op = search_matrix(matrix, target)
print(op)
