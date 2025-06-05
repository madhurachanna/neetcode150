import time
from typing import List

# First Solution (Recursive Subsets Generation with p())
class Solution1:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def p(arr):
            if len(arr) == 1:
                return [arr]

            res = []
            for i in range(len(arr)):
                a = p([arr[i]])
                b = p(arr[i + 1:])
                res.append(a[0])
                for lt in b:
                    lt.append(arr[i])
                    res.append(lt)
            return res

        op = p(nums)
        op.append([])
        return op

# Second Solution (DFS Approach)
class Solution2:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res


# Function to measure execution time
def measure_execution_time(solution, nums):
    start_time = time.time()
    result = solution.subsets(nums)
    end_time = time.time()
    execution_time = end_time - start_time
    return execution_time, result


# Test case
nums = [1, 2, 3, 4, 5, 6, 7, 8]

# Instantiate both solutions
solution1 = Solution1()
solution2 = Solution2()

# Measure execution time for Solution1
execution_time1, result1 = measure_execution_time(solution1, nums)
print(f"Solution 1 (Recursive) Execution Time: {execution_time1} seconds")

# Measure execution time for Solution2
execution_time2, result2 = measure_execution_time(solution2, nums)
print(f"Solution 2 (DFS) Execution Time: {execution_time2} seconds")

fastest = "My soln" if execution_time1 < execution_time2 else "Neetcode soln"
print('fastest', fastest)

# Ensure both solutions produce the same result
# assert sorted(result1) == sorted(result2), "The results of both solutions are different!"
