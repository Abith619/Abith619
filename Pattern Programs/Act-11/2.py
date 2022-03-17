"""Write a program that prompts the user to enter a string and displays the number of the 
uppercase letters in the string
Enter a string: Welcome to JavA == The number of uppercase letters is 2"""
str = "AbiThRaJ"
def Count(str):
    upper = 0
    for i in range(len(str)):
        if str[i].isupper():
            upper += 1
    print('Upper case letters = ', upper)
Count(str)