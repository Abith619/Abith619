"""In a particular jurisdiction, older license plates consist of three letters followed by three 
numbers. When all of the license plates following that pattern had been used, the format was 
changed to four numbers followed by three letters. Write a function that generates a random 
license plate. Your function should have approximately equal odds of generating a sequence of 
characters for an old license plate or a new license plate. Write a main program that calls 
your function and displays the randomly generated license plate"""
import random
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers="13579"
n="2468"
for i in range(3):
    print(random.choice(letters), end="")
for j in range(2):
    print(random.choice(numbers), end="")
for j in range(2):
    print(random.choice(n), end="")