"""Write a program that reads an integer from the user. Then your program should display 
a message indicating whether the integer is even or odd."""
n=int(input())
if n%2 == 0:
    print("even")
if n%2!=0:
    print("odd")