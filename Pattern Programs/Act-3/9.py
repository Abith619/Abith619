# Subtract a week (7 days)  from a given any date in Python
import datetime
date = datetime.date(2015, 10, 10)
days = datetime. timedelta(7)
new_date = date - days
print(new_date)