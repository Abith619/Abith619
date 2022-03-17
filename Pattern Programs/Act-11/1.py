"""(Count positive and negative numbers and compute the average of numbers) Write a program that 
reads an unspecified number of integers, determines how many positive and negative values have 
been read, and computes the total and average of the input values (not counting zeros). Your 
program ends with the input 0 . Display the average as a floating-point number.
	Enter an integer, the input ends if it is 0: 1 2 -1 3 0 The number of positives is 3 The 
    number of negatives is 1 The total is 5.0 The average is 1.25
	Enter an integer, the input ends if it is 0: 0 No numbers are entered except 0"""
nums = []    
while True:
    n = input("Enter number: ")
    if n == '0':
        break
    else:
        nums.append(int(n))
pos_count, neg_count = 0, 0
for num in nums:
	if num >= 0:
		pos_count += 1
	else:
		neg_count += 1
print("Positive numbers in the list: ", pos_count)
print("Negative numbers in the list: ", neg_count)
