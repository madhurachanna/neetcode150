/*
	Climbing Stairs

	You are given an integer n representing the number of steps to reach the top of a staircase.
	You can climb with either 1 or 2 steps at a time.

	Return the number of distinct ways to climb to the top of the staircase.

	Example 1:
	Input: n = 2
	Output: 2
	Explanation:
	1 + 1 = 2
	2 = 2

	Example 2:
	Input: n = 3
	Output: 3
	Explanation:
	1 + 1 + 1 = 3
	1 + 2 = 3
	2 + 1 = 3
*/

package main

import "fmt"

// Memoization
func climbingStairs(n int, memo map[int]int) int {
	if val, exists := memo[n]; exists {
		return val
	}
	if n == 0 {
		return 0
	}
	if n == 1 {
		return 1
	}
	count := climbingStairs(n-1, memo) + climbingStairs(n-2, memo)
	memo[n] = count
	return count
}

// Tabulation
func climbingStairs2(n int) int {
	dp := make([]int, n+1)
	dp[0] = 1
	dp[1] = 1
	for i := 2; i < n+1; i++ {
		dp[i] = dp[i-1] + dp[i-2]
	}
	fmt.Print(dp)
	return dp[n]
}

// func main() {
// 	// op := climbingStairs(50, make(map[int]int))
// 	op := climbingStairs2(50)
// 	fmt.Println(op)
// }
