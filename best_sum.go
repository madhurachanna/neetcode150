package main

import (
	"fmt"
)

var best_sum []int

func get_best_sum(target int, nums []int, lt []int) {
	// fmt.Print(target, nums, lt)
	if target == 0 {
		if best_sum == nil || len(best_sum) > len(lt) {
			best_sum = append([]int{}, lt...)
		}
		return
	}
	if target < 0 {
		return
	}
	for _, num := range nums {
		rem := target - num
		lt = append(lt, num)
		get_best_sum(rem, nums, lt)
		lt = lt[:len(lt)-1]
	}

}

// func main() {
// 	get_best_sum(7, []int{5, 3, 4, 7}, []int{})
// 	fmt.Print(best_sum)
// }
