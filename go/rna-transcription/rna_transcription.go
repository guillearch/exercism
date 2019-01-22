// Package strand is the solution to: https://github.com/exercism/go/tree/master/exercises/rna-transcription/.
package strand

var transcription = map[rune]string{
	'G': "C",
	'C': "G",
	'T': "A",
	'A': "U",
}

// ToRNA returns the RNA complement of a DNA strand.
func ToRNA(dna string) string {
	var rna string
	for _, nucleotide := range dna {
		rna += transcription[nucleotide]
	}
	return string(rna)
}
