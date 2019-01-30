// Package raindrops is the solution to: https://github.com/exercism/go/tree/master/exercises/raindrops.
package raindrops

import "strconv"

// Convert converts a number to a string depending on the number's factor.
func Convert(x int) string {

	var raindrops string

	if x%3 == 0 {
		raindrops += "Pling"
	}
	if x%5 == 0 {
		raindrops += "Plang"
	}
	if x%7 == 0 {
		raindrops += "Plong"
	}

	if raindrops == "" {
		return strconv.Itoa(x)
	}
	return raindrops
}
