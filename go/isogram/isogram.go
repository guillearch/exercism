// Package isogram is the solution to: https://github.com/exercism/go/tree/master/exercises/isogram.
package isogram

import (
	"regexp"
	"strings"
)

// IsIsogram determines if a word or phrase is an isogram.
func IsIsogram(s string) bool {

	re := regexp.MustCompile("[^a-zA-Z]")
	characters := strings.ToUpper(re.ReplaceAllString(s, ""))

	for _, i := range characters {
		if strings.Count(characters, string(i)) > 1 {
			return false
		}
	}

	return true
}
