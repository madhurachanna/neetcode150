package main

import (
	"fmt"
	"strconv"
)

func isValidNumber(str string) bool {
	// Check if the string has leading zeros
	if len(str) > 1 && str[0] == '0' {
		return false
	}

	// Convert the string to an integer
	num, err := strconv.Atoi(str)
	if err != nil {
		return false // Not a valid number
	}

	// Check if the number is between 1 and 26 (inclusive)
	if num >= 1 && num <= 26 {
		return true
	}
	return false
}

func decode_ways(s string) int {
	if len(s) == 0 {
		return 0
	}
	if len(s) == 1 {
		return 1
	}

	count := 0

	if isValidNumber(s[0:1]) {
		count++
		decode_ways(s[1:])
	}

	if isValidNumber(s[0:2]) {
		count++
		decode_ways(s[2:])
	}

	return count
}

func main() {
	x := decode_ways("12")
	fmt.Print(x)
}
