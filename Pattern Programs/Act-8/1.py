"""The surface of the Earth is curved, and the distance between degrees of longitude varies 
with latitude. As a result, finding the distance between two points on the surface of the Earth
is more complicated than simply using the Pythagorean theorem. Let (t 1 , g 1 ) and (t 2 , g 2 )
be the latitude and longitude of two points on the Earth's surface. The distance between these
points, following the surface of the Earth, in kilometers is: 
distance = 6371.01 * arccos(sin(t 1 ) * sin(t 2 ) + cos(t 1 ) * cos(t 2 ) * cos(g 1 - g 2 ))

HINT : The value 6371.01 in the previous equation wasn't selected at random. It is the average 
radius of the Earth in kilometers.Create a program that allows the user to enter the latitude 
and longitude of two points on the Earth in degrees. Your program should display the distance 
between the points, following the surface of the earth, in kilometers."""
"""import math
radius_Earth = 6371.01

t1=int(input("enter the latitude in degree"))
g1=int(input("enter the longitude"))
t2=int(input("enter the latitude in degree"))
g2=int(input("enter the longitude"))
latitude = (t1, g1) 
longitude = (t2, g2)
distance = 6371.01 * arccos(sin(t1 ) * sin(t2 ) + cos(t1 ) * cos(t2 ) * cos(g1 - g2 ))"""
from math import radians, cos, sin, asin, sqrt
lat1 = 53.32055
lat2 = 53.31861
lon1 = -1.72972
lon2 = -1.69972
def distance(lat1, lat2, lon1, lon2):
	lon1 = radians(lon1)
	lon2 = radians(lon2)
	lat1 = radians(lat1)
	lat2 = radians(lat2)
	dlon = lon2 - lon1
	dlat = lat2 - lat1
	a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
	c = 2 * asin(sqrt(a))
	r = 6371
	return(c * r)
print(distance(lat1, lat2, lon1, lon2), "K.M")