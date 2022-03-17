"""from datetime import datetime
date_time_str = '18/09/19 01:55:19'
obj = datetime.strptime(date_time_str, '%d/%m/%y %H:%M:%S')
print(obj)"""
"""def Sum(myDict):
    list = []
    for i in myDict:
        list.append(myDict[i])
    final = sum(list)     
    return final
dict = {'a': 100, 'b':200, 'c':300}
print("Sum =", Sum(dict))"""
"""import calendar
from datetime import datetime
n=input()
datetime_object = datetime.strptime('n', '%d/%b/%Y')

month=calendar.monthrange(2008, 2)
print(month)"""
"""import datetime
now = datetime.datetime.now()
import calendar
print (calendar.monthrange(now.year, now.month)[1])"""

"""def leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False
def days_in_month(month, year):
    if month in {1, 3, 5, 7, 8, 10, 12}:
        return 31
    if month == 2:
        if leap_year(year):
            return 29
        return 28
    return 30
print(days_in_month(2, 2016)) """
