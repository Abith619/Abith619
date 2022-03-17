"""Write a Python program to find the roots of a quadratic function.
Expected Output :                                                                                             
There are 2 roots: -0.834579 and -1.725421"""
# Quadratic_function = (a * x^2) + b*x + c
import cmath
a= 25
b= 64
c= 36
root = (b**2)-(4 * a*c)

ans2 = (-b-cmath.sqrt(root))/(2 * a)
ans1 = (-b + cmath.sqrt(root))/(2 * a)

print('The roots are')
print(ans1)
print(ans2)