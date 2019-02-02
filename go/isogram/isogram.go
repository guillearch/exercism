// Package isogram is the solution to: https://github.com/exercism/go/tree/master/exercises/isogram.
package isogram

import (
	"strings"
	"unicode"
)

// IsIsogram determines if a word or phrase is an isogram.
func IsIsogram(s string) bool {

	for _, i := range s {
		if unicode.IsLetter(i) {
			letter := string(unicode.ToUpper(i))
			if strings.Count(strings.ToUpper(s), letter) > 1 {
				return false
			}
		}

	}

	return true
}
