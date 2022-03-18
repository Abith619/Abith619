"""Assume letters A, E, I, O, and U as the vowels. Write a program that prompts the user to enter a string 
and displays the number of vowels and consonants in the string.
Enter a string: Programming is fun 
The number of vowels is 5 
The number of consonants is 11"""
def countCharacterType(str):
	vowels = 0
	consonant = 0
	for i in range(0, len(str)):
		ch = str[i]
		if ( (ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z') ):
			ch = ch.lower()
			if (ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'):
				vowels += 1
			else:
				consonant += 1
	print("Vowels:", vowels)
	print("Consonant:", consonant)
str = input()
countCharacterType(str)