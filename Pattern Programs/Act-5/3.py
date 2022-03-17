# Write a Python program to remove the intersection of a 2nd set from the 1st set
x={1, 3, 5, 8}
y={2, 4, 6, 8}
x.difference_update(y)
print(x)