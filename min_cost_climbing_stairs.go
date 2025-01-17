/*
	Min Cost Climbing Stairs

	You are given an array of integers cost where cost[i] is the cost of taking a step
    from the ith floor of a staircase. After paying the cost, you can step to either the
    (i + 1)th floor or the (i + 2)th floor.

	You may choose to start at the index 0 or the index 1 floor.

	Return the minimum cost to reach the top of the staircase,
    i.e. just past the last index in cost.

	Example 1:

	Input: cost = [1,2,3]
	Output: 2
	Explanation: We can start at index = 1 and pay the cost of cost[1] = 2 and take two
    steps to reach the top. The total cost is 2.

	Example 2:

	Input: cost = [1,2,1,2,1,1,1]
	Output: 4
	Explanation: Start at index = 0.

	Pay the cost of cost[0] = 1 and take two steps to reach index = 2.
	Pay the cost of cost[2] = 1 and take two steps to reach index = 4.
	Pay the cost of cost[4] = 1 and take two steps to reach index = 6.
	Pay the cost of cost[6] = 1 and take one step to reach the top.
	The total cost is 4.
*/

package main

import "fmt"

// Memoization
func dfs(cost []int, i int, memo map[int]int) int {
	if value, exists := memo[i]; exists {
		return value
	}
	if i == 0 || i == 1 {
		return 0
	}

	min_cost := 0

	prevStep1 := (dfs(cost, i-1, memo) + cost[i-1])
	prevStep2 := (dfs(cost, i-2, memo) + cost[i-2])

	if prevStep1 > prevStep2 {
		min_cost = prevStep2
	} else {
		min_cost = prevStep1
	}

	memo[i] = min_cost

	return min_cost
}

func minCostClimbingStairs(cost []int) int {

	// return dfs(cost, len(cost), make(map[int]int))

	// Tabulation
	dp := make([]int, len(cost)+1)

	for i := 2; i < len(dp); i++ {
		tc1 := dp[i-1] + cost[i-1]
		tc2 := dp[i-2] + cost[i-2]
		if tc1 > tc2 {
			dp[i] = tc2
		} else {
			dp[i] = tc1
		}
	}

	return dp[len(dp)-1]
}

// func main() {
// 	op := minCostClimbingStairs([]int{1, 2, 1, 2, 1, 1, 1})
// 	// op := climbingStairs2(50)
// 	fmt.Println(op)
// }
