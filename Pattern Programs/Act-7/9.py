"""Write a Python program to calculate wind chill index.
Expected Output :
Input wind speed in kilometers/hour= 150                                
Input air temperature in degrees Celsius= 29                            
The wind chill index = 31 """
import math
v = float(input("Input wind speed in kilometers/hour: "))
t = float(input("Input air temperature in degrees Celsius: "))
wci = 13.12 + 0.6215*t - 11.37*math.pow(v, 0.16) + 0.3965*t*math.pow(v, 0.16)
print("The wind chill index is", int(round(wci, 0)))
