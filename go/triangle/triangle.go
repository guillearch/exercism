// Package triangle is the solution to: https://github.com/exercism/go/tree/master/exercises/triangle.
package triangle

import "math"

// Kind describes the type of triangle.
type Kind string

// Types of triangle.
const (
	NaT = "NaT"
	Equ = "Equ"
	Iso = "Iso"
	Sca = "Sca"
)

// KindFromSides determines if a triangle is equilateral, isosceles or scalene.
func KindFromSides(a, b, c float64) Kind {

	var k Kind

	if isTriangle(a, b, c) == false {
		k = NaT
	} else {
		if a == b || b == c || c == a {
			if a == b && b == c {
				k = Equ
			} else {
				k = Iso
			}
		} else {
			k = Sca
		}
	}

	return k
}

func isTriangle(a, b, c float64) bool {
	if a > 0 && b > 0 && c > 0 {
		if !(math.IsInf(a, 0) || math.IsInf(b, 0) || math.IsInf(c, 0)) {
			if a+b >= c && b+c >= a && c+a >= b {
				return true
			}
		}
	}
	return false
}
