"""
Search a 2D Matrix

You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.
"""
from typing import List

def search_matrix(matrix: List[List[int]], target: int) -> bool:
    # Find row
    for row in matrix:
        if row[0] >= target and row[-1] <= target:
            for num in row:
                if num == target:
                    return True

    return False
