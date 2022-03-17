# Write a Python program to convert a string into datetime
from datetime import datetime

my_date_string = "Mar 11 2011 11:31AM"
datetime_object = datetime.strptime(my_date_string, '%b %d %Y %I:%M%p')

print(datetime_object)
# Method-2
from dateutil import parser

date_time = parser.parse("Mar 11 2011 11:31AM")
print(date_time)