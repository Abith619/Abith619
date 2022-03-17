# Print a date in a the following format
# Day_name  Day_number  Month_name  Year
from calendar import day_name
import datetime 
from datetime import date, time
x = datetime.datetime.now()
print(x.strftime("%A"), x.day, x.strftime("%B"), x.year)