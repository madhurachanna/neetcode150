package main

import (
	"fmt"
)

func h_rob2(nums []int, i int) int {
	if i == 0 {
		return nums[0]
	}

	if i == 1 {
		return max(nums[1], nums[0])
	}

	return max(h_rob2(nums, i-1), h_rob2(nums, i-2)+nums[i])
}

func h_rob_dp(nums []int) int {
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

func h_rob(nums []int) int {
	ln := len(nums)
	// return max(h_rob2(nums[:ln-1], ln-2), h_rob2(nums[1:], ln-2))
	//
	return max(h_rob_dp(nums[:ln-1]), h_rob_dp(nums[1:]))

}

// func main() {
// 	x := rob([]int{2, 9, 8, 3, 6})
// 	x := rob2([]int{5, 3, 10, 10, 15, 7, 20}, 6)
// 	x := h_rob([]int{5, 3, 10, 10, 15, 7, 20})
// 	x := h_rob([]int{1, 2, 3, 1})
// 	x := h_rob([]int{1, 2, 3, 1})
// 	fmt.Print(x)
// }
