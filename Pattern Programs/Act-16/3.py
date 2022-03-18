"""Write a program that prompts the user to enter a Social Security number in the format DDD-DD-DDDD, 
where D is a digit. Your program should check whether the input is valid. Here are sample runs: 
Enter a SSN: 232-23-5435 
232-23-5435 is a valid social security number 
Enter a SSN: 23-23-5435
 23-23-5435 is an invalid social security number"""
import re
def isValidSSN(str):
    regex = "^(?!666|000|9\\d{2})\\d{3}-(?!00)\\d{2}-(?!0{4})\\d{4}$"
    p = re.compile(regex)
    if (str == None):
        return False
    if(re.search(p, str)):
        return True
    else:
        return False
str1 = input()
print(isValidSSN(str1))