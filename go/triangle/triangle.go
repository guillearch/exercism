// Package triangle is the solution to: https://github.com/exercism/go/tree/master/exercises/triangle.
package triangle


// Notice KindFromSides() returns this type. Pick a suitable data type.
type Kind

const (
    // Pick values for the following identifiers used by the test program.
    NaT // not a triangle
    Equ // equilateral
    Iso // isosceles
    Sca // scalene
)

// KindFromSides returns .
func KindFromSides(a, b, c float64) Kind {

	var k Kind
	return k
}
