"""Write a program that reads numbers from the user until a blank line is entered. Your program
 should display the average of all of the values entered by the user. Then the program should display all of the below average values, followed by all of the average values (if any), followed by all of the above average values. An appropriate
label should be displayed before each list of values"""
from numpy import average


n = None    
num = []    
while True:
    n = input("Enter number: ")
    if n == "":
        for i in num:
            print(i)
        break
    else:
        num.append(n)
average = sum(num) / len(num)
print (list(average()))