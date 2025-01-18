package main

import (
	"fmt"
)

func all_palindromes(s string) []string {

	pals := []string{}
	memo := make(map[string]bool)

	for i := 0; i < len(s); i++ {
		// For odd-length palindromes
		a := i
		b := i

		for a >= 0 && b < len(s) && s[a] == s[b] {
			pal := s[a : b+1]
			if !memo[pal] {
				pals = append(pals, pal)
				memo[pal] = true
			}
			a -= 1
			b += 1
		}

		// For even-length palindromes
		a = i
		b = i + 1

		for a >= 0 && b < len(s) && s[a] == s[b] {
			pal := s[a : b+1]
			if !memo[pal] {
				pals = append(pals, pal)
				memo[pal] = true
			}
			a -= 1
			b += 1
		}
	}

	return pals
}

// func main() {
// 	x := all_palindromes("ababd")
// 	fmt.Print(x)
// }
