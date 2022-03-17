"""Write a Python program to calculate surface volume and area of a sphere.
Note: A sphere is a perfectly round geometrical object in three-dimensional space that is the 
surface of a completely round ball."""
"""Expected Output :
Surface Area is : 7.071428571428571
Volume is : 1.7678571428571428"""
import math

PI=math.pi
radius = float(input('the Radius of a Sphere= '))
surface_area =  4 * PI * radius * radius
Volume = (4 / 3) * PI * radius * radius * radius

print("\n The Surface area of a Sphere = %.2f" %surface_area)
print("\n The Volume of a Sphere = %.2f" %Volume)