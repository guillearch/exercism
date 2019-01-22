// Package hamming is the solution to: https://github.com/exercism/go/tree/master/exercises/hamming.
package hamming

import "fmt"

// Distance returns the Hamming difference between two homologous DNA strands.
func Distance(a, b string) (int, error) {

	if len(a) != len(b) {
		return 0, fmt.Errorf("DNA strands are not homologous")
	}

	distance := 0

	for i := 0; i < len(a); i++ {
		if a[i] != b[i] {
			distance++
		}
	}

	return distance, nil
}
