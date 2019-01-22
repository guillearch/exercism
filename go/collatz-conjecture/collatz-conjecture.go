// Package collatzconjecture is the solution to: https://github.com/exercism/go/tree/master/exercises/collatz-conjecture.
package collatzconjecture

import "fmt"

// CollatzConjecture returns the number of steps required to reach 1, given a number n.
func CollatzConjecture(n int) (int, error) {

	steps := 0

	if n <= 0 {
		return n, fmt.Errorf("number n must be greater than 0")
	}

	for i := 1; n > 1; i++ {
		if n%2 == 0 {
			n /= 2
		} else {
			n = n*3 + 1
		}
		steps = i
	}

	return steps, nil
}
