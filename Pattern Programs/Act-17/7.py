"""(Count occurrence of numbers) Write a program that reads the integers between 1 and 100 and counts the 
occurrences of each. Assume the input ends with 0. Here is a sample run of the program: 
Enter the integers between 1 and 100: 2 5 6 5 4 3 23 43 2 0 
2 occurs 2 times 
3 occurs 1 time 
4 occurs 1 time 
5 occurs 2 times 
6 occurs 1 time
23 occurs 1 time 
43 occurs 1 time"""
import collections
nums = []    
while True:
    n = input("Enter the integers between 1 and 100: ")
    if n == '0':
        break
    else:
        nums.append(int(n))

occurrences = collections.Counter(nums)
print(occurrences)