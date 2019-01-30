// Package scrabble is the solution to: https://github.com/exercism/go/tree/master/exercises/scrabble-score.
package scrabble

import "strings"

// Score returns the scrabble score for a given word.
func Score(word string) (score int) {
	word = strings.ToUpper(word)
	for _, i := range word {
		score += letterToValue(i)
	}
	return score
}

func letterToValue(i rune) int {
	switch i {
	case 'A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T':
		return 1
	case 'D', 'G':
		return 2
	case 'B', 'C', 'M', 'P':
		return 3
	case 'F', 'H', 'V', 'W', 'Y':
		return 4
	case 'K':
		return 5
	case 'J', 'X':
		return 8
	case 'Q', 'Z':
		return 10
	default:
		return 0
	}
}
