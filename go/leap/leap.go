// Package leap is the solution to: https://github.com/exercism/go/tree/master/exercises/leap.
package leap

// IsLeapYear determines if a given year is leap or not.
func IsLeapYear(year int) bool {
	if year%400 == 0 || year%100 != 0 {
		if year%4 == 0 {
			return true
		}
	}
	return false
}
