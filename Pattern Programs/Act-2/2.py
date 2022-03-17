"""Python's standard library includes a method named count that determines how many times 
a specific value occurs in a list. In this exercise, you will create a new function named 
countRange which determines and returns the number of elements within a list that are greater 
than or equal to some minimum value and less than some maximum value. Your function will take 
three parameters: the list, the minimum value and the maximum value. It will return an integer
result greater than or equal to 0. Include a main program that demonstrates your function for 
several different lists, minimum values and maximum values. Ensure that your program works 
correctly for both lists of integers and lists of floating point numbers."""
def count_range_in_list(list, min, max):
	ctr = 0
	for x in list:
		if min <= x <= max:
			ctr += 1
	return ctr

list1 = [10,20,30,40,40,40,70,80,99]
print(count_range_in_list(list1, 40, 100))
print(max(list1))

list2 = ['a','b','c','d','e','f']
print(count_range_in_list(list2, 'a', 'e'))