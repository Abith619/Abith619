"""A string is a palindrome if it is identical forward and backward. For example “anna”, “civic”,
“level” and “hannah” are all examples of palindromic words. Write a program that reads a string 
from the user and uses a loop to determines whether or not it is a palindrome. Display the result, 
including a meaningful output message"""

def isPalindrome(str):
	for i in range(0, int(len(str)/2)):
		if str[i] != str[len(str)-i-1]:
			return False
	return True
s = input()
ans = isPalindrome(s)

if (ans):
	print("Yes")
else:
	print("No")