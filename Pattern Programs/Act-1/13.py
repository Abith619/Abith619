"""create a program that reads words from the user until the user enters a blank line. 
After the user enters a blank line your program should dis-play each word entered by the user 
exactly once. The words should be displayed in the same order that they were entered"""

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
print(list(set(num)))