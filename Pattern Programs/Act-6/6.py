"""Write a function that determines whether or not a list of values is in sorted order
(either ascending or descending). The function should return True if the list is already
sorted. Otherwise it should return False. Write a main program that reads a list of
numbers from the user and then uses your function to report whether or not the list
is sorted."""
list1=[1, 3, 5, 7, 8, 9]
list2=[5, 1, 8, 7, 9, 3]
print ("list 2 = " + str(list2))
x = 0
test_list1 = list2[:]
test_list1.sort()
if (test_list1 == list2):
	x = 1
if (x) :
	print ("Yes, List1 is sorted.")
else :
	print ("No, List2 is not sorted.")

