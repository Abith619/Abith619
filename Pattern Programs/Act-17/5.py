"""Write a program that displays the date and time. 
Here is a sample run: 
Current date and time is May 16, 2012 10:34:23"""
import datetime
x = datetime.datetime.now()
print(x.strftime("%b %d %Y %H:%M:%S"))