"""Write a program that reads integers from the user and stores them in a list. 
Use 0 as a sentinel value to mark the end of the input. Once all of the values have been read 
your program should display them (except for the 0) in reverse order, with one value
appearing on each line."""


n = None    
num = []    
while True:
    n = input("Enter number: ")
    if n == "0":
        for i in num:
            print(i)
        break
    else:
        num.append(n)
num.reverse()
print(num)