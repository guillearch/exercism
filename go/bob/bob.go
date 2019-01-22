// Package bob is the solution to: https://github.com/exercism/go/tree/master/exercises/bob.
package bob

import (
	"regexp"
	"strings"
)

// Hey returns Bob's answer to the input string.
func Hey(remark string) string {

	re := regexp.MustCompile("[A-Za-z]")

	remark = strings.TrimSpace(remark)

	if remark == strings.ToUpper(remark) && re.MatchString(remark) {
		switch {
		case strings.HasSuffix(remark, "?") == true:
			return "Calm down, I know what I'm doing!"
		default:
			return "Whoa, chill out!"
		}
	} else {
		switch {
		case strings.HasSuffix(remark, "?") == true:
			return "Sure."
		case len(remark) == 0:
			return "Fine. Be that way!"
		default:
			return "Whatever."
		}
	}
}
