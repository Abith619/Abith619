#     9) Write a Python program to extract year, month, date and time using Lambda.
"""    Sample Output:
2020-01-15 09:03:32.744178
2020
1
15
09:03:32.744178"""
import datetime
now = datetime.datetime.now()

year = lambda x: x.year
month = lambda x: x.month
day = lambda y: y.day
time = lambda y: y.time()
print(year(now))
print(month(now))
print(day(now))
print(time(now))