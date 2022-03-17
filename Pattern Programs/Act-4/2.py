"""The length of a month varies from 28 to 31 days. In this exercise you will 
create a program that reads the name of a month from the user as a string. Then your 
program should display the number of days in that month. Display “28 or 29 days” for February
so that leap years are addressed"""
"""import datetime
n=input()
month=datetime.monthrange()
print(month)"""

print("List of months: January, February, March, April, May, June, July, August, September, October, November, December")
month_name = input("Input the name of Month: ")

if month_name == "February":
	print("No. of days: 28/29 days")
elif month_name in ("April", "June", "September", "November"):
	print("No. of days: 30 days")
elif month_name in ("January", "March", "May", "July", "August", "October", "December"):
	print("No. of days: 31 day")
else:
	print("Wrong month name")

