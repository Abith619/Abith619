"""Canada has three national holidays which fall on the same dates each year.
  Holiday                    Date
New year's day           January 1
Canada day               July 1
Christmas day           December 25
Write a program that reads a month and day from the user. If the month and day match one of the
holidays listed previously then your program should display the holiday's name. Otherwise your 
program should indicate that the entered month and day do not correspond to a fixed-date holiday.
HINT :
Canada has two additional national holidays, Good Friday and Labour Day, whose dates vary 
from year to year. There are also numerous provincial and territorial holidays, some of which 
have fixed dates, and some of which have variable dates. We will not consider any of these 
additional holidays in this exercise."""
from datetime import datetime
n=input("Enter mon day")
#new_years_day=datetime.date(2015, 1, 1).strftime('%B')

if n == "jan 1":
  print("New year's day")
elif n== "jul 1":
  print("Canada day")
elif n == "dec 25":
  print("Christmas Day")
else:
  print("The date you entered is not a Holiday")