"""
Rotate Image

You are given an n x n 2D matrix representing an image,
rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify
the input 2D matrix directly.

DO NOT allocate another 2D matrix and do the rotation.
"""
from typing import List

def rotate_image(matrix: List[List]):
    # Transpose
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix[i])):
            # Swap
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse Rows
    for i in range(len(matrix)):
        j = 0
        k = len(matrix[0]) - 1
        while j < k:
            matrix[i][j], matrix[i][k] = matrix[i][k], matrix[i][j]
            j += 1
            k -= 1

    print(matrix)

rotate_image([[1,2,3],[4,5,6],[7,8,9]])
