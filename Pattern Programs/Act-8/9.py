"""Two words are anagrams if they contain all of the same letters, but in a different order. 
For example, “evil” and “live” are anagrams because each contains one e, one i, one l, and 
one v. Create a program that reads two strings from the user, determines whether or not they 
are anagrams, and reports the result"""
from collections import Counter

def anagram(s1, s2):
	if(Counter(s1) == Counter(s2)):
		print("The strings are anagrams.")
	else:
		print("The strings aren't anagrams.")
s1 = "evil"
s2 = "live"
anagram(s1, s2)