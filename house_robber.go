package main

import (
	"fmt"
)

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func rob2(nums []int, i int) int {
	if i == 0 {
		return nums[0]
	}

	if i == 1 {
		return nums[1]
	}

	return max(rob2(nums, i-1), rob2(nums, i-2)+nums[i])
}

func rob(nums []int) int {
	n := len(nums)
	if n == 0 {
		return 0
	}
	if n == 1 {
		return nums[0]
	}
	if n == 2 {
		return max(nums[0], nums[1])
	}

	dp := make([]int, n)
	dp[0] = nums[0]
	dp[1] = max(nums[0], nums[1])

	for i := 2; i < n; i++ {
		dp[i] = max(nums[i]+dp[i-2], dp[i-1])
	}

	return dp[n-1]
}

// func main() {
// 	x := rob([]int{2, 9, 8, 3, 6})
// 	x := rob2([]int{5, 3, 10, 10, 15, 7, 20}, 6)
// 	x := rob([]int{5, 3, 10, 10, 15, 7, 20})
// 	fmt.Print(x)
// }
