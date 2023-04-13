# polynomial_calculator

This function takes one or more polynomials and does addidtion or subtraction to output a single polynomial.

Pass the polynomials to be solved as a string in the below format

(a1x\*\*n + b1x\*\*n + c1x + d1) + (a2x\*\*n + b2x\*\*n + c2x + d2) + .......

*Take care of the spacing between the operators while passing the input.*

Sample inputs:<br />
add_poly('(x\*\*3 + 5x\*\*2 - 3x + 3) + (4x\*\*5 - 2x\*\*2 + 1) + (4x\*\*3)')<br />
add_poly('(x**3 + 5x**2 - 3x + 3) + (4x**5 - 2x**2 + 1) + (-1)')<br />
add_poly('(x**3 + 5x**2 - 3x + 3) + (4x**5 - 2x**2 + 1)')<br />
add_poly('(x**3 + 5x**2 - 3x + 3)')<br />
add_poly('(x**3 + 5x**2 - 3x + 3) - (4x**5 - 2x**2 + 1)')<br />
add_poly('(x**3 + 5x**2 - 3x + 3) - (-3)')<br />

Sample outputs:<br />
(x**3 + 5x**2 - 3x + 3) + (4x**5 - 2x**2 + 1) + (4x**3) = 4x**5 + 5x**3 + 3x**2 - 3x + 4<br />
(x**3 + 5x**2 - 3x + 3) + (4x**5 - 2x**2 + 1) + (-1) = 4x**5 + x**3 + 3x**2 - 3x + 3<br />
(x**3 + 5x**2 - 3x + 3) + (4x**5 - 2x**2 + 1) = 4x**5 + x**3 + 3x**2 - 3x + 4<br />
(x**3 + 5x**2 - 3x + 3) = x**3 + 5x**2 - 3x + 3<br />
(x**3 + 5x**2 - 3x + 3) - (4x**5 - 2x**2 + 1) = 4x**5 + x**3 + 7x**2 - 3x + 2<br />
(x**3 + 5x**2 - 3x + 3) - (-3) = x**3 + 5x**2 - 3x + 6<br />
