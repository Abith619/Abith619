"""An integer, n, is said to be perfect when the sum of all of the proper divisors of n is 
equal to n. For example, 28 is a perfect number because its proper divisors are 1, 2, 4, 7 
and 14, and 1 + 2 + 4 + 7 + 14 = 28.Write a function that determines whether or not a positive
integer is perfect. Your function will take one parameter. If that parameter is a perfect 
number then your function will return true. Otherwise it will return false. In addition, 
write a main program that uses your function to identify and display all of the perfect 
numbers between 1 and 10,000."""
import math
def isPerfectSquare(x) :
	sq = (int)(math.sqrt(x))
	return (x == sq * sq)

def countPerfectDivisors(n) :
	cnt = 0

	for i in range(1, (int)(math.sqrt(n)) + 1) :

			if ( n % i == 0 ) :

				if isPerfectSquare(i):
						cnt = cnt + 1
				if n/i != i and isPerfectSquare(n/i):
						cnt = cnt + 1
	return cnt
	
		
print("Total perfect divisor of 16 = ",
	countPerfectDivisors(16))
	
print("Total perfect divisor of 12 = ",
	countPerfectDivisors(12))
