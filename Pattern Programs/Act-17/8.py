"""(Print distinct numbers) Write a program that reads in ten numbers and displays the number of distinct 
numbers and the distinct numbers separated by exactly one space (i.e., if a number appears multiple times, 
it is displayed only once). (Hint: Read a number and store it to an array if it is new. If the number is 
already in the array, ignore it.) After the input, the array contains the distinct numbers. Here is the 
sample run of the program: 
Enter ten numbers: 1 2 3 2 1 6 3 4 5 2
 The number of distinct numbers is 6
 The distinct numbers are: 1 2 3 6 4 5"""
import array as arr
n=input()
arr=n
print(sorted(set(arr)))