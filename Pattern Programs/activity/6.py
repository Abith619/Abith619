"""Develop a program that reads a four-digit integer from the user and displays the sum of 
the digits in the number. For example, if the user enters 3141 then your program should display 
3 + 1 + 4 + 1 = 9"""

"""def Sum(a):
	sum = 0
	for digit in str(a):
	    sum += int(digit)	
        return sum
a = 3141
print(Sum(a))"""

def getSum(a):
    strr = str(a)
    list_of_number = list(map(int, strr.strip()))
    return sum(list_of_number)
a = 12345
print(getSum(a))
