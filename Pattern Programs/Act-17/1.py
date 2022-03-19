"""Some websites impose certain rules for passwords. Write a method that checks whether a string is a 
valid password. Suppose the password rules are as follows: 
■ A password must have at least eight characters.
 ■ A password consists of only letters and digits.
 ■ A password must contain at least two digits. 
Write a program that prompts the user to enter a password and displays Valid Password if the rules are 
followed or Invalid Password otherwise"""
import re
def validate():
    while True:
        password = input("Enter a password: ")
        if len(password) < 8:
            print("Make sure your password is at lest 8 letters")
        elif re.search('[0-9].*[0-9]',password) is None:
            print("Make sure your password has two number in it")
        elif re.search('[a-z]',password) is None: 
            print("Make sure your password has a letter in it")
        else:
            print("Your password seems fine")
            break
validate()