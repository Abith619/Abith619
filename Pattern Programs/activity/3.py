"""Write a program that begins by reading a radius, r , from the user. 
The program will continue by computing and displaying the area of a circle with radius r 
and the volume of a sphere with radius r . Use the pi constant in the math module in your calculations."""
from cmath import pi
import math
r = 10
area=math.pi*r*r
print(area)

vol = 4/3*pi*r*r*r
print(vol)