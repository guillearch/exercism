// Package reverse is the solution to: https://github.com/exercism/go/tree/master/exercises/reverse-string/.
package reverse

// String reverses a given string.
func String(s string) (reversed string) {
	for _, i := range s {
		reversed = string(i) + reversed
	}
	return reversed
}
