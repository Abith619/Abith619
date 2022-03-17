#                 Write a Python program to get the first and last second
inputstring = "AbithRaj"

count = 0

for i in inputstring:
	count = count + 1
newstring = inputstring[ 0:1 ] + inputstring [count - 2]
print("Input string = " + inputstring)
print("New String = "+ newstring)