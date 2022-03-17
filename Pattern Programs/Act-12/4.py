"""While generating a password by selecting random characters generally gives a rela-tively 
secure password, it also generally gives a password that is difficult to memorize. As an alternative, 
some systems construct a password by taking two English words and concatenating them. While this 
password isn't as secure, it is much easier to memorize.Write a program that reads a file 
containing a list of words, randomly selects two of them, and concatenates them to produce a 
new password. When producing the password ensure that the total length is between 8 and 10 
characters, and that each word used is at least three letters long. Capitalize each word in 
the password so that the user can easily see where one word ends and the next one begins. 
Display the password for the user"""
import random
import string
def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(open("123.txt","r").readline().split()) for i in range(2))
    print("Random string of length", length, "is:", result_str.upper())
get_random_string(8)