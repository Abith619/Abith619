"""Write a program that prompts the user to enter a year and the first three letters of a month 
name (with the first letter in uppercase) and displays the number of days in the month. If the 
input for month is incorrect, display a message as shown in the following sample run: 
Enter a year: 2001
Enter a month: Jan 
Jan 2001 has 31 days 
Enter a year: 2016 
Enter a month: jan 
jan is not a correct month name"""
year=int(input("year = "))
month=input("month = ")
if year%4==0:
        year=('leap year')
if month in ['Sep', 'Apr', 'Jun', 'Nov']:
        print ("30")
elif month in ['Jan', 'Mar', 'May', 'Jul', 'Aug','Oct','Dec']:
        print ("31")        
elif month == 'Feb' and year == "leap year":
        print ("29")
elif month == 'Feb' and  year != "leap year":
        print ("28")
else:
    print("{month} name is Invalid")