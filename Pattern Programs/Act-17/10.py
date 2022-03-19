"""Write a test program that prompts the user to enter a list and displays whether the list is sorted or 
not. Here is a sample run. Note that the first number in the input indicates the number of the elements 
in the list. This number is not part of the list. 
Enter list: 8 10 1 5 16 61 9 11 1 
The list is not sorted 
Enter list: 10 1 1 3 4 4 5 7 9 11 21 
The list is already sorted """
nums = []    
while True:
    n = input("Enter the integers between 1 and 100: ")
    if n == '':
        break
    else:
        nums.append(int(n))
list1=[1, 3, 5, 7, 8, 9]
list2=[5, 1, 8, 7, 9, 3]
print ("list 2 = " + str(nums))
x = 0
test_list1 = nums[:]
test_list1.sort()
if (test_list1 == nums):
	x = 1
if (x) :
	print ("Yes, List is sorted.")
else :
	print ("No, List is not sorted.")