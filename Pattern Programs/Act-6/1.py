"""Write a function that takes the lengths of the two shorter sides of a right triangle
as its parameters. Return the hypotenuse of the triangle, computed using
Pythagorean theorem, as the function's result. Include a main program that reads
the lengths of the shorter sides of a right triangle from the user, uses your function
to compute the length of the hypotenuse, and displays the result."""
from math import sqrt
print("Input lengths of shorter triangle sides:")
a = float(input("a= "))
b = float(input("b= "))
c = sqrt(a**2 + b**2)
print("The length of the hypotenuse is = ", c )