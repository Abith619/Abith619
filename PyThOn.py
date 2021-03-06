import operator
import scipy
import re
from builtins import function
import copy
from hashlib import new
from typing import FrozenSet
import key as key
import numpy as np
import this
from attr import field
from django import db
from sympy import SymmetricDifference, intersection, print_python
from tensorflow.python.types.distribute import Iterable

"""dict = object  
list, tuple = array
str = string
int, float = number"""
#                                                                                       Date And Time
"""datetime - Allows us to manipulate times and dates together (month, day, year, hour, second, microsecond).
date - Allows us to manipulate dates independent of time (month, day, year).
time - Allows us to manipulate time independent of date (hour, minute, second, microsecond).
timedelta — A duration of time used for manipulating dates and measuring.
tzinfo — An abstract class for dealing with time zones."""
# import datetime class from datetime module
from datetime import datetime
#                                            get current date
datetime_object = datetime.now()
print(datetime_object)
print('Type :- ',type(datetime_object))
#   Getting Day of the Month and Day of the Week from a Date
import calendar
print('Day of Month:', my_date.day)
#                                                    to get name of day(in number) from date
print('Day of Week (number): ', my_date.weekday())
#                                                   to get name of day from date
print('Day of Week (name): ', calendar.day_name[my_date.weekday()])
#                                                                                              Getting Hours and Minutes
from datetime import datetime
todays_date = datetime.now()
#                                to get hour from datetime
print('Hour: ', todays_date.hour)
#                                 to get minute from datetime
print('Minute: ', todays_date.minute)
# Getting Week of the Year from a Datetime Object
# Return a 3-tuple,                                         (ISO year, ISO week number, ISO weekday)
todays_date.isocalendar()
todays_date.isocalendar()[1]
#                                                                                                       kwargs(**)
print("Program to demonstrate **kwargs for variable number of keywords:")
print("\n")
def concatenate(**kwargs):
    r = ""
    for arg in kwargs.values():
        r += arg
        return r
print("The concatenated value is displayed as follows:")
print(concatenate(a="kaashiv", b="Training", c="Institue"))
# arguments should also be the same as the number of keys in the dictionary
print("Another use of **kwargs:")
print("\n")
def print_values(**kwargs):
    for key, value in kwargs.items():
        print("The value of {} is {}".format(key, value))
print_values(my_name="Rahul", your_name="Ratan")
# *args to pass the elements to the function in an iterable variable
print("Program to demonstrate the *args is as follows:")
def func(a, b, c):
    print(a, b, c)
a = [1,2,3]
func(*a)
# 
print("Program to demonstrate the **kwargs used in function call is as follows:")
def func(a, b, c):
    print(a, b, c)
a = {'a': "one", 'b': "two", 'c': "three" }
func(**a)
#                                                                                                               JSON
p = '{"name": "Bob", "languages": ["Python", "Java"]}'
import json
#                                to parse JSON strings and files containing JSON object
person = '{"name": "Bob", "languages": ["English", "Fench"]}'
person_dict = json.loads(person)
#                   Output: {'name': 'Bob', 'languages': ['English', 'Fench']}
print( person_dict)
#                    Output: ['English', 'French']
print(person_dict['languages'])
with open('path_to_file/person.json') as f:
    data = json.load(f)
# Output: {'name': 'Bob', 'languages': ['English', 'Fench']}
print(data)
#                                                                   Convert to JSON string
person_dict = {'name': 'Bob',
'age': 12,
'children': None
}
person_json = json.dumps(person_dict)
# Output: {"name": "Bob", "age": 12, "children": null}
print(person_json)
{"name": "Bob", "languages": ["English", "Fench"], "married": True, "age": 32}
person_string = '{"name": "Bob", "languages": "English", "numbers": [2, 1.6, null]}'
#                                          Getting dictionary
person_dict = json.loads(person_string)
# Pretty Printing JSON string back
print(json.dumps(person_dict, indent = 4, sort_keys=True))
#                                                                                                             BeautifulSoup
# navigation, modifying, and searching of necessary files                    HTML and XML 
# used in tree parsing using your favorite parser,                                           web scraping
# Accessing the HTML Through a Webpage
import requests
URL = "www.kaashivinfotech.com/internship-in-chennai/"
r = requests.get(URL)
print(r.content)
#                                 Parsing of the Content HTML
import requests
from bs4 import BeautifulSoup
URL = "https://www.kaashivinfotech.com/internship-in-chennai/"
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html5lib' )
print = (soup.prettify())
# A Simple Quick Scrape:
import requests
from bs4 import BeautifulSoup
vgm_url = 'https://www.vgmusic.com/music/console/nintendo/nes/'
html_text = requests.get(vgm_url).text
soup = BeautifulSoup(html_text,'html.parser')
soup.findall() # is used in adventures of web scraping
# filter out all the MIDI files and understand how to download them
import re
import requests
from bs4 import BeautifulSoup
vgm_url = 'https://www.vgmusic.com/music/console/nintendo/nes/'
html_text = requests.get(vgm_url).text
soup = BeautifulSoup(html_text,'html.parser')
if __name__ == '__main__':
    attrs = {
        'href' : re.compile(r'\.mid$')
        }
tracks = soup.find_all('a', attrs=attrs, string=re.compile(r'^((?!\().)*$'))
count = 0
for track in tracks:
    print(track)
count += 1
print(len(tracks))
# donwload_track and calling the function to the above helps us to download the files through iterating all the MIDI files
import re
import requests
from bs4 import BeautifulSoup
vgm_url = 'https://www.vgmusic.com/music/console/nintendo/nes/'
html_text = requests.get(vgm_url).text
soup = BeautifulSoup(html_text,'html.parser')
def download_track(count, track_element):
    #                            Get the title of the track from the HTML element
    track_title = track_element.text.strip().replace('/','-')
    download_url = '{}{}'.format(vgm_url, track_element['href'])
    file_name = '{}_{}.mid'.format(count,track_title)
    #                                                    Download the track
    r = requests.get(download_url,allow_redirects=True)
    with open(file_name, 'wb') as f:
        f.write(r.content)
# Print to the console to keep track of how the scraping is coming along.
    print('Downloaded: {}'.format(track_title, download_url))
if __name__ == '__main__':
    attrs = {
        'href' : re.compile(r'\.mid$')
        }
tracks = soup.find_all('a', attrs=attrs, string=re.compile(r'^((?!\().)*$'))
count = 0
for track in tracks:
    print(track)
count += 1
print(len(tracks))
#                                                                                                  BufferedReader
import sys
import io
# a variable sourcefile is used to store the argument that is passed while running the script.
# Sys.argv is the argument taking the file name while executing the script and 1 indicates the argument number 
sourcefile = sys.argv[1] #the file is opened in binary mode to read using open function
with open(sourcefile, 'rb') as file:
#   file descriptor is obtained by making using of FileIO which is used to identify the file that is opened
    fi  = io.FileIO(file.fileno())
#   Buffered reader is then used to read the contents of the file
    fb = io.BufferedReader(fi)
#                    the contents of the file is printed
    print (fb.read(20))
#                                                                     buffered reader to read the contents of the file
filename = sys.argv[1] #the file is opened in binary mode to read using open function
with open(filename, 'rb') as file:
#   file descriptor is obtained by making using of FileIO which is used to identify the file that is opened
    fi  = io.FileIO(file.fileno())
#   Buffered reader is then used to read the contents of the file
fb = io.BufferedReader(fi)
#                               the contents of the file is printed
print (fb.read(20))
#                                                                                                                    Async
# function multiple operations without waiting time
import queue
def task(name, sample_queue):
    if sample_queue.empty():
        print(f'Task {name} has nothing to do')
    else:
        while not sample_queue.empty():
            cnt = sample_queue.get()
            total = 0
            for x in range(cnt):
                print(f'Task {name} is running now')
            total += 1
print(f'Task {name} is running with a total of: {total}')
def sample_async():
    sample_queue = queue.Queue()
    for work in [2, 5, 10, 15, 20]:
        sample_queue.put(work)
        tasks = [
                (task, 'Async1', sample_queue),
                (task, 'Async2', sample_queue),
                (task, 'Async3', sample_queue)
                ]
    for t, n, q in tasks:
        t(n, q)
    if __name__ == '__main__':
        sample_async()
# ‘task’ in the above example accepts string and queue
import asyncio
import functools
def event_handler(loop, stop=False):
    print('Calling event handler')
    if stop:
        print('Loop is being stopped')
        loop.stop()
    if __name__ == '__main__':
        loop = asyncio.get_event_loop()
        try:
            loop.call_soon(functools.partial(event_handler, loop))
            print('Loop is being started')
            loop.call_soon(functools.partial(event_handler, loop, stop=True))
            loop.run_forever()
        finally:
            print('Loop is being closed')
            loop.close()
# concurrent programming for single code to be executed independently
import asyncio
async def sample_task(task_seconds):
    print('Task takes {} seconds to complete'.format(task_seconds))
    await asyncio.sleep(task_seconds)
    return 'task has been completed'
if __name__ == '__main__':
    sample_event = asyncio.get_event_loop()
try:
    print('Creation of tasks started')
    task_object_loop = sample_event.create_task(sample_task(task_seconds=3))
    sample_event.run_until_complete(task_object_loop)
finally:
    sample_event.close()
    print("Task status: {}".format(task_object_loop.result()))
# Event loop countdown() coroutine calls, executes until yield from, and asyncio.sleep() function
import asyncio
@asyncio.coroutine
def countdown(number, n):
    while n > 0:
        print('Counter of ', n, '({})'.format(number))
        yield from asyncio.sleep(1)
        n -= 1
loop = asyncio.get_event_loop()
tasks = [
    asyncio.ensure_future(countdown("First Count", 2)),
    asyncio.ensure_future(countdown("Second Count", 4))]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()



#                                                                                                  Contextlib Module
from contextlib import contextmanager


@contextmanager
def open_file(path, mode):
    the_file = open(path, mode)
    yield the_file
    the_file.close()
files = []
for x in range(100000):
    with open_file('foo.txt', 'w') as infile:
        infile.write('Hello Abith')
    for f in files:
        if not f.closed:
            print('not closed')
files =open('foo.txt', 'r+')
contents = files.read()
print(contents)
#                                        Nested Implementation
import contextlib


@contextlib.contextmanager
def multicontext(ctxt):
    print ('entering contents:', ctxt)
    yield ctxt
    print('exiting contents:', ctxt)
    with contextlib.nested(multicontext('kaashiv'), multicontext('Training'), multicontext('Intitute')) as (X, Y, Z):
        print('inside with statement:', X, Y, Z)
#                                                   Class-based approach
from contextlib import ContextDecorator


class htmlparagraph(ContextDecorator):
    def __enter__(self):
        print('')
        return self
    def __exit__(self, *exc):
        print('')
        return False
@htmlparagraph()
def emit_html():
    print('Here is some non-HTML ')
    emit_html()
#                                                   Closing open handles
import contextlib


class contxt(object):
    def __init__(self):
        print ('inside the init() method')
    def close(self):
        print ('inside the close() method')
with contextlib.closing(contxt()) as ctxt:
    print ('inside the with statement')
print()
print ('Error handling:')
try:
    with contextlib.closing(contxt()) as ctxt:
        print ('  raising from inside the with statement')
        raise RuntimeError('There is a runtime error')
except Exception as err:
    print('  Had an error:' , err)
#                                                                 # creating username from user's first and last name
# list containing users name
names = ['john garner',  'karen bag', 'neil amster', 'jason smith', 'richard king', 'david klok'] # empty list which will contain usernames
username = [] # defining function for creating username
def uname(names):
    for i in names:
        full_name=i.split()  # split the name on occurrence of whitespace chars
        fname = full_name[0]
        lname = full_name[1] # concatenating first 3 chars of first name with first 3 chars of last name to create username
    uname = fname[:3]+lname[:3]     # extracting substrings from fname and lname
    username.append(uname)
# calling function uname() taking list “names” as input argument
    uname(names)
# printing name of the user along with username
print("Name                Username")
for name,uname in zip(names, username):
    print(name, '------->', uname)
#                                                                                      Program to check eligibility to vote
valid_voters = [] # defining function to test if entered age is above 18 or not
def eligible_vote(i):
    for age in i:
        if age >= 18 :
            valid_voters.append(age)            # Calling function
            eligible_vote((12, 21, 18, 23, 9, 55, 82, 69, 14, 32, 10, 55)) # Printing results
print("these are the eligible voters")
for voter in valid_voters:
    print("person with age",voter,"is a valid one")
# Function to test a person age > 18 or not --> first argument for                                           filter()
def eligibility(age):
    if age >= 18:
        return True
    else:
        return False
    # List of all voters --> second argument for filter()
all_voters = [12, 21, 18, 23, 9, 55, 82, 69, 14, 32, 10, 55]
eligible_voters =filter(eligibility , all_voters)
print("these are the eligible voters")
for voter in eligible_voters:
    print("age",voter,"is a valid one")
#                                        List of all voters --> second argument for filter()
all_voters = [12, 21, 18, 23, 9, 55, 82, 69, 14, 32, 10, 55]
eligible_voters =filter(lambda age : age >=18 , all_voters)
print("these are the eligible voters")
for voter in eligible_voters:
    print("age",voter,"is a valid one")
#                                             filter out vowels from the input list of alphabets.
count_vowel = 0  # to track no. of vowels
count_consonant = 0 # no. of consonants
alphabets = ['a', 'b', 'U', 'd', 'e', 'i', 'j', 'o', 'x', 'A', 'Z', 't'] # Function to filter out vowels
def filterVowels(alpha):
    vowels = ['a', 'e', 'i', 'o', 'u']
    if(alpha.lower() in vowels): # lower() is used to lowercase elements
        return True
    else:
        return False
filter_vowel = filter(filterVowels, alphabets)
print('The filtered vowels are:')
for vowel in filter_vowel:
    count_vowel += 1
print(vowel)
print("total number of alphabets in the list :",len(alphabets))
print("total number of vowels in the list :",count_vowel)
print("total number of consonants in the list :",len(alphabets) - count_vowel)
#                                                            function to check divisibility by 6
def div_six(x):
    if x % 6 == 0:
        return True
    else :
        return False
num_list = [10, 120, 30, 50, 90, 180, 72, 24, 88, 112]
result1 = filter(div_six, num_list)
print("numbers divisbile by 6:")
for num in result1:
    print(num)
#                     without the filter function
# a random list
input_list = [(), 100, 7, 'a', 0, False, True, {}, '0', []]
filtered_list = filter(None, input_list)
print('The filtered elements are:')
for item in filtered_list:
    print(item)
#                                                    using lambda function
result2 = filter(lambda x : x % 6 == 0, num_list)
print("using lambda : numbers divible by 6 :")
for num in result2:
    print(num)

#                                                                                                         If Main
# Execution Modes = Directly executing the Python file.
# Importing an external Python file as a package and then using the function from that file
# assign “__main__” to __name__
import numpy as np


def get_square(number):
    print("The square of {} is :".format(number))
    square = np.square(number)
    return square
print("Using function :")
square=get_square(5)
print(square)
#              “__name__” to control the execution of our code
def main():
    print("Programming in Python is fun!!!")
if __name__== "__main__" :
    main()
# 
def get_square(number):
    print("Inside the first function")
    print("The square of {} is :".format(number))
    square = np.square(number)
    return square
def main(number):
    print("Inside the main function")
    square_root = np.sqrt(number)
    print("The square root of {} is {}".format(number,square_root))
    square = get_square(number)
    print(square)
if __name__ == "__main__":
    main(5)
"""Inside the main function
The square root of 5 is 2.23606797749979
Inside the first function
The square of 5 is :
25"""
def get_square(number):
    print("Inside the square function")
    print("The square of {} is :".format(number))
    square = np.square(number)
    return square
def get_square_root(number):
    print("Inside the square root function")
    print("The square root of {} is :".format(number))
    square_root = np.sqrt(number)
    return square_root
def main(number):
    print("Inside the main function")
    square_root = get_square_root(number)
    print(square_root)
    square = get_square(number)
    print(square)
if __name__ == "__main__":
    main(5)
#                                         declare the Python Main Function
print('Introduction to main() function')
def main():
    print("This is main function")
print('Outside main function')
def function():
    return 19, 'Abith', 619
roll, name, score = function()
name
def sum(a,b):
    return (a+b)
print(sum(3,6))
print("__name__ variable set to ",name)
"""__name__=='__main__':
name = Abith"""
print("Main function illustration")
def sum(a,b):
    return (a+b)
def main():
    print("Inside main() function")
x=int(input("enter value x"))
y=int((input("enter value y")))
print("sum of values entered is",end=' ')
print(sum(x,y))
if __name__ == "__main__":
    main()
#                                                                                                         stream
asyncio=asyncio
asyncio.open_connection()
asyncio.create_connection()
asyncio.open_connection(host, port, *, loop, limit, **kwds)
asyncio.start_server() #                                       start socket server
asyncio.start_server(client_connected_cb, host, port, loop, limit)
asyncio.client_connected_cb
asyncio.loop.create_server()
# path parameter for using path-like objects
"""open_unix_connection()
start_unix_connection()
class asyncio.StreamReader( limit, loop)
whitelines()  # used to write a list of lines
writing ()
get_extra_info()
write_eof() # = close the write of the transport at the end of the file after flushing all the buffer data from the transport
can_write_eof() # Trur or False
close()"""
#                                                                                 Access Modifiers(_)
# define parent class Company
class Company:
    # constructor
    def __init__(self, name, proj):
        self.name = name      # name(name of company) is public
        self._proj = proj     # proj(current project) is protected
    # public function to show the details
    def show(self):
        print("The code of the company is = ",self.ccode)
# define child class Emp
class Emp(Company):
    # constructor
    def __init__(self, eName, sal, cName, proj):
        # calling parent class constructor
        Company.__init__(self, cName, proj)
        self.name = eName   # public member variable
        self.__sal = sal    # private member variable
    # public function to show salary details
    def show_sal(self):
        print("The salary of ",self.name," is ",self.__sal,)
# creating instance of Company class
c = Company("Stark Industries", "Mark 4")
# creating instance of Employee class
e = Emp("Steve", 9999999, c.name, c._proj)
print("Welcome to ", c.name)
print("Here ", e.name," is working on ",e._proj)
# only the instance itself can change the __sal variable
# and to show the value we have created a public function show_sal()
e.show_sal()
#                                                                                                         Map Function
def function():
    return 19, 'Abith', 619
roll, name, score = function()
name
# 
def SquareOf_Num(a):
    return a*a
list_numbers = (5, 10, 15, 20)
result = map(SquareOf_Num, list_numbers)
print(result)
#                                        map object to a set conversion
Square_numbers = set(result)
print(Square_numbers)
#                                       Lambda expressions in the map()
list_ = (1, 2, 3, 4)
ans = map(lambda a: a*a, list)
print(ans)
#map object to  set conversion
squarenum = set(ans)
print(squarenum)
#                                                                                                                Loops
"""myList = [8, 9, 2, 6, 1, 9]
for i in myList:
    print (i)   

bigList = [[1, 3, 6], [8, 2,], [0, 4, 7, 10], [1, 5, 2], [6]]
for i in bigList:
	for j in i:
		print("Element of list within a list - ", j)
#                                                           if True execute continously
while True:
	print ("I am printing because the condition is True")
#                                                                          infinite loop
myList = [8, 9, 2, 3, 4, 6]
i = 0
while i < len(myList):
    print (myList[i])
    i = i+1
#                                                                               continue
#                       Print LowerCase Letter
name = "Abith"
for i in name:
    if not i.islower():
        continue # Altering the Loop
    print(i)
#                                                                                  Break
for i in name:
	if i == "A":
		break
print (i)
"""
#                                                                                               argparse
import argparse
parser = argparse.ArgumentParser(description='Understand functioning')
parser.add_argument('-x', action="store_true", default=False)
parser.add_argument('-y', action="store", dest="y")
parser.add_argument('-z', action="store", dest="z", type=int)
print (parser.parse_args(['-x', '-yval', '-z', '3']))

parser = argparse.ArgumentParser(description='How argparse() deals with Long option names')
parser.add_argument('--noargument', action="store_true", default=False)
parser.add_argument('--withargument', action="store", dest="witharg")
parser.add_argument('--withargument2', action="store", dest="witharg2", type=int)
print (parser.parse_args([ '--noargument', '--withargument', 'val', '--withargument2=3' ]))
#                                                                                                Lambda()
# Anonymous functions are tagged as lambda functions
a = (lambda z: z+5)(2)
print(a)
Anonymous_add_function = lambda x, y : x + y
print(Anonymous_add_function(2, 3))
#                                   Lambda with python map() function
map(lambda x : x*2, [1, 2, 3, 4])
dict_a = [{'name': 'python3', 'points': 9}, {'name': 'java', 'points': 7}]
list_a = [1, 2, 3]
list_b = [11, 21, 31]
a=map(lambda x : x['name'], dict_a) 
# Output: ['python3', 'java'] b=map(lambda x : x['points']*10,  dict_a) # Output: [90, 70] c=map(lambda x : x['name'] == "python3", dict_a) # Output: [True, False] d=map(lambda x, y: x + y, list_a, list_b) # Output: [12, 23, 34] print(a,b,c,d)
listing_a = [1, 3, 2, 4, 1]
dictionary_a = [{'name': 'python3', 'points': 11}, {'name': 'java', 'points': 9}]
a = filter(lambda x : x['name'] == 'python', dictionary_a)
print(a)
b = filter_obj = filter(lambda x: x % 2 == 0, listing_a) # filter object
print(b)
even_num = list(filter_obj) # Converts the filer obj to a list
print(even_num)
#                                                                                              format() Function
x = format(255, 'b') # ‘b’ represents binary form
print(x)
x = format(0.08, '%') # 8.000000%
print(x)
x = format(255, 'o')
print(x)
#                        % is associated with the data type
emp_name = 'Leo Shein'
emp_age = 24
print("Name: %s Age:%d"%(emp_name,emp_age))
#                         {} is a placeholder irrespective of the data type
emp_name = 'Leo Shein'
emp_age = 24
print("Name: {} Age: {}".format(emp_name,emp_age))
# index
emp_name = 'Leo Shein'
emp_age = 24
print("Name: {0} Age: {1}".format(emp_name,emp_age))
# 
print("Hello {0}, your balance is {abc}.".format("Fina", abc=230.2346))
print("{:6d}".format(12))
print("{:06d}".format(12))
print("{:+f} {:+f}".format(21.99, -22.99)) # This will show the + sign
print("{:-f} {:-f}".format(21.99, -22.99)) # This will show the - sign only
print("{:6}".format("dog")) # string-padding with                  left-alignment
print("{:>6}".format("dog")) # string-padding with                   right-alignment
print("{:^7}".format("dog")) # string-padding with                 center-alignment
# Format Class members
class Employee:
    id = 41
    name = "Prince"
print("{p.name}'s company ID is: {p.id}".format(p=Employee())) # format name and id
#                                                                Truncate String using the format()
print("{:.5}".format("Singapore"))
print("{:^7.3}".format("Singapore"))# truncating strings to 3 letters, and then padding & center-aligned
#                                                                                                            Extend()
import array as arr
arr1 = arr.array('i', [1,2,3,4])
arr2 = arr.array('i', [5,6,7])
arr1.extend(arr2)
print(arr1)
a = [1,2,3,4,5]
b = [6,7]
a.extend(b)
print(a)
a = [2010,2011,2012]
b = ['john','doe',2013]
a.extend(b)
print(a)
a = [2010,2011,2012]
a.extend("John")
print(a)
#                                                                                                             super()
class ParentClass(object):
    def __init__(self):
        print("This is Base class")
        pass
class ChildClass(ParentClass):
    def __init__(self):
        ParentClass.__init__(self)
c1 = ChildClass()
# super() in                           multiple inheritances
class ParentClass1(object):
    def __init__(self):
        print("This is Base class 1")
pass
class ParentClass2(object):
    def __init__(self):
        print("This is Base class 2")
pass
class ChildClass(ParentClass1,ParentClass2):
    def __init__(self):
        super(ChildClass, self).__init__()
c1 = ChildClass()
# parent and child class to attributes and methods
class ParentClass:
    def __init__(self):
        self.parent_attribute = 'I am a parent'
    def parent_method(self):
        print('Good old days')
class ChildClass(ParentClass):
    def __init__(self):
        super().__init__()
        self.child_attribute = 'I am a child'
    def child_method(self):
        print('New is awesom')
# Create instance of child class i.e. "ChildClass"
child = ChildClass()
# Print attributes and methods of child class
print(child.child_attribute)
print(child.parent_attribute)
child.parent_method()
child.child_method()
#                                                        Multiple resolution orders
class BB:
    def check(self):
        print('This is b')
class CC:
    def check(self):
        print('This is c')
class DD(BB, CC):
    def check(self):
        print('This is d')
d_inst = DD()
d_inst.check()
#                                                                                                  PEP8-Naming Conventions
class ClassName: #Class naming rule
    C = 1 #Constat naming rule
    the_variable = 2020; # variable naming rule
    print("The constant value is:", C)
    def the_method(self): # method naming rule
        print("I'm inside class ")
    def insideclass(self):
        print("The Variable: ",ClassName.the_variable)
        self.the_method()
n = ClassName()
n.insideclass()
#                                                                                                           Return Value
#                                 Function to convert the temperature from Celcius to Fahrenheit
def temp_converter (Temp_Celsius):
    return(Temp_Celsius* 9 / 5) + 32
#                                   Main from where the function "temp_converter" is called
for temp_Celsius in (20, 25, 30, 40):
    print(temp_Celsius, ": ", temp_converter (temp_Celsius))
def square(x,y):
    return x*x, y*y
t = square(2,3)
print(t)
def min_val(x,y):
    if x < y :
        return x
    else :
        return y
print( min_val(5,8) )
print( min_val(52,8) )
#                                                                                       yield Statement
def yield_function():
    yield 10
    yield 20
    yield 30
for y in yield_function():
    print(y)
# 
def yield_func():
    n = range(3)
    for i in n:
        yield i*i
gen = yield_func()
print(gen)
for i in gen:
    print(i)
# generating generator objects and printing the return values using a loop
def gen_func():
    x = 0
    while x < 5:
        yield x
    x += 1
print("Simple function call without using loop:\n")
print(gen_func())
print("Below is with using a loop:")
for y in gen_func():
    print(y)

def yield_func(l):
    total = 0
    for n in l:
        yield total
    total += n
new_lst = yield_func([10,20,30])
print(next(new_lst))
print(next(new_lst))
print(next(new_lst))
#                                                                                                                Pickle
import pickle
pickle.dump()
pickle.load()
#                                           number of input data to take
n = int(input("Enter the number of items "))
data = []  # input list
#                           adding items to the list
for d in range(n):
    item = input("Enter data :" + str(d+1)+': ')
data.append((item))
#                             open a file where data need to be stored
file = open('list.pkl', 'wb')
#                           dump information to the file
pickle.dump(data, file)
#                       close the file
file.close()
print('\n')
print('<-------------------Un-Pickling----------------------->')
#                                 open the file where data is dumped
fileo = open('list.pkl', 'rb')
#                              loading data
datao = pickle.load(fileo)
#                         close the file
fileo.close()
#             showing pickled data
print("showing data pickled")
for i in datao:
    print(i)
#                                    creating python object --> dictionary
dictionary = {1: 'monday', 2: 'tuesday', 3: 'wednesday', 4: 'thursday', 5: 'friday', 6: 'saturday', 7: 'sunday'}
print('<--------------Pickling----------------->')
#                                  open a file where to store dictionary
print("dictionary to be stored:")
print(dictionary)
file = open('dictionary.pkl', 'wb')
pickle.dump(dictionary, file) # storing dictionary into file
#               closing file
file.close()
print('\n')
print('<---------------Un-pickling-------------->')
fileo = open('dictionary.pkl', 'rb')
dicto = pickle.load(fileo)
fileo.close()
print("displaying dictionary data")
for key, item in dicto.items():
    print(key, '-->', item)
#                                    pickling of python functions
# creating python object --> function()
def add(a, b):
    return (a+b)
#                opening file to store the add()
file = open('function.pkl', 'wb')
pickle.dump(add, file)
#                      closing file
file.close()
#                                   unpickling
fileo = open('function.pkl', 'rb')
addition = pickle.load(fileo)
fileo.close()
#                                    calling function
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
print("Sum of numbers entered is :", addition(x, y))
#                                                                                                   Filter() Function
#                                     Filtering values above average
import statistics
data = [1,3,5,7,11,17] #The short list of data is collected from a nearby fuel sensor.
avg= statistics.mean (data)
new =filter(lambda x : x > avg, data)
print(new)
new =list(filter(lambda x: x>avg, data))
print(new)
#                                      filters out odd and even numbers.
Fibnocci = [0,1,1,2,3,5,8,12,21,34,55]
odd_numbers = list (filter (lambda x : x %2, Fibnocci))
print (odd_numbers)
even_numbers = list (filter(lambda x : x%2 == 0, Fibnocci))
print(even_numbers)
# when the                                           None value is passing the parameter
# filters out data based on whether the element is True or False and returns accordingly
New_list = [0, 1, 'a', 'B', False, True, '0', '4']
filtered_list = filter (None, New_list)
print('Filtered elements')
for element in filtered_list:
    print(element)
#                                                                                                                max()
#Program to illustrate max() functionality, when key is set to some function
# Input --> list of strings
inp = ['John', 'Rob', 'Karen', 'Diana', 'Emanual', 'Alexnder', 'Tina']
print("input -->", inp)
def length(item):
    return len(item)
# Key function -->                       len()
print("Using user defined function")
print("max: ", max(inp, key = length))
# This can be implemented using built-in function                len()
print("Using built-in function")
print("max: ", max(inp, key = len))
#                               Using lambda function
print("Using lambda function")
print("max: ", max(inp, key = lambda item : len(item)))
# Input -->                                          multiple iterables
x = [10, 20, 30] y = [5, 10, 15, 20, 25]
print("max among x and y :", max(x, y, key = len))
print("max among x and y :", max(x, y))

def sum_digits(num):
    sum = 0
    while(num > 0):
        rem = num % 10
        sum = sum + rem
        num = num
        return sum
# Input --> list of                                         positive integers
inp = [120, 20, 42, 212, 802, 139, 175, 802, 468]
print("Input List = ", inp)
print("Maximum Value in the List = ", max(inp, key = sum_digits))
inp = []
print("input:", inp)
print(max(inp, default=0))
#                                                                                                   sleep()
import time
print("Simple program to demonstrate sleep function:")
print("The Start time is as follows : ")
print(time.ctime())
time.sleep( 5 )
print("The End time is as follows:" )
print(time.ctime())
# A dramatic way of printing the given message or String
import time
print("Program to demonstrate sleep() function used for printing words letter by letter:")
strn = "kaashiv"
print("The given word is as follows:")
print(strn)
for i in range(0, len(strn)):
    print(strn[i], end ="")
time.sleep(0.3)
# for multithreading as the sleep() function is used to stop the current thread’s execution
import time
from threading import Thread
class Worker(Thread):
    def run(self):
        for x in range(0, 12):
            print(x)
time.sleep(1)
class Waiter(Thread):
    def run(self):
        for x in range(100, 103):
            print(x)
time.sleep(5)
print("Starting Worker Thread will start from :")
Worker().start()
print("Starting Waiter Thread will stop at:")
Waiter().start()
print("Done")
#                                                                                               Power Function
base = int(input("Enter base:"))
power = int(input("Enter power:"))
n = 1
for i in range(1,power+1):
    n=base*n
print ("The value of",base,"**",power," is",n)
result = pow(base,power)
print(math.pow(base,power))
print(np.power(base,power))
print(scipy.power(base,power))
#                                                                                                           Function Generator
class power_two:
    def _init_(self, max = 0 ):
        self. max = max
    def _iter_(self):
        self.n = 0
        return self
    def _next_(self):
        if self.n > self. max:
            raise StopIteration
        result = 2 ** self.n
        self.n+=1
        return result
# generator function instead of a normal function in a few lines.
def power_two(max = 0 ):
        n = 0
        while n < max:
            yield 2 ** n
        n+=1
#                                Implement Python Function Generator
def generator_funciton():
    a = 1
    print("First value")
    yield a
    a += 1
    print("Second value")
    yield a
    a += 1
    print("Third value")
    yield a
for x in generator_funciton():
    print(x)
# throw() method is used to throw exceptions with the generator
def infinite_palindromes():
    num = 0
    while True:
        if is_palindrome(num):
            i = (yield num)
        if i is not None:
            num = i
            num += 1
def is_palindrome(num):
#                           Skip single-digit inputs
    if num // 10 == 0:
        return False
    temp = num
    reversed_num = 0
    while temp != 0:
        reversed_num = (reversed_num * 10) + (temp % 10)
        temp = temp // 10
    if num == reversed_num:
        return True
    else:
        return False
""" pal_gen = infinite_palindromes()
    for i in pal_gen:
        print(i)
        digits = len(str(i))
        if digits == 5:
            pal_gen.throw(ValueError("We don't like large palindromes"))
        pal_gen.send(10 ** (digits))"""
#                                          yield a series of values from huge data sets like a number of rows
"""def csv_reader(“article.txt”):
    for row in open(“article.txt”,”r”):
        yield row
generator_csv = csv_reader(“article.txt”)
count_rows = 0
for rows in generator_csv:
    count_rows+= 1
    print(“Count of number of rows”, count_rows)"""
#                                                                                                                   Parser
#                                        parsing the given expressions
import parser
print("Program to demonstrate parser module in Python")
print("\n")
exp = "5 + 8"
print("The given expression for parsing is as follows:")
print(exp)
print("\n")
print("Parsing of given expression results as: ")
st = parser.expr(exp)
print(st)
print("\n")
print("The parsed object is converted to the code object")
code = st.compile()
print(code)
print("\n")
print("The evaluated result of the given expression is as follows:")
res = eval(code)
print(res)
#                                                               argparse
#  command-line options and arguments using an argparse module
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("ls")
args = parser.parse_args()
print(args.ls)
#                                                                                                                  SystemExit
print("Program that uses SystemExit as Exception instead of BaseException.")
try:
    raise SystemExit
except SystemExit:
    print("Specifying SystemError exception in this block works.")
#                                                  os._exit(), sys.stdin
import sys
print("Program to demonstrate sys.exit() function")
limit = 15
if limit < 18:
    sys.exit("Numerical limit less than 18")
else:
    print("Numerical limit is not less than 18")
#                                                                                                                  Zip Function
name = [ "Hemanth", "Anjum", "Ramya", "Saira" ]
id_no = [ 111, 92, 137, 103 ]
score = [ 40, 50, 60, 70 ] # Mapping values using zip()
mapping = zip(name, id_no, score)
#                      A set of values print after conversion
mapping = set(mapping)
#                     resultant values are printed
print ("The zipped values are : ",end="")
print (mapping)

coordinate_plane = ['x', 'y', 'z']
val = [13, 14, 15]
res = zip(coordinate_plane, val)
res_list = list(res)
print(res_list)
c, v =  zip(*res_list)
print('c =', c)
print('v =', v)

texts   = ("Baker Street", "Golden Ratio", "Room")
numbers = (221.5,           1.61803,        237)
result  = zip(texts, numbers)
print(result)
result_tuple = tuple(result)
print("Zipped Tuples: ",result_tuple)
print("Äddress 1: ",result_tuple[0][0], result_tuple[0][1])
t, n = zip(*result_tuple)
print("Texts: ",t)
print("Numbers: ",n)
#                                                                  Unzipping Values
numList = [1558, 1884, 1111]
strList = ['one', 'two', 'three']
A_output = zip(numList, strList)
print(A_output)
a, b = zip(*A_output )
print('numList = ', a)
print('strlist = ', b)
#                                                                                                                  File Methods
"""r: This mode opens a file in read-only form
w: This mode opens a file in the write-only form
r+: This mode opens a file in both reads and writes form
w+: This mode opens a file in both write and read
a: This mode opens a file for appending purpose
a+: This mode opens a file for both appending as well as for reading"""
# open(), read(), readline(), next(), write(), writelines(), truncate(), seek() and close()
# read() = reading the full file in the form of a string
# Readline() = reading only the first line of the file or reading line until it meets an EOF character in the file
# Next() = while iterating a file through a loop, akes the next line.
ff = open("/run/media/abith/Abith/py/Hello.txt", "r")
print(ff.next())
print(ff.next())
#                      file.write() = 
"""“x”: This is for creating a file. If the file exists with that name, an error will be thrown
“a”: This is for appending. If a file doesn't exist, it will create that file
“w”: This will create that file if the file doesn't exist and then write to it"""
# truncate() = 
ff = open("C:/Users/Test/desktop/sample_Kaashiv.txt", "r+")
print(ff.read())
ff = open("C:/Users/Test/desktop/sample_Kaashiv.txt", "w+")
ff.truncate()
ff = open("C:/Users/Test/desktop/sample_Kaashiv.txt", "r+")
print(ff.read())
#                                                            File Handling Operations
myFile = 5
myFile.readline()
for line in myFile:
    # will print all the lines one by one
    print(line)
content = []
for line in myFile:
    content.append(line)
myFile.write("Hello, World. I am learning Python")
content = ["Python 2.x\n", "Hello, World. I am learning Python"]
#                                                                               Tell and Seek
myFile = open('file.txt','r+')
myFile.seek(5)
myFile.read()
', World!'
myFile.tell()
#                                                                               Copying a File
file1 = open("original.txt", "r")
file2 = open("duplicate.txt", "w")
l = file1.readline()
while l:
    file2.write(l)
l = file1.readline()
file1.close()
file2.close()
#                                                                                      Seek()
# to set the offset position, of the reading and writing pointer
ff.seek(0)
#                                                                                                   Sub-String
statement = "Coding in Python is fun."
start_index = 0
end_index = 7
print("Original Text :",statement)
length_statement = len(statement)
print("Length of the string",statement,"is",length_statement)
print("Character at",start_index,"th position :",statement[start_index])
print("Character at",end_index,"th position :",statement[end_index])
substring = statement[start_index:end_index]
print("Substring :",substring)
#                                     naïve approach  of  Sub-String
statement = "Coding in Python is fun."
length_statement = len(statement)
for i in range(length_statement-1):
    if(i<7):
        print(statement[i], end="")
#                                        End string as blank
start_index = 4
print("The substring of the statement starting from the \n", start_index,"th index position till the end :",
statement[start_index:])
#                                       Start index as blank
statement = "Coding in Python is fun."
end_index = 16
print("The substring of the statement ending at from the \n",end_index-1,"th index position from the start :",
statement[:end_index])
#                                           Start and End index with step
start_index = 0
end_index = 16
step = 2
print("The substring of the statement starting from \n",start_index,"th index position and ending at the",end_index-1,
"th index position with step",step," :",statement[start_index:end_index:step])
#                                                                             Reversing a string using substring
statement = "Coding in Python is fun."
string_length = len(statement)
print("The reverse of the string",statement,"\n using substring :",statement[string_length::-1])
#                                                                                                                Built-in Functions
# abs(x) for fetching the absolute value of x, bin() for getting the binary value,  reversed() for reversing the order
# bool() for retrieving the boolean value of an object, list() for lists, len() to get the length of the value, 
# open() to open the files, pow() for returning the power of a number, # sum() for fetching the sum of the elements
#                                                                        abs(x) = Returns absolute value of a number
a = 12
b = -4
c = 3+4j
d = 7.90
print(abs(a))
print(abs(b))
print(abs(c))
print(abs(d))
#                                                                          all(x)
# it will return true if all variables in the iterator are true, iterable objects = tuple, lists, dictionary.
tuple = (0, True, False)
x = all(tuple)
print(x)
#                                                                          bin()
# returns the binary value for the number passed in the argument
a=5
print(bin(a))
print(bin(4))
print(bin(9))
#                                                                         round()
print(round(4.5))
print(round(-7.7))
#                                                                         bool()
print(bool(0))
print(bool(-4.5))
print(bool(None))
print(bool("False"))
#                                                                        bytearray()
bytearray(source,encoding,errors)
# This function returns a new array of bytes, i.e. a mutable sequence of integers from range 0 to 256
print(bytearray())
print(bytearray('Python','utf-8'))
#                                                                        compile()
Compile(source,filename,mode,flags=0,dont_inherit=False,optimize=-1)
#  to generate a Python code object from a string or an AST object.
myCode = 'a = 7\nb=9\nresult=a*b\nprint("result =",result)'
codeObject = compile(myCode, 'resultstring', 'exec')
exec(codeObject)
#                                                                        list()
print(list()) #returns empty list
stringobj = 'PALINDROME'
print(list(stringobj))
tupleobj = ('a', 'e', 'i', 'o', 'u')
print(list(tupleobj))
listobj = ['1', '2', '3', 'o', '10u']
print(list(listobj))
#                                                                        len()
stringobj = 'PALINDROME'
print(len(stringobj))
tupleobj = ('a', 'e', 'i', 'o', 'u')
print(len(tupleobj))
listobj = ['1', '2', '3', 'o', '10u']
print(len(listobj))
#                                                                        max()
num = [11, 13, 12, 15, 14]
print('Maximum is:', max(num))
#                                                                        min()
print(min(2,5,3,1,0,99))
sampleObj = ['B','a','t','A']
print(min(sampleObj))
#                                                                        map()
numList = (11, 21, 13, 41)
res = map(lambda x: x + x, numList)
print(list(res))
#                                                                       open()
f = open("myFile.txt", "r") #  read mode
print(f.read())
#                                                                        pow()
print(pow(2,-3))
print(pow(2,4.5))
print(pow(3,0))
#                                                                        oct()
# to generate the octal representation of a number
print("The octal representation of 32 is " + oct(32))
print("The octal representation of the ascii value of 'A' is " + oct(ord('A')))
print("The octal representation of the binary of 32 is " + oct(100000))
print("The octal representation of the binaryof 23 is " + oct(0x17))
#                                                                       sorted()
sampleObj = (3,6,8,2,5,8,10)
print(sorted(sampleObj,reverse=True))
sampledict = {'a':'sss','g':'wq','t':2}
print(sorted(sampledict,key= len))
#                                                                       sum()
num = [2.5, 3, 4, -5]
numSum = sum(num)
print(numSum)
numSum = sum(num, 20)
print(numSum)
#                                                                       str()
print(str('A1323'))
b = bytes('pythön', encoding='utf-8')
print(str(b, encoding='ascii', errors='ignore'))
# errors = 'ignore', helps interpreter to ignore when it found a non Ascii character
#                                                                       type()
# used for debugging purposes.
tupleObj=(3,4,6,7,9)
print(type(tupleObj))
new1 = type('New', (object, ),
dict(var1 ='LetsLearn', b = 2029))
print(type(new1))
#                                                                      callable()
def myFun():
    return 5
res = myFun
print(callable(res)) #            function is called to get this value
num1 = 15 * 5
print(callable(num1))#no function is called
#                                                                     input()
#                                                                     range()
res = 1
for i in range(1, 10,2):
    res = res * i
    print("multiplication of first 10 natural number :", res)
#                                                                    reversed()
tupleObj=(3,4,6,7,9)
for i in reversed(tupleObj):
    print(i,end=' ')
#                                                                  Absolute Value
def absolute_value(number):
    if(number<0):
        abs_num = -number
    else:
        abs_num = number
        return abs_num
print("The absolute value of 1 is {}".format(absolute_value(1)))
#                                                                Passing zero value
print("The absolute value of 0 is {}".format(absolute_value(0)))
#                                                                                                        Abs()
print("The absolute value of -1 is {}".format(abs(-1)))
print("The absolute value of -4.2 is {}".format(abs(-4.2)))
print("The absolute value of 3+4j is {}".format(abs(3+4j)))
bin_num = 0b0101010011 #               to find the absolute value of a binary number
print("The absolute value is {}".format(abs(bin_num)))
oct_num = 0o75 #                       to find the absolute value of a octal numbe
print("The absolute value of is {}".format(abs(oct_num)))
hex_num = 0xFFC6F3 #                   to find the absolute value of a hexadecimal number
print("The absolute value of is {}".format(abs(hex_num)))
#                                                                                                           count()
# Python program to count the number of times an object occurs in the list of integers
list1 = [ 1 , 1 , 1 , 2 , 3 , 2 , 1 , 23 , 43 , 54 , 4 , 5 ,65 , 67 , 76 , 54 , 34 , 2 , 4 ,5 , 6 , 6 , 6, 7 , 8 , 9]
# Count() function as an attribute to count the number of times the numeral 6 occours in the list1
print(list1.count(6))
# number of times an object occurs in the list of chars
list1 = [ 'e' , 'r' , 't' , 'e' , 'r' , 't' ,  'e' , 'r' , 't' ,  'e' , 'r' , 't' , 'e' , 'r' , 't' , 'e' , 'r' , 't' , 'e' ,
'r' , 't' , 'e' , 'r' , 't' , 'e' , 'r' , 't' , 'e' , 'r' , 't' , 'e' , 'r' , 't' , 'e' , 'r' , 't' , 'e' , 'r' , 't' ,
'e' , 'r' , 't' ,'e' , 'r' , 't' , 'e' , 'r' , 't' , 'e' , 'r' , 't' , 'e' , 'r' , 't'  ] 
# Count() function as an attribute to count the number of times two elements occours in the list1
print(list1.count('e'))
print(list1.count('z'))
# count the number of times an object occurs in the list of string
list1 = [ 'edu' , 'cba' ,  'learn' , 'ca' , 'na'  ] # Count() function as an attribute to count the number of times two elements occours in the list1
print(list1.count('edu'))
#                                                                                                                   CSV File
csv.writer()
import csv

print("Program to demonstrate csv.writer() function")
print("\n")
p_details =[('course','fees','place'),('Python',22000,'Pune'),('Android',11000,'Assam'),('Java',30000,'Delhi')]
c = open('programs.csv','w')
print("File is opened for writing:")
o = csv.writer(c)
for p in p_details:
    o.writerow(p)
    c.close()
# DictReader = dictionary object is created for mapping the data to read it to the dictionary
import csv

print("Program to demonstrate DictReader() class")
print("\n")
with open('company.csv') as c:
    r = csv.DictReader(c)
for row in r:
    print(row['Name'], row['Age'])
#                                                        DictWriter
import csv

print("Program to demonstarteDictWriter() class")
print("\n")
with open('Game.csv', 'w') as file:
    columnnames = ['Game_name', 'No_of_players']
    writer = csv.DictWriter(file, fieldnames=columnnames)
writer.writeheader()
writer.writerow({'Game_name': 'Cricket', 'No_of_players': 12})
writer.writerow({'Game_name': 'Football', 'No_of_players': 11})
writer.writerow({'Game_name': 'Hockey', 'No_of_players': 11})
#                                                                 to set the directory
import csv

with open('Emp_Info.csv', 'r') as file:
    reader = csv.reader(file)
for each_row in reader:
    print(each_row)
#                                                   for semi-colon separated file
reader = csv.reader(file, delimiter  = '';'')
finally:
    file.close()
    reader = csv.reader(file,quotechar="'")
    reader = csv.reader(file,skipinitialspace=True)
    reader = csv.reader(file,quoting=csv.QUOTE_NONE)
#                                                                                        dialect
csv.register_dialect(
'mydialect',+delimiter = ';',
skipinitialspace = True,
quotechar = '"',
doublequote = True,)
reader = csv.reader(csv_file, dialect='mydialect')
#                                                                                         Writer
csv.writer(csvfile, dialect='excel', **fmtparams)
import csv

with open('start.csv', 'w') as csvfile:
    startwriter = csv.writer(csvfile, delimiter=' ',
quotechar='|', quoting=csv.QUOTE_MINIMAL)
startwriter.writerow(['Start'] * 2 + ['working example of csv write'])
startwriter.writerow(['starting', 'this is an example', 'just a simple working example'])
#                                     open an empty csv file, then write the data
import csv

row_list = [
["SN", "Name", "Quotes"],
[1, "Linus Torvalds", "Talk is cheap. Show me the code."],
[2, "Martin Fowler", "Any fool can write code that a computer can understand. Good programmers write code that humans can understand."],
[3, "Anonymous", "The most important property of a program is whether it accomplishes the intention of its user."] ]
with open('quotes.csv', 'w') as file:
    writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC, delimiter=';')
writer.writerows(row_list)
# 
import csv

newdict=[{'branch': 'ME', 'cgpa': '9.4', 'student_name': 'Sulaksh', 'year': '2'},
{'branch': 'COE', 'cgpa': '8.9', 'student_name': 'Amit', 'year': '2'},
{'branch': 'IF', 'cgpa': '8.3', 'student_name': 'Rutuja', 'year': '2'},
{'branch': 'IM', 'cgpa': '7.1', 'student_name': 'Madhu', 'year': '2'}]
fields = ['student_name', 'branch', 'year', 'cgpa']
filename = "uni_records.csv"
with open(filename, 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames = fields)
writer.writeheader()
writer.writerows(newdict)
#                                                                                             user-defined functions
import math

a = 2.3
print ("The floor of 2.3 is : "+ math.floor(a))
# 
def add(a, b):
    c = (a+b)
    return c
def add(a, b):
    return (a+b)
print (add(5, add(7, 6))) #                     add Multiple tags in Print
#                                                                                 Return Type
# print all the even numbers and double of all the odd numbers, starting from 1
n = int(input())
for i in range(1, n+1):
	if i%2 == 0:
		print (i)
	else:
		print (2*i)
#                     2nd Method
def check(k):
	if (k%2==0):
		print (k)
	else:
		print (2*k)
n = int(input())
for i in range(1, i+1):
	check(i)
#                               Default Arguments
def add(a=0, b=0):
    return (a+b)
#                               Aliasing function names
a = add()
n = int(input())

#                                                                              Constructors
myObject.myVariable = "some other value"

class Example:
	def anotherFunction(self, parameter1):
		self.myVariable = parameter1
		# or                             by calling for a user input
        self.myVariable = input()

myObject = Example()
myObject.anotherFunction("Amazing Spiderman")
print(myObject.myVariable)
#                                                                            Object Creation
class Example:
    def __new__(self):
        return 'kaashiv'
# creating object of the class Example
mutantObj = Example()
# but this will return that our object 
# is of                                       type str
print (type(mutantObj))
# The object created is of the type Example
class Example:
    myVariable = "some value"
    simpleObj = Example()
print (type(simpleObj))
#                                                                       Object Initialisation
class Example:
	def __init__(self, value1, value2):
	    self.myVariable1 = value1
	    self.myVariable2 = value2
		print ("All variable initialized")
myObj = Example("first variable", "second variable")
def __init__(self):
    self.myVariable1 = input()
    self.myVariable2 = input()
#                                                                                 Destructors
# destroy the object and perform the final clean up, garbage collector
# closing open files, closing database connections, cleaning up the buffer or cache
# The destructor method will only be called when the reference count becomes zero
class Example:
	def __init__(self):
		print ("Object created")
	#                                     destructor
	def __del__(self):
	    print ("Object destroyed")
#                                        creating an object
myObj = Example()
#                           to delete the object explicitly
del myObj
#                                                                                   Circular Referencing
# two objects refers to each other, both of these objects goes out of reference
class Foo():
    def __init__(self, id, bar):
        self.id = id
        # saving reference of Bar object
        self.friend = bar
        print ('Foo', self.id, 'born')
    def __del__(self):
        print ('Foo', self.id, 'died')
class Bar():
    def __init__(self, id):
        self.id = id
        # saving Foo class object in variable
        # 'friend' of Bar class, and sending
        # reference of Bar object for Foo object
        # initialisation
        self.friend = Foo(id, self)
        print ('Bar', self.id, 'born')
    def __del__(self):
        print ('Bar', self.id, 'died')
b = Bar(12)
#                                                     Exception in __init__ method
class Example():
	def __init__(self, x):
	    # for x = 0, raise exception
		if x == 0:
			raise Exception()
		self.x = x
	def __del__(self):
		print (self.x)
#                                                                                                              Deleting a file
import os

if os.path.exists("pythonfile2.txt"):
    os.remove("pythonfile2.txt")
else:
    print("File not found to delete !!!")
if os.path.exists("pavan kumar sake.txt"):
    os.remove("pavan kumar sake.txt")
else:
    print("pavan kumar sake.txt is not found in the directory !!!")
#                                                                                              File readline
file = open("sample.txt", "r")
print(file.readline(11))
print(file.readlines())
#                                                                                 Patterns
# Type 1.                                                                  $ Star Pattern
#                                    Program to print full pyramid
num_rows = int(input("Enter the number of rows"));
for i in range(0, num_rows):
    for j in range(0, num_rows-i-1):
        print(end=" ")
    for j in  range(0, i+1):
        print("*", end=" ")
    print()
#                                    Program to print Left Half Pyramid
num_rows = int(input("Enter the number of rows"));
k = 1
for i in range(0, num_rows):
    for j in range(0, k):
        print("* ", end="")
    k = k + 1
    print()
#                                     Program to print Right Half Pyramid
num_rows = int(input("Enter the number of rows"));
k = 8
for i in range(0, num_rows):
    for j in range(0, k):
        print(end=" ")
    k = k - 2
    for j in range(0, i+1):
        print("* ", end="")
    print()
# # Program to print One More Star Pattern Pyramid
print("Program to print star pattern: \n");
rows = input("Enter maximum stars you want display on a single line")
rows = int (rows)
for i in range (0, rows):
    for j in range(0, i + 1):
        print("* ", end='')
    print("\r")
    for i in range (rows, 0, -1):
        for j in range(0, i -1):
            print("* ", end='')
        print("\r")
#                                                     diamond star pattern
num_rows = int(input("Enter the number of rows"))
k = 0
for i in range(1, num_rows + 1):
    for j in range (1, (num_rows - i) + 1):
        print(end = " ")
    while k != (2 * i - 1):
        print("*", end = "")
        k = k + 1
        k = 0
print()
k = 2
m = 1
for i in range(1, num_rows):
    for j in range (1, k):
        print(end = " ")
        k = k + 1
        while m <= (2 * (num_rows - i) - 1):
            print("*", end = "")
            m = m + 1
            m = 1
        print()
#                                                                                                                   Factorial
n! = n*(n-1)*(n-2)*(n-3)*
# Python program to determine the value of factorial for a given number
# modifying the value keyed in will produce a different result
Number = int(input(" Enter the number for which factorial value to be determined : "))
factorial = 1
# to verify that the given number is greater than zero incase it is less than zero then the
# message stated below will be printed
if Number < 0:
    print(" ! ! ! ! ! Factorial value cannot be intended for negative integers ! ! ! ! ! ")
# The default factorial value for zero is one and this is printed here
elif Number == 0:
    print(" ! ! ! ! 1 is the factorial value 0 ! ! ! ! ")
else:
    # For loop to handle the factorial calculation
    for i in range(1,Number + 1):
        factorial = factorial*i
    print("The factorial value for the " , Number , "is" , factorial)
# Python Code for finding nth                                                                                Fibonacci Number
def Fibonacci_num(m):
    u = 0
    v = 1
    if m < 0:
        print("Incorrect input entered")
    elif m == 0:
        return u
    elif m == 1:
        return v
    else:
        for i in range(2,m):
            c = u + v
            u = v
            v = c
        return v
Fibonacci_num(9)
#                                             print series till the position mentioned
n_terms = int(input("how many terms ? "))
n1 = 0
n2 = 1
count = 0
if n_terms <= 0:
    print("Invalid, Enter a positive Integer :")
elif n_terms == 1:
    print("Fibanocci Sequence upto",n_terms,":")
    print(n1)
else:
    print("Fibanocci Series upto",n_terms,":")
    while count < n_terms:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1
#                                       Generators
def fibo(num):
    a,b = 0, 1
    for i in range(0, num):            # Generator
        yield "{}:: {}".format(i + 1,a)
        a, b = b, a + b
for item in fibo(10):
    print(item)
# Through                                 for loop
u, v = 0, 1
for i in range(0, 10):
    print(u)
    u, v = v, u + v
#  Through                                  Recursion
def fibonacci_ser(m):
    if(m <= 1):
        return m
    else:
        return(fibonacci_ser(m-1) + fibonacci_ser(m-2))
m = int(input("Enter number of terms:"))
print("Fibonacci sequence:")
for i in range(m):
    print(fibonacci_ser(i))
#                                                                                                      Trigonometric
# to convert the values in radians to degrees and degrees to radians = degrees(value), radians(value)
#                                                            sin(x) Function
import math

x = 1
print(math.sin(x))
print(math.cos(x))
print(math.tan(x))
print(math.asin(x))
print(math.acos(1))
print(math.atan(1))
# The hyperbolic sine of the angle of the value passed as an argument is returned
a = 1.0
b = 1.0
c = complex(a,b)
print("The value of hyperbolic sine is",math.sinh(c))
print("The value of hyperbolic sine is",math.cosh(c))
print("The value of hyperbolic sine is",math.tanh(c))
print("The value of inverse hyperbolic sine is",math.asinh(c))
print("The value of inverse hyperbolic sine is",math.acosh(c))
print("The value of inverse hyperbolic sine is",math.atanh(c))
#                                                                                                             ordinal(ord) Function
# integer representing the character passed to it. It means every character has some integer value, ASCII code
# works only for single character
x = 'a'
print(ord(x))
#                                                                                            Strip Function
# rstrip, lstrip
string_before_strip  = '00000000abcdefghijklmnopqrstuvwxyz00000000'
print( " String before striping : " , string_before_strip)
string_after_strip = string_before_strip.strip( '00000000' ) # ("00000000") is Removed
print( " String after striping  : " , string_after_strip)
#                                                                                                 Split Function
# While reading data from CSV
# split() is used to break the data into various chunks of data
# split () taking different delimiters
# 1 -->                                                 no delimiter specified
inp1 = 'A E I O U'
print("String will split at whitespace :",inp1.split())
print("list of vowels :")
for i in inp1.split():
    print(i)
# 2 -->                                                 delimiter is comma and a space (, )
inp2 = 'J&K, Puducherry, Delhi, Andamana and Nicobar, Chandigarh, Dadra and Nagar Haveli, Daman and Diu, Lakshadweep, Ladakh'
ut = inp2.split(', ')
print("Number of Union Territories :", len(ut))
print("UT is listed as below :")
for u in range(len(ut)):
    print((u+1),'-->', ut[u])
# 3 -->                                                  delimiter is |
inp3 = 'java|python|c++|scala|julia'
print("String will split at '|' :", inp3.split('|'))
print("Different programming languages are :")
for lang in inp3.split('|'):
    print(lang) 
# 4 -->                                                 splitting string at every 4 character
inp4 = 'fourfivenine'
print([inp4[i: i+4] for i in range(0, len(inp4), 4)])
#                                                                               max splits
# split() function with different values for max splits
print("Split() with default max split values i/e -1 :")
inp1 = 'Java@Python@C++@Scala@Julia'
print("Input string will split at @ :", inp1.split('@'))
print('\n')
print("number of splits (0):", inp1.split('@', 0))
print("number of splits (1):", inp1.split('@', 1))
print("number of splits (2):", inp1.split('@', 2))
print("number of splits (3):", inp1.split('@', 3))
print("number of splits (4):", inp1.split('@', 4))
print("number of splits (5):", inp1.split('@', 5))
print('\n')
print("Split using for loop")
for i in range(6):
    print("number of splits", i, inp1.split('@', i))
# calculating sum of marks of a student
# input string containing marks scored by a student in five different subjects
marks = '95, 92, 82, 92, 98'
sum = 0
#                                      input string will split at ', '
list_marks = marks.split(', ')
print("Marks scored by student :", list_marks)
print("Student marks:")
for marks in list_marks:
    print(marks)
print('\n')
#                                         calculating total marks
for i in range(len(list_marks)):
    sum += int(list_marks[i])
print("total marks scored by student :", sum)
#                                                                       Round Function
#                                              Integers:
a = 12
round (a)
print (a)
#                                              Floating Point
b = 21.7
c = 21.4
print(round(b))
print(round(c))
# 
#          when the (n+1)th digit is equal to 5
a = 5.465
print(round(a, 2))
#           when the (ndigit+1)th digit is >=5
b = 5.476
print(round(b, 2))
#                  when the (ndigit+1)th digit is <5
c = 5.473
print(round(c, 2))

Tup = (-40.95, 50.85, 10.98, 20.26, 30.05) #                                              Declaration of a Tuple
Lis = [-39.29, -42.15 , -39.97, -10.98, 32.65] #                     Declaration of a List
print('Round Function on Negative Decimal = %.2f' %round(-19.48476))
print('Round Function on Positive Decimal = %.2f' %round(15.98763))
print('Round Function with 2nd parameter on positive = %.3f' %round(11.98763, 3))
print('Round Function with 2nd parameter on negative = %.3f' %round(-18.48476, 3))
print('Round Function for Items in a List = %d' %round(Lis[2]))
print('Round Function for Items in a List = %d' %round(Lis[4]))
print('Round Function for Items in a Tuple = %d' %round(Tup[2]))
print('Round Function for Items in a Tuple = %d' %round(Tup[4]))
print('Round Function for Multiple Number = %.2f' %round(20 + 40 - 20.6578, 2))
#                                                                                 Truncate() 
# truncate the digits on the left side of the decimal point
# truncate(565.5556, -2)
def truncate():
    truncate = Tup(565.5556, -1);
    return
print (truncate)
#                                                                                                                Regex
# specify a set of rules that can fetch a particular group and validate a string against that rule
# contain e-mail addresses, phone numbers or any particular pattern to match
import re

word = "He is very smart"
x =re.search("^He.*smart$",word)
print(x)
"""
[] = It represents a set of characters.
. = It represents any character except a newline.
* = It represents zero or more occurrences.
+ = It represents one or more occurrences.
^ = It represents the starting character.
$ = It represents the ending character.
| = It represents either-or.
() = It represents capture and group.
\ = It is generally used to escape special characters

\w = It shows a match if the string has any set of word characters from [0-9], A-Z or a-z and underscore.
\W = It returns a match if the string has no word characters present.
\d = These returns match when there are digits in the string.
\D = It is the opposite of the previous one as it returns a match if no digits are present in the string.
\s = It is used to check for white space characters in a string. It returns a match if white space characters are present.
\S = It returns a match when there are no white spaces in the string."""
#                                                                               findall() function
import re

word = "Abith is 22 years old and his mobile number last three-digit is 703"
rgex ='\d+'
x =re.findall(rgex,word) # find numbers
print(x)
#                                                                               search() function
import re

word = "Abith is 22 years old"
rgex ='^Abith'
x =re.search(rgex,word)
print(x)
regex1= '^Raj'
x1 = re.search(regex1,word)
print(x1)
#                                                                              Split() function
import re

word = "Raju is 22 years old"
rgex ='\s'
x =re.split(rgex,word) # 
print(x)
#                                                                               sub() function
# replaces the matches with the string or character, replace the white space with ‘&’ in our string
import re

word = "Raju is 22 years old"
rgex ='\s'
x =re.sub(rgex,'&',word)
print(x)
#                                                                                                regex replace 
""" + = matching one or more occurrences of preceding expressions
? =  matching zero or one occurrence of preceding expressions
. =  to match any single character except a newline
* =  to match zero or more occurrences of preceding expressions
^ =  to match the starting of the line
$ = to match the end of the line"""
import re

print("The simple program for sub() method for replacing:")
str = "kaashiv#!!Training#!!Institute"
print("The given string that needs to be replaced with given pattern is as follows:")
print(str)
res_str = re.sub("#!!"," ",str)
print("The string obtained after replacing special character with space is as follows:")
print (res_str)
"""pattern: In this, we write the pattern to be searched in the given string.
replc: This parameter is for replacing the part of the string that is specified.
string: This provides a string that needs to be replaced with a given pattern
max: This is used to replace all the occurrences until the max number is provided"""
import re

print("The below program is used to demonstrate sub() method:")
phonenum = "2004-959-559 # This is Phone Number"
print("The given string is as follows:")
print(phonenum)
correct_num1 = re.sub(r'#.*$', "", phonenum)
print("The correct phone number by removing special characters in the given string which means replacing them by space is as follows:")
print(correct_num1)
correct_num2 = re.sub(r'\D', "", phonenum)
print("Now we have replaced all the spaces and have only digits in the given string is as follows:")
print(correct_num2)
#                                                                                                           Regex Tester
#                                                                                              Pythex
(Ed[a-z]cba) | (Tra[a-z]ning) = input()
# we input the logic pattern in regular expression using special characters or metacharacters
#                                                                                                       Debuggex
# tool to test for regular expression with a given logic pattern to test or match with the given string
#                                                                                                           FREEFORMATTER
# it displays the match found in the given string, freeformatter.com
#                                                                                                            String Join
# concatenate iterable objects (list, dict, tuple, string, set)
list = ['Sugar', 'Salt', 'Pepper', 'Pots', 'loves', 'the', 'Iron-Man'] # This seperator is used to seperate each object of the iterable element when concatenated by the join() function
seperator = "-"
# Using join() function to concatenate the elements of list and store the returned string in the variable "Str"
Str = seperator.join(list)
#                          Prints the string "Str" using the Python Print function
print(Str)
#                                 Using a blank string as a seperator in join function
list = ['S', 'u', 'g', 'a', 'r']
Str = "".join(list)
print(Str)
#                                                                                                    Reverse Number
# 1                            Using Slicing Method
def reverse_slicing(s):
    return s[::-1]
my_number = '123456'
if __name__ == "__main__":
    print('Reversing the given number using slicing =', reverse_slicing(my_number))
# 2                                                      Using For loop Method
def reverse_for_loop(s):
    s1 = ''
    for c in s:
        s1 = c + s1
        return s1
my_number = '123456'
if __name__ == "__main__":
    print('Reversing the given number using for loop =', reverse_for_loop(my_number))
# 3.                                                        While Loop Method
# 
def reverse_while_loop(s):
    s1 = ''
    length = len(s) - 1
    while length >= 0:
        s1 = s1 + s[length]
        length = length - 1
        return s1
my_number = '123456'
if __name__ == "__main__":
    print('Reversing the given number using while loop =', reverse_while_loop(my_number))
# 4.                                                       Using Reversed Method
def reverse(string):
    string = "".join(reversed(string))
    return string
my_number = "123456"
print ("The given number is : ",end="")
print (my_number)
print ("Reversing the given number using reversed is : ",end="")
print (reverse(my_number))
# 5.                                                      Using user-entered number and then reversing it
My_Number = int(input("Please provide the number to be reversed: "))
Reverse_Number = 0
while(My_Number > 0):
    Reminder = My_Number %10
    Reverse_Number = (Reverse_Number *10) + Reminder
My_Number = My_Number //10
print("Reverse of the provided number is = %d" %Reverse_Number)
# 6.                                                      Two-Digit Reverse Method
My_Number = int(input("Please provide the number to be reversed: "))
Reverse_Number = 0
temp = Reverse_Number
Reminder = 1
for i in range (Reminder+1):
    Reminder = My_Number %10
    Reverse_Number = (Reverse_Number *10) + Reminder
    My_Number = My_Number //10
    print("Reverse of the provided number is = %d" %Reverse_Number)
# 7.                                                      Three-Digit Reverse Method
My_Number = int(input("Please provide the number to be reversed: "))
Reverse_Number = 0
temp = Reverse_Number
Reminder = 1
for i in range (Reminder+2):
    Reminder = My_Number %10
    Reverse_Number = (Reverse_Number *10) + Reminder
    My_Number = My_Number //10
    print("Reverse of the provided number is = %d" %Reverse_Number)
# 8.                                                      Without the Recursion Method
my_num=str(input("Enter the number to be reversed: "))
print("Reverse of the given number is: ")
print(my_num[::-1])
# 9.                                                      With Recursion Method
def reverse(s):
    if len(s) == 0:
        return s
    else:
        return reverse(s[1:]) + s[0]
my_number = "123456789"
print ("The given number is : ",end="")
print (my_number)
print ("Reversing the given number using recursion is : ",end="")
print (reverse(my_number))
# 10.                                                  Using Function Method
def rev_number(My_Number):
    reverse_num = 0
    while(My_Number):
        Reminder = My_Number % 10
        reverse_num = reverse_num * 10 + Reminder
        My_Number //= 10
    return reverse_num
if __name__ == "__main__" :
    My_Number = int(input('Please provide the number to be reversed:: '))
    print('Reverse of the provided number is: ', rev_number(My_Number))
# 11                                                                     Using List Method
number = "123456789"
print ("The given number is : " + number)
#                                           converting number into list
list1 = list(number)
#                                            applying reverse method of list
list1.reverse()
#                                          converting list into number
number = ''.join(list1)
print ("Reverse of the provided number is : " + number)
# 12.                                                                  Using the Stack Method
def create_stack():
    #                              creating a list as stack and return it
    stack = []
    return stack
def push(stack,element):
    #                         adding new element to list
    stack.append(element)
def pop(stack):
    #                      deleting the last element from the list
    if len(stack) == 0:
        return
    return stack.pop()
num = 619
stack = []
def reverse(number):
    #                       reversing the number by using stack's functions
    num = len(number)
    #                               creating empty list (stack)
    stack = create_stack()
    #                             inserting number into list
for i in range(0,num):
    push(stack,number[i])
    number = ""
# getting last element of the stack list
for i in range(0,num):
    number = number + pop(stack)
    return number
number1 = "123456789"
number2 = reverse(number1)
print ("The given number is : " + number1)
print ("Reverse of the given number is : " + number2)
#                                                                                                         Slice String
string = "PYTHON TUTORIAL"
print("Input string :",string)
#                                   Positive indexing
print("First six characters :")
print(string[slice(6)])
print("8th char to end of string :")
print(string[slice(7, len(string))])
#                                      Extracting alternate odd chars using step parameter
print("First char to end of string skipping one character")
print(string[slice(0,len(string),2)])
#                                       Extracting alternate even chars using step parameter
print("Second char to end of string skipping one character")
print(string[slice(1, len(string), 2)])
#                                          Negative indexing
print(string[slice(-4,-1)])
print(string[slice(-8)])
#                           Stop parameter should be greater than start parameter
print("Nothing will be printed :",string[slice(-4,0)])
print("Nothing will be printed :",string[slice(-1,-1)])
print("Nothing will be printed :",string[slice(-2,-4)])

string[slice(7, len(string))] 
string[slice(0,len(string),2)]
string[slice(1,len(string),2)]
string[slice(-4,-1)]
# Python                 slicing          using indexing
string = "PYTHON TUTORIAL"
print("Input string :",string)
print("default start/stop/step parameters")
print(string[::])
#                        Positive indexing
print("First six characters :")
print(string[:6])
print("8th char to end of string :")
print(string[7:])
#                                         Extracting alternate odd chars using step parameter
print("First char to end of string skipping one character")
print(string[::2])
#                                         Extracting alternate even chars using step parameter
print("Second char to end of string skipping one character")
print(string[1::2])
#                      Negative indexing
print("last 8 characters")
print(string[-8:])
print("string reversal")
print(string[::-1])
#                                        Stop parameter should be greater than start parameter
print("Nothing will be printed :",string[3:1])
print("Nothing will be printed :",string[-1:-8:1])
#                                                                                             String Replace
str = "Let's go to a place, from where we can go to another. But where exactly do we want to go"
# Prints the string by replacing go by GO
print(str.replace("go", "#GO"))
# Prints the string by replacing only 2 occurrence of go
print(str.replace("go", "#GO", 2))
# Removing junk charachters from DF using string replace function
DF = [['Last name, first name 1'],['Last name, first name 2'],['Last name, first name 3'],['Last name, first name 4'],['Last name, first name 5'],['Last name, first name 6']]
for i in DF:
    for j in i:
        print (j.replace(',' , ''))
junkch = [['/'],['$'],['&']]
str = 'abcdef $ gh@#'
str.replace(junkch,'')
#                                                                                                              eval()
# run the python programming code (which is actually passed as the argument)
# evaluates the “String” like the Python Code expression & returns as an integer
# parsing the string value, and that string value also be evaluated as the python expression
x = 10
print ('value of x ==>')
print(eval('x'))
print ('value of x+10 ==>')
print(eval('x+10'))
print ('value of x^2 ==>')
print(eval('x*x'))
print('value of x^3==>')
print(eval('x*x*x'))
# IF and ELSE conditions are prepared to make the prime number logic program by using the value of x
if(x%2==0):
    print('X is even number')
if(x%2!=0):
    if(x%3!=0):
        if(x%5!=0):
            if(x%7!=0):
                print(eval('x'))
                print('is a prime number')
            else:
                print ('x is not prime number')
        else:
            print('x is not prime number')
    else:
        print('x is not prime number')
else:
    print('x is not prime number')
#                                          Using For Loop
from math import *

for lm in range(1, 3):
    func1 = input("Enter the Math Function which are mentioned below to Evaluate.\nFunctions Allowed are: 1. square_root(x) and 2. power(x,y):\n")
    try:
        print(eval(func1, {'square_root': sqrt, 'power': pow}))
    except Exception as ex1:
        print(ex1)
    break
print('Now it is Done')
#                                                                                                              Counter
# count of how mant times repeated
# dictionary subclass used for counting the objects that are hashable, includes zero and negatives values
from collections import Counter

c = Counter()
print(c)
c = Counter('sample string')
print(c)
c = Counter(['word', 'word1','word1']) # Word Count
print(c)
c = Counter(a=4, b=2, c=0, d=-2)
sorted(c.elements())
#                                       Character count
from collections import Counter

lst = ['a', 'b', 'c', 'b', 'a', 'b']
c = Counter(lst)
print(c)

from collections import Counter

counter = Counter(a=3, b=2, c=4)
print(counter)
print(list(counter.elements()))     # o/p = 
"""Counter({'c': 4, 'a': 3, 'b': 2})
['a', 'a', 'a', 'b', 'b', 'c', 'c', 'c', 'c']"""
c = Counter('sssssshhhhhcccdddd')
c.most_common(3)
a.subtract(b)
a
a-b
#                                                                                                     string _contains_()
print("Python program to demonstrate _contains_() function")
print("\n")
str1 = "Kaashiv Training"
sub_str = "Kaashiv"
if (str1.__contains__(sub_str)):
    print("The given String contains the given substring")
    print(sub_str)
    print("\n")
else:
    print("The given String does not contain substring")
#                                                          The given substring is present in the string or Not
print(str.__contains__("Kaashiv Training Institute", "Abith Raj"))

import operator

print("Python program to demonstrate contains() function of operator module ")
print("\n")
str1 = "Kaashiv is best in programming courses."
if operator.contains(str1, "best"):
    print ("The given substring is present in the string.")
else :
    print ("The given substring is not present in the string.")
# created a series using pandas object pd,
import pandas as pd

print("Program to demonstrate contains() function provided by pandas")
print("\n")
sr = pd.Series(['Kaashiv', 'Training', 'Institue', 'Chennai', 'India'])
print("The given series along with its index and type is as follows:")
print(sr)
print("\n")
r = sr.str.contains('Kaashiv')
print(r)
#                                 Python Program for                                         printing pyramid pattern using stars
# two for loops; the outer for loop can be used to take care of a number of rows, while the inner for loop can be used to take care of the number of columns 
# Program to print pyramid patterns of stars
for i in range(0, 5):
    for j in range(0, i+1):
        print("* ",end="")
    print()
a = 8
for i in range(0, 5):
    for j in range(0, a):
        print(end=" ")
    a = a - 2
    for j in range(0, i+1):
        print("* ", end="")
    print()
#                              print a triangle using stars
# Ask the Range of the triangle
num = int(input("Enter the range: \t ")) # input = 5
# i loop for range(height) of the triangle
# first j loop for printing space ' '
# second j loop for printing stars '*'
for i in range(num):
    for j in range((num - i) - 1):
        print(end=" ")
    for j in range(i + 1):
        print("*", end=" ")
    print()
#                                     single star in the first line, then 3 stars in the second line,
# increasing the “l” count by 2 at the end of second for loop
k = 16
l = 1
for i in range(0, 5):
    for j in range(0, k):
        print(end=" ")
    k = k - 4
    for j in range(0, l):
        print("* ", end="")
    l = l + 2
    print()
#                                Numeric pattern
k = 1
for i in range(0, 5):
    for j in range(0, i+1):
        print(k, end=" ")
    k = k + 1
    print()
# to print number 1 in the first row, number 1 and 2 in the second row, number 1, 2 and 3 in the third row & continue
for i in range(0, 5):
    num = 1
    for j in range(0, i+1):
        print(num, end=" ")
        num = num + 1
    print()
# end the row with the squares the row number, two for loops
# incrementing the numb variable’s value by 1 in the inner for loop and incrementing the value of variable inc by 2 for the outer for loop
numb = 1
inc = 1
for i in range(0, 5):
    for j in range(0, inc):
        print(numb, end=" ")
        numb = numb + 1
    print()
    inc = inc + 2
#                             running the outer loop in range 10
for num in range(10):
    for i in range(num):
        print (num, end=" ") #              printing the number
#            We will use new line in order to display the pattern correctly
    print("\n")
# print it column-wise, 
last_num = 6
for row in range(1, last_num):
    for column in range(row, 0, -1):
        print(column, end=' ')
    print("")
#                                         taking the squares of the numbers
last_num = 9
for i in range(1, last_num):
    for j in range(-1+i, -1, -1):
        print(format(2**j, "4d"), end=' ')
    print("")
# (eg-2)
for i in range(1, last_num):
    for i in range(0, i, 1):
        print(format(2**i, "4d"), end=' ')
    for i in range(-1+i, -1, -1):
        print(format(2**i, "4d"), end=' ')
    print("")
#                                                                            right angle triangle pattern
stop = 2
start = 1
current_num = stop
for row in range(2, 6):
    for col in range(start, stop):
        current_num -= 1
        print (current_num, end=' ')
    print("")
    start = stop
    # stop It is similar to the previous programrow
    current_num = stop
# Type 3.                                                                              Character pattern
# converting the numeric value 65 into the capital letter A and hence iterating over the loop to increment the “value” variable
value = 65
for i in range(0, 5):
    for j in range(0, i+1):
        ch = chr(value)
        print(ch, end=" ")
        value = value + 1 # remove 4 indents to repeat characters
    print()
#                                  incrementing it by 2 in the outer for loop
value = 65
inc = 1
for i in range(0, 5):
    for j in range(0, inc):
        ch = chr(value)
        print(ch, end=" ")
        value = value + 1
    inc = inc + 2
    print()
#                                  rotated the pattern by 180 degrees
decrement = 8
counter = 64
value = 65
for i in range(0, 5):
    for k in range(0, decrement):
        print(end=" ")
    for j in range(0, i+1):
        counter = counter + 1
        value = counter
        temp = value
    for j in range(0, i+1):
        ch = chr(value)
        print(ch, end=" ")
    value = value - 1
    value = temp
    decrement = decrement - 2
    print()
#  to print the square pattern using any value 
square_side = int(input("Please enter the square dimension  : "))
print("Square Pattern")
for i in range(square_side):
    for i in range(square_side):
        print("$", end = '  ')
    print()
#                                                                                                                                 Functions
# (pi for return value 3.141592, E for return value 0.718282 , nan for representing non numbers, inf for representing infinite), 
# logarithmic functions (exp(x) returns e**x), expm1(x) returns e**x-1, log2(x) returns logarithmic value for x with base2, 
# sqrt(x) returns square root value for x), numeric functions ( factorial(x), isinf(x), 
# remainder(x, y) returns value of remainder for dividing x by y) and trigonometric functions (sin(x), cos(x), tanx(x))
#                                                                                 Constants
"""
Constants	Description
pi	         Returns 3.141592
E	         Returns 0.718282
nan	         Not a number
inf	         Infinite"""
import math

print( "CONSTANTS IN PYTHON")
print(" PI value : " , math.pi)
print(" E value : " , math.e)
print(" nan value : " , math.nan)
print(" E value : " , math.inf)
#                                                                               Logarithmic Functions
"""
Function	Description
exp(x)	Returns e**x
expm1(x)	Returns e**x - 1
log(x[, base])	x to the base logarithm is returned
log1p(x)	Base1 logarithm of x value is returned
log2(x)	Base2 logarithm of x value is returned
log10(x)	Base10 logarithm of x value is returned
pow(x, y)	Returns x raised to the power y
sqrt(x)	Square root value for x is returned"""
import math

#              variable declaration and assignation
Number_1 = 1
Number_2 = 2
Number_3 = 3
Number_4 = 4
#             Applying exp() function
print("            EXPONENT VALUE                     ")
print(" Exponent value: " , math.exp(Number_1))
print(" \n ")
#            Applying Base1 logarithm function
print("            BASE1 LOGARITHM  " )
print(" BASE1 LOGARITHM VALUE of 2 : ", math.log1p(Number_2))
print(" \n " )
#             Applying Base2 logarithm function
print("           BASE2 LOGARITHM  " )
print(" BASE2 LOGARITHM VALUE of 2 : ", math.log2(Number_2))
print(" \n " )
#              Applying                                         Base10 logarithm function
print("           BASE10 LOGARITHM  " )
print(" BASE10 LOGARITHM VALUE of 2 : ", math.log10(Number_2))
print(" \n " )
#                                                               Applying x to power of Y
print("           X^Y" )
print(" X^Y Value : ", math.pow(Number_3,Number_4))
print(" \n " )
#                                                           Applying square root determination
print("     SQUARE ROOT " )
print(" SQUARE ROOT of 4 : ", math.sqrt(Number_4))
print(" \n " )
#                                                           Numeric Functions
"""Constants	Description
ceil(x)	The smallest integer which is very much greater than or equal to the x value is returned
copysign(x, y)	Using the sign of y, the value for x is returned
fabs(x)	absolute value for the x is returned
factorial(x)	factorial value of x is returned
floor(x)	the largest integer, which is very much less than or equal to the x value, is returned
fmod(x, y)	the remainder of dividing x by y value is returned
frexp(x)	Returns the mantissa and exponent of x as the pair (m, e)
fsum(iterable)	Returns an accurate floating-point sum of values in the iterable
isfinite(x)	if x is not an infinity or a Nan, then boolean value true is returned
isinf(x)	if x holds a positive or negative infinity, then true is returned
isnan(x)	Returns True if x is a NaN
gcd(x, y)	for x and y value, the most greates common divisor value is returned
the remainder(x, y)	Find the remainder after dividing x by y."""
import math

#                    variable declaration and assignation
Number_1 = 10.5
Number_2 = 20
Number_3 = -30
Number_4 = -40.24566
Number_5 = 50
Number_6 = 60.94556
Number_7 = 70
Number_8 = 80
#                   Applying Ceil() function
print( " CEIL : Smallest integer which is very much greater than or equal to the x value is returned  ")
print( " CEIL value : " , math.ceil(Number_1))
print( " \n " )
#                  Applying Copysign() function
print( " COPYSIGN : Smallest integer which is very much greater than or equal to the x value is returned  ")
Temp_var1 = math.copysign(Number_2,Number_3)
print(" VALUE AFTER COPY SIGN : ", Temp_var1)
print(" \n ")
#                Applying fabs() function
print( " FABS : absolute value for the x is returned  ")
print(" ABSOLUTE VALUE FOR 40.24566 : ", math.fabs(Number_4))
print(" \n ")
#               Applying Factorial() function
print(" FACTORIAL : factorial value of  x is returned  ")
print(" Factorial value for 50 : ", math.factorial(Number_5))
print(" \n ")
#              Applying Floor() function
print(" FLOOR : largest integer which is very much less than or equal to the x value is returned " )
print(" Floor : ", math.floor(Number_6))
print(" \n ")
#             Applying Fmod() function
print(" FMOD : remainder of divinding x by y value is returned ")
print(" Remainder : ", math.fmod(Number_6,Number_5))
print(" \n ")
#               Applying Frexp() function
print( " FREXP : Returns the mantissa and exponent of x as the pair (m, e) " )
print(" MANTISSA EXPONENT : ", math.frexp(Number_7))
print( " \n " )
#              Applying isfinite() function
print(" isfinite : if x is not an infinity or a Nan then boolean value true is returned ")
print(" Infinite or Nan (produces boolean output): ", math.isfinite(Number_8))
print(" \n ")
#                                                                                               Trigonometric Functions
"""
function	Description
sin(x)	sine value of x in radians is determined
cos(x)	cosine value of x in radians need to be determined
tan(x)	tangent value of x in radians need to be determined
degrees(x)	radian to degree conversion
radian(x)	the degree to radian conversion"""
import math

print(" \n ")
print("   TRIGNOMETRIC FUNCTION USAGE                        " )
print(" \n ")
print(' The value of Sin(90 degree) : ' + str(math.sin(math.radians(90))))
print(' The value of cos(90 degree) : ' + str(math.cos(math.radians(90))))
print(' The value of tan(pi) : ' + str(math.tan(math.pi)))
print(" \n ")
#                                                                                               String Functions
# center(), count(),  find(), format(), index(), isalnum(), lower(), maketrans(), replace()
#                                                                                           capitalize(uppercase)
# First Letter Only "A"
str1 = "hello from Abith"
str2 = str1.capitalize()
print(str2)
#                                                                      casefold(lowercase)
str2 = str1.casefold()
print(str2)
#                                                                      center()
# aligns the string at the center
str1 = "Abith"
str2 = str1.center(10)
print(str2)
#                                                                      count()
# number of times a substring occurs
str1 = "Hello from kaashiv. Welcomw to kaashiv "
num = str1.count("kaashiv")
print(str2)
#                                                                     encode()
str1 = "Abith"
str2 = str1.encode()
print("Hello from", str2)
#                                                                    endswith()
# Return True or False
str1 = "Hello from kaashiv"
str2 = str1.endswith("CBA")
print(str2) 
#                                                                    expandtabs()
str1 = "Hello\tfrom\t kaashiv"
str2 = str1.expandtabs(2)
print(str2)
#                                                                    find()
#                                                                    format()
str1 = "kaashiv"
print("Hello from {}.".format(str1)) # {} = placeholders
#                                                                    index()
str1 = "Hello from kaashiv"
str2 = str1.index("kaashiv")
print(str2)
# is = True or False
#                                                                    isalnum()
#                                                                    isalpha()
#                                                                    isdecimal()
#                                                                    isidentifier() = Spaces = False
#                                                                    islower()
#                                                                    isnumeric()
#                                                                    isprintable()
#                                                                    isspace()
#                                                                    istitle()
#                                                                    isupper()
#                                                                    join()
# to concatenate two strings in an iterated manner
#                                                                    lower()
#                                                                    upper()
#                                                                    replace()

# pandas = dataframe
# built-in = print(), enumerate(), range(), user-fun = def, Lambda
# sum_values_lambda = lambda                                                      $ Lambda
# def = to declare functions
# func-var = lambda x: x + 1
# print func-var(1)
# 2
# def passing_example(a_list, an_int=2, a_string="A default string"):
# a_list.append("A new item")
# an_int = 4
# return a_list, an_int, a_string
# my_list = [1, 2, 3] my_int = 10
# print passing_example(my_list, my_int)
# ([1, 2, 3, 'A new item'], 4, "A default string")
# my_list
# [1, 2, 3, 'A new item'] my_int
# 10
def fun():
    print("Abith")
fun()
def Abithfunction():                      # function call without argument
    print("Function Executed")
Abithfunction()

def Abithfunction(name):                # function call with argument
    print("my name is "+name)
Abithfunction("Abith")

def Abithfunction(name,age):            # function call with multiple arguments
    print("my name is "+name,"and age is "+age)
Abithfunction("Abith","25")

def Abithfunction(*name):                             # function call with array of arguments
    print("The student name is " + name[1])
Abithfunction("Venkat","Abith","Krishiv")

def Abithfunction(*name):
    print("The Guy : " + name[0])
def fun(*field):                                      # # function call with array of parameters
    print("is good in : "+field[2])
fun("Abith","25","Specialist in ML")

def square(value):
    return value*5                                     # function returning parameter
print(square(8))

def f():                  # Global scope
    s = "Abith"
    print("s")
f()
# data can be customized to passing into a function
from functools import partial  # partial parameters are added dynamically


def fun(f,a, b, c):
    return f*1000 + a *100 + b*10 + c
g = partial(fun,a=6,b=1,c=9)
print(g(0))
#                            Listing -packing 
def fun1(a,b,i):                                         # packing
    my_list = [6,1,9]                             # source-code
fun1(*my_list)                                           # un-packing
#                                                                                        unpacking dictionary
def fun(a, b, i):
    print(a, b, i)
d = {'a':6, 'b':1, "i":9}
fun(*d)                                          # to get the variables 
fun(**d)                                         # to get the value of variables
#                                                                                                                                  $ Range()
# # Generates List of Numbers in syntax with endValue = -1
# # range(start, end, step) => startValues, endValues, step = increment Value
# # range(3, 10) => [3, 4, 5, 6, 7, 8, 9]
# # range(4, 10, 2) => [4, 6, 8]
# # range(end) => range(5) => [0, 1, 2, 3, 4]
#                                                                                                                                $ Random()
#                                                                  $ Random number generator
# choice()
import random

sequence=[1,4,6,10]
random.choice(sequence)
random.random()
# 0.34486332358477956, 0.6366111987379882
#                                                                                          randrange (begin,end,step)
random.randrange(10,20,2)
#                                                                                                            shuffle()
# random.shuffle(x,random)
import random

num_list =  [7,8,10,12]
print(“List before using shuffle: “,num_list)
random.shuffle(num_list)
print(“List after using shuffle method: “, num_list)
#                                                      Uniform(a,b)
random.uniform(3,5)
#                                                                                                $     generate integers
import random
from random import randint, seed

seed(619)
within 0 to 5
for _ in range(5):
value = randint(0,5)
print(value)
#                                                                                                      $ generate float
seed(619)
for _ in range(5):
value = random()
print(value)
#                                                                                                  $   StopIteration
# object that holds a value (generally a countable number) which is iterated upon, iterator’ and ‘iterable’
# __next__(),                     Syntax for (StopIteration in if and else of next())
class classname:
    def __iter__(self):
        #set of statements
        return self;
def __next__(self):
    if # condition till the loop needs to be executed
    # set of statements that needs to be performed till the traversing needs to be done
    return
else:
    raise StopIteration               #  it will get raised when all the values of iterator are traversed
# Stop the printing of numbers after 20 or printing numbers incrementing by 2 till 20 in case of Iterators
class printNum:
    def __iter__(self):
        self.z = 2
        return self
def __next__(self):
    if self.z<= 20:   #performing the action like printing the value on console till the value reaches 20
        y = self.z
        self.z += 2
        return y
    else:
        raise StopIteration   #raising the StopIteration exception once the value gets increased from 20
obj = printNum()
value_passed = iter(obj)
for u in value_passed:
    print(u)
# Finding the cubes of number and stop executing once the value becomes equal to the value passed using StopIteration
def values():
    #list of integer values with no limits
    x = 1             #initializing the value of integer to 1
while True:
    yield x
    x+=  1
def findingcubes():
    for x in values():
        yield x * x *x     #finding the cubes of value ‘x’
def func(y, sequence):
    sequence = iter(sequence)
    output = [ ] #          creating an output blank array
try:
    for x in range(y):   #using the range function of python to use for loop
        output.append(next(sequence))   #appending the output in the array
except StopIteration:    #catching the exception
    pass
return output
print(func(5, findingcubes()))  #passing the value in the method ‘func’
#                                                                             to swap two values                   
#               taking values from the user
x = input()
y = input()
print('The value of x is {}'.format(x))
print('The value of y is {}'.format(y))
#               swapping the values
temp_var = x                        #       the value of x has been temporarily stored in the variable named temp_var
x = y
y = temp_var
print('The value of x after swapping is {}'.format(x))
print('The value of y after swapping is {}'.format(y))
# o/p => 619 <=> 196
#                                                                                                                    len()
len(str)
str2 = "Abith"
print("Length of str2 is:")
print(len(str2))
#                                                                                               in DataFrame
#                                                         reading csv file from url
DF = pd.read_csv("C:/Users/name/Desktop/Projects/abc.csv")
#                dropping null value columns to avoid errors as nulls can not be passed on to len() function
DF = DF.dropna()
#                                        converting to string dtype
DF["Salary"]= DF["Salary"].astype(str)
#                                             passing values
DF["Salary Length"]= DF["Salary"].str.len()
#                                           converting back to float dtype
DF["Salary"]= DF["Salary"].astype(float)
#  display
DF
# Python Program                                                               to find the length of a tuple
Tupl = ('Jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec')
print("The value returned by len() function for this tuple is \n", len(Tupl))
#                                                 get the number of elements present in the python dictionary
Dic = {'kaashiv': 18,'kaashiv':12,'kaashiv':22,'kaashiv':25}
print("The value returned by len() function for this dictionary is \n", len(Dic))
#                                                                               len() function in arrays 
arr = ['Kaashiv'] print("The value returned by len() function for this array is ", len(arr))
"""
#                                                                                                                                 $  Templates

from string import Template
student=(["Abith",100],["Arun",96])
t=Template("Hi,\n\n The student '$name' got a marks of '$marks' in the last semester.\n\nBy principal")
for i in student:
    print(t.substitute(name=i[0],marks=i[1]))
"""
#                                                                                                                                Regular Expressions
# to find list or sequence or patterns in a string 
#  import re
pattern=re.compile('[a-e]')
print(pattern.findall("this is abith"))

pattern=re.compile('\d')                                   # to find the numbers in string (&) mobile number validation
print(pattern.findall("this is abith"))
# ("\d") => separate numbers, ("\d+") => combined numbers like contact numbers
# ("\D"), ("\D+") = discards the numbers and prints rest of the items
# ("\s") = list the number of spaces 1 by 1 , ("\s+") = multiple spaces
# ("\S"), ("\S+") = list or matches the non-spaces
# ("\W"), ("\W+") = find the special characters
# ("\ab*") = matches with letters starting with a, b, abbb, ("\ab+") = ab, abb, ("\b b*") = b, b b                             $ compiler designing
 
# """
#                                                                                                                                Operator
import operator

# print(any([False,False,False,False])) o/p => False
# print(any([False,True,False,False])) o/p => True
# print(5.0/2) o/p => 2.5
# print(-5.0/2) o/p => -2.5
#                                                        $ addition
a = 4
b = 3
print("the addition of numbers is : ");
print(operator.add(a,b))
# O/P = the addition of numbers is :
# 7
#                                                 $ difference or sub
print("the difference of numbers is : ");
print(operator.sub(a,b))
#                                                 $ Product or Multi-ply
print("the product of numbers is : ");
print(operator.mul(a,b))
#                                                 $ true division (with decimals (eg)= 1.65416465465476)
print("the true division of numbers is : ");
print(operator.truediv(a,b))
#                                                 $ floor division
print("the floor division of numbers is : ");
print(operator.floordiv(a,b))
#                                                 $ exponentiation
print("the exponentiation of numbers is : ");
print(operator.pow(a,b))
#                                                 $ Modulus of numbers
print("the Modulus of numbers is : ");
print(operator.mod(a,b))

#                                                   Comparison Operator
"""
==	a == b	Returns True if the values on the either side of the operator is equal otherwise False.
!=	a != b	Returns True if the values on either sides of the operator is not equal to each other otherwise False.
>	a > b	Returns True if the value of the operand on the left of the operator is greater than the value on the right side of the operator.
<	a < b	Returns True if the value of the operand on the left of the operator is less than the value on the right side of the operator.
>=	a >= b	Returns True if the value of the operand on the left of the operator is greater than or equal to the value on the right side of the operator.
<=	a <= b	Returns True if the value of the operand on the left of the operator is less than or equal to the value on the right side of the operator."""

#                                                       Membership Operators
#     in	x in y	True if the value/operand in the left of the operator is present in the sequence in the right of the operator.
# not in	x not in y	True if the value/operand in the left of the operator is not present in the sequence in the right of the operator.

#                                                        Identity Operators
# is    	x is True	True if both the operands refer to the same object.
# is not	x is not True	Evaluates to false if the variables on either side of the operator point to the same object and true otherwise.
#                                                          Logical Operators
"""
and	x and y	True if both sides of the operator is True
or	x or y	True if either of the operand is True
not	not x	Complements the operand"""
#                                                           Relational
"""Less than → used with <
Greater than → used with >
Equal to → used with ==
Not equal to → used with !=
Less than or equal to → used with <=
Greater than or equal to → used with >="""
x = int(input())
(x > 0)
(x < 100)
#                                                                                                                             basic operations
year=2008                                # if-else
if year%4==0:
 print("year is leap")
else:
 print("year is not leap")
#                                        $ if-else->if-else
a=5
if a>=20:
 print("condition is true")
else:
 if a>=8:
  print("checking second value")
 else:
  print("all conditions are false")
#                          $ if-else->if-else        (eg)      $ in range func()
num=2
for a in range(1,4):
    print(num*a)
# o/p = 2, 4, 6
for i in range(1,6):               #                        $ to display stars in range using for loop
    for j in range(5,i-1,-1):
        print("*",end="")
        print("*")
        print()
#                                                                                                                         $ List
myList1 = ['first', 'second', 'third', 'fourth', 'fifth']
myList2 = myList1 # complete copying
myList2 = myList1[0:3] # Slicing
#                                                                                   Adding Serial Numbers in a List
#                  For storing 0 to (n-1) numbers in a list use range(n) function
myList1 = range(9)
#                                     to create a list with squares of all whole numbers
myQuickList = [x**2 for x in range(5)]
#                                       Appending to a List (Adding to a Existing List)
emptyList = []
emptyList.append('Python Online Internship')
emptyList.append('F.R.I.E.N.D.S')
emptyList.append('Online Internship')
emptyList.append('Kaashiv')
print (emptyList)

#                                                                                                   Naive method
print("Program to demonstrate length of list using naive method:")
print("\n")
lst = [ 1, 5, 7, 5, 2 ]
print ("The given list is as follows:")
print(lst)
print("\n")
counter = 0
for i in lst:
    counter = counter + 1
    print ("The Length of given list using naive method is as follows:")
print(counter)
#                                                     Implement Python                               List Length
from operator import length_hint

length_hint(iterable)
length_lst = length_hint(lst)
print(length_lst)

import time

start_time_naive = time.time()
counter = 0
for i in lst:
    counter = counter + 1
    end_time_naive = str(time.time() - start_time_naive)
    start_time_len = time.time()
    list_len = len(lst)
    end_time_len = str(time.time() - start_time_len)
    start_time_hint = time.time()
    list_len_hint = length_hint(lst)
    end_time_hint = str(time.time() - start_time_hint)
    print ("Time taken by using naive method is : " + end_time_naive)
    print ("Time taken by using len() method is : " + end_time_len)
print ("Time taken by using length_hint() method is : " + end_time_hint)
#                                                                                       Accessing using Indexing of elements
fruitsList = ["Orange", "Mango", "Banana", "Cherry", "Blackberry", "Avocado", "Apple"]
len(fruitsList)
#                                                                                                                         $ Listing with operator
lis = [1, 2, 3]
lis1 = [4, 5, 6]
lis2 = lis + lis1
print("list after concatenation is : ", end="")          # + => concatenation => adding two list
for i in range(0,len(lis2)):
    print (lis2[i], end=" ")
print ("\r")
lis3 = lis * 3                                        # $  * => print no of times
print ("list after combining is : ", end="")
for i in range(0,len(lis3)):
    print (lis3[i], end=" ")
# O/P => list after concatenation is : 1 2 3 4 5 6
#        list after combining is :  1 2 3 1 2 3 1 2 3
#                                                using $ max() to print the maximum element of the list       $ max()
print("the maximum element of list is : ", end="")
print(max(lis))
#                                 using count() to count the number of occurrence       $ count()
print("the number of occurrence of 3 after 3rd position is : ", end="")
print(lis.count(3))
#                                                                           Copy List
a = [2,5,4,3,6,1] print(a)
b = list(a)
print(b)
a[0] = 10
print(a)
#                                Shallow copy
import copy

a = [[1,2,3],[4,5,6],[7,8,9]]
print(a)
b = copy.copy(a)
print(b)
a.append(['a','b','c'])
print(a)
b = copy.copy(a)
print(b)
a[1][2] = 10
print(a)
b = copy.copy(a)
print(b)
#                                Deep Copy
import copy

a = [[1,2,3],[4,5,6],[7,8,9]]
print(a)
b = copy.deepcopy(a)
print(b)
a.append(['a','b','c'])
print(a)
b = copy.deepcopy(a)
print(b)
a[1][2] = 10
print(a)
b = copy.deepcopy(a)
print(b)
# to                                                                      iterate over 3 lists         using zip function 
import itertools 
num = [1, 2, 3]
color = ['red', 'while', 'black'] 
value = [255, 256]
# iterates over 3 lists and excutes  
# 2 times as len(value)= 2 which is the 
#                                       minimum among all the three  
for (a, b, c) in zip(num, color, value): 
     print (a, b, c)
#               over 3 lists using itertools.zip_longest
num = [1, 2, 3] 
color = ['red', 'while', 'black'] 
value = [255, 256] 
#                   Specifying default value as -1 
for (a, b, c) in itertools.zip_longest(num, color, value, fillvalue=-1): 
    print (a, b, c) 
#                                        Using try & except
a = ['Heena', 10, 'Rohit', 80, True]
try:
    a.remove(80)
except ValueError:
    print("Doesn't exist")
pass
print(a)
#                                                                                                       random.choice()
import random
numberList = [111,222,333,444,555]
print("random item from list is: ", random.choice(numberList))
movie_list = ['The Godfather', 'The Wizard of Oz', 'Citizen Kane', 'The Shawshank Redemption', 'Pulp Fiction']
moview_item = random.choice(movie_list)
print ("Randomly selected item from list is - ", moview_item)
moview_item = random.choice(movie_list)
print ("Randomly selected item from list is - ", moview_item)
#                                                                 sampling with replacement
list = [20, 30, 40, 50 ,60, 70, 80]
sampling = random.choices(list, k=4)
print("Randomly selected multiple choices using random.choices() ", sampling)
#                                                                              Applying Functions To List Items
regimentNames = ['Night Riflemen', 'Jungle Scouts', 'The Dragoons', 'Midnight Revengence', 'Wily Warriors']
# create a variable for the for loop results
regimentNamesCapitalized_f = []
# for every item in regimentNames
for i in regimentNames:
    # capitalize the item and add it to regimentNamesCapitalized_f
    regimentNamesCapitalized_f.append(i.upper())
# View the outcome
regimentNamesCapitalized_f
#                                    Create a                                     lambda function that capitalizes x
capitalizer = lambda x: x.upper()
# Map the capitalizer function to regimentNames, convert the map into a list, and view the variable
regimentNamesCapitalized_m = list(map(capitalizer, regimentNames)); regimentNamesCapitalized_m
#                                                                                              List Comprehension
regimentNamesCapitalized_l = [x.upper() for x in regimentNames]; regimentNamesCapitalized_l
#                                                         Remove using for Loop
List_example = [1, 2, 3, 4, 5, 6,7, 8, 9, 10, 11, 12]
print("Present List: ")
print(List_example)
for i in range(5, 8):
    print(i)
    List_example.remove(i)
    print("\nList after Removing a range of elements: ")
    print(List_example)
#                                                              Remove()
List_example = [1, 2, 3, 4, 5, 6,7, 8, 9, 10, 11, 12]
print("Present List: ",List_example)
List_example.remove(3)
print("Present List: ",List_example)
List_example.pop(3)
print("Present List: ",List_example)
#                                                  Indexing
letters = ['a', 'e', 'i', 'o', 'i', 'u', 'k', 'h']
print("Prints the index value of vowels in the above given list:")
indexa = letters.index('a')
print('The index of a:', indexa)
indexe = letters.index('e')
print('The index of e:', indexe)
indexi = letters.index('i')
print('The index of i:', indexi)
print(list1.index(4, 3, 8))
#                                                  Tuples
myTuple = 1, 2, 3, 4
del myTuple
myTuple[2:4]
t = (2, 5, 0) + (1, 3) + (4,)
2 in t
len(t)
max(t)
min(t)
# #                                                                                                      Recursive Function
# repetitively calling the same function until the loop reaches the desired value during the program execution by using the divide and conquer logic
get_factorial(5) 5 * get_factorial(4)
function get_factorial( n ):
if n < 2:
    return 1
else:
    return get_factorial(n -1)
#                               Recursion Code for Factorial
def get_recursive_factorial(n):
    if n < 0:
        return -1
    elif n < 2: #base condition
        return 1
    else:
        return n * get_recursive_factorial(n -1)
#                                                Factorial problem using iteration (looping)
def get_iterative_factorial(n):
    if n < 0:
        return -1
    else:
        fact = 1
    for i in range( 1, n+1 ):
        fact *= i
        return fact
print(get_recursive_factorial(6))
print(get_iterative_factorial(6))
#                                                                                                 $ with time calculation
import time


def get_recursive_factorial(n):
    if n < 0:
        return -1
    elif n < 2:
        return 1
    else:
        return n * get_recursive_factorial(n-1)
def get_iterative_factorial(n):
    if n < 0 :
        return -1
    else:
        fact = 1
    for i in range(1, n+1):
        fact *= i
        return fact
start_time = time.time()
get_recursive_factorial(100)
print("Recursion--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()
get_iterative_factorial(100)
print("Iteration--- %s seconds ---" % (time.time() - start_time))

sys.getrecursionlimit() # tells the limit for recursion
#                                                                Copy Using Constructor
a = [2,5,4,3,6,1] print(a)
b = list(a)
print(b)
a[0] = 10
print(a)
b = list(a)
print(b)
#                                        @classmethod decorator
class MyDecorator:
    def __init__(self, function):
        self.function = function
    def __call__(self):
        self.function()
@MyDecorator
def function():
    print("Beautiful Day")
function()
# class method with args and kwargs that are used as arguments
class cubeDecorator:
    def __init__(self, function):
        self.function = function
    def __call__(self, *args, **kwargs):
        result = self.function(*args, **kwargs)
        return result
# implementing class decorator to the function
@cubeDecorator
def get_cube(n):
    print("Number:", n)
    return n **3
print("Cube value is:", get_cube(10))
#   
def area_rectangle(l, b):
    try:
        print(l * b)
    except TypeError:
        print("area_rectangle Input should be integers")
area_rectangle(2,4)
area_rectangle('four','eight')
# error handling using the class decorator method
def exception_handle(func):
    def function(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except TypeError:
            print(f"{func.__name__} Input should be integers")
            return function
@exception_handle
def area_rectangle(l, b):
    print(l * b)
area_rectangle(4, 8)
area_rectangle('four','eight')
@exception_handle
def area_triangle(b, h):
    print(b * h / 2)
area_triangle(3,4)
area_triangle('four','eight')
#                               ErrorCheck
class ErrorCheck:
    def __init__(self, function):
        self.function = function
    def __call__(self, *params):
        if any([isinstance(i, str) for i in params]):
            raise TypeError("Input cannot be a string")
        else:
            return self.function(*params)
@ErrorCheck
def area_rectangle(l, b):
    print(l * b)
    print(area_rectangle(12, 3))
    print(area_rectangle('12', '3'))

#                                                             oops Concept
#                                                                                                             class :
# Template for Object
# any Attribute defined within a class definition but not within a fun() = class Attribute 
# it can share across all instances of the class, # changes are Visible to all other Instances
# Data & Functions are defined
# human = class, abith = object
# data, functions are bundled as Unit
Class Class_Name:                                 # class Declaration
Object_Name = Class_Name()
Object_Name.Method_Name()
Class_Name.fun()
def fun(self):
    print("the student name is : "+self.name) # define function with self as a parameter
    print("hi Class_Name")
def __init(self,name):  #                          Constructor Declaration
    self.name = Name
# function declaration with setting address
def setaddress(self,address):
    self.address=address
def getaddress(self):
    return self.address
# call setaddress with address as parameter
Abith.setaddress("chennai")
print(Abith.getaddress())  # call the getaddress
#                                                                                                                   object
# Identity, Properities, behaviour
# setting values
abith = abithclass("abith") # Object Declaration with Initializing
abith.fun()                 # Function call
Class pen:
a = 10
b = a+10
print("b")
penObject = pen
#                             Create an Object and call the fun(self)
class Abithclass:
    def __init__(self,name):  #                          Constructor Declaration
        self.name = name
    def Abithfun(self):
        print("hi"+self.name)
Abithobj = Abithclass("Abith")
Abithobj.Abithfun()
#                                 multiple Arguments
class Abithclass:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def Abithfun(self):
        print("hi" + str(self.a + self.b))
Abithobj=Abithclass(10,20)
Abithobj.Abithfun()
#                                                                   object types
import abc


class FourWheelVehicle (abc.ABC):
    @abc.abstractmethod
    def SpeedUp( self ):
        pass
class Car(FourWheelVehicle) :
    def SpeedUp(self):
        print(" Running! ")
        s = Car()
        print( isinstance(s, FourWheelVehicle))
#                                           
self = current object
class myclass:
    __hiddenVariable = int(0)                                                     # hidden number of myclass
def add(self, increment):self.__hiddenVariable += print(self.__hiddenVariable)
def myobject():
    myobject = myclass()
    myobject.add(2)
    myobject.add(5)
print(myobject.__hiddenVariable)
#                                                                                                                                  class Declare
class pen:
    int a;
    int(b)=a+10;
    print(b)
class Employee: #                                                                             declaring class & function
    def display(self):
        print("ID: %d nName: %s"%)

penObject #                                                                                                                           Object Declare
emp1 = Employee("john",101)           # creating object for class
emp2 = Employee("David",102)          #

emp1.display();                                                                      # access class method with Object
emp2.display();                                                          # Objects accessing the function

#                                                              to call an object
class Test:
    def __init__(self, a, b) : self.a = a, self.b = b
    def __repr__(self):
        return "Test a:%s b:%s" % (self.a, self.b)
    def __str__(self):
        return""
t = Test(619, 1234)
print(t)
print([t])

Class MyData
def __init__(self, string=None, list=None):
    self.mylist = []
    self.val = ""
    if string is not None:
        self.val = string
    elif list is not None:
        self.mylist = data
def GetData(self):
    print("self.List=> " + str(self.myList))
    print("self.val=> " + self.val)
c = MyData("Abith")
c.GetData()
# 
class Employee:
    def __init__(self,name,id):
        self.id = id;
        self.name = name;
    def display (self) : print("ID: %d nName: %s"%(self.id, self.name))
    emp1 = Employee("Abith", 619)
    emp2 = Employee("David", 102)
    emp1.display();
#    ID: 619
#    nName: Abith
#                                                                           $ class Object
class Student:
    def show(self,name):
        print("hello", name)
student = student()
student.show(name="Abith")
#                                                        determination of performance percentage of the employee
# multiple inheritance subject where the child class is responsible for calling the methods implied in its corresponding parent class.
#Define a class as 'Individual'#
import sys


class Individual:  #                               individual class defenition
    def __init__(self):  #    Constructor
        Valid_genders = ['Male','Female','transgender']
        self.Employee_Name = input( " Enter Name of the Employee : " )
        self.Employee_age = input( " Enter age of the Employee : " )
print( " Valid gender values are " )
print( " 1. Male " )
print( " 2. Female " )
print( " 3. Transgender " )
try:
    Employee_gender = input( " Enter gender of the Employee : " )
    if Employee_gender not in Valid_genders:
        raise Exception('valueerror')
except Exception as valueerror:
print("PLEASE ENTER A VALID GENDER")
sys.exit(0)
#                                                                       Method
def display(self):
    print( " ! ! ! ! ! EMPLOYEE PERFORMANCE CALCULATOR ! ! ! ! ! " )
    print( "  Employee Name : " , self.Employee_Name )
    print( " Employee Age : " , self.Employee_age )
#                                                               Define a class as 'Evaluated_Rating'      #
class Evaluated_Rating:
    def __init__(self):
        self.department = input( " department of the Employee : " )
        print( " Note : An employee produces more than 50 units with 7 average minutes perunit in a day " )
self.Productivity = int(input( " Average productive units by the employee per day : " ) )
self.production_time = int(input( " Average production time for one unit by the employee :  " ) )
#                         Method
def display(self):
    print( " Employee Deparment : " , self.department )
    performance_percentage = (self.Productivity * self.production_time)/100
    print( " Performance percentage : " , performance_percentage )
    if (performance_percentage > 4 ) :
        print(" THE EMPLOYEE HAS SCORED RATING 3 ")
    elif (performance_percentage > 6 ) :
        print(" THE EMPLOYEE HAS SCORED RATING 2 ")
    elif (performance_percentage > 9):
        print(" THE EMPLOYEE HAS SCORED RATING 1 ")
class Employee(Individual, Evaluated_Rating):
    def __init__(self):
        Individual.__init__(self) #       Call ' Individual ' super class constructor
        Evaluated_Rating.__init__(self) # Call ' Evaluated_Rating ' super class constructor
def result(self):
    Individual.display(self)  # Call method of class 'Individual'
    Evaluated_Rating.display(self) # Call method of class 'Evaluated_Rating'
#                        Objects of class 'Employee1'
Employee1 = Employee()
Employee1.result()  #                  object using the methods of the declared class
#                   Objects of class 'Employee'    
Employee2 = Employee()
Employee2.result()               # object using the methods of the declared class
print("                                                                           ")
print( "Note: The instances get initialized with the given values Successfully " )
#                                                               Constructor = Default Child => Class name + Function Name
# constructor functions automatically call functions when objects are created
# normal functions = object.display(); we have to call function manually
# Constructor = def __init__(): , def display():, with(self,parameter)
class pen:
    def __init__(self, name):
        a = 10;
    def display():
        b = 20;
#  Constructor
class pen:
    {
        pen()
    {
        int a=10;
    }
    display();
    {
        int b=20;
    }
    Void Main()
    {
        pen penObject = new pen();
    pen.display();
    }
penObject:  # access the class method using Object
    __init__()
#                                                                                                                            self
# used to specify the current instance, Multiple objects cannot be created using (self)
# used in functions declared in a class
# this =(or) self => i'd or name in a box of rows and columns
# dec = E("Abith",101)

#                                                                                                 declaring private methods (def)

# Private methods and variables can be declared with the addition of two or more underscores and at most one trailing one. You can also bind names to class instances
class MyClass(object):
    common = 10
def __init__(self):
    self.variable = 3
def myfunction(self, arg1, arg2):
    return self.variable
class instance = MyClass()
class instance.myfunction(1, 2)
# 3
class instance2 = MyClass()
class instance.common
# 10
class instance2.common
# 10
MyClass.common = 30
class instance.common
# 30
class instance2.common
# 30
class instance.common = 10
class instance.common
# 10
class instance2.common
# 30
MyClass.common = 50
class instance.common
# 10
class instance2.common
# 50
def __init__(self, arg1):
    self.variable = 3
    print arg1
class instance = OtherClass("hello")
# hello
class instance.myfunction(1, 2)
# 3
class instance.test = 10
class instance.test
# 10
#                                                                                                         Method Overriding
class Animal:  
    #                     properties
	multicellular = True
	#                                           Eukaryotic means Cells with Nucleus
	eukaryotic = True
	#                               function breathe
	def breathe(self):
	    print("I breathe oxygen.")
    #                               function feed
	def feed(self):
	    print("I eat food.")
def feed(self):
    print("I eat only plants. I am vegetarian.")
herbi = Herbivorous()
herbi.feed()
#                   calling some other function
herbi.breathe()
#                                                                                                $ define derived-class
class    derivedClassName([list, ...]):
class cuisine():                                                                    # class cuisine
    def __init__(self, type, cooked=None):
        self.type = type
        return cooked-cuisine=newcusine('cooked')
#
viod sum()
{
    a = a+10;                                                    # function with no parameter & no return type
}
int sum()
{
    a = a+10;                                                    # function with no parameter & 1 return type
return a;
}
void sum(int a)
{
a = a+10;                                                        # function with  parameter & no return type
}
int sum(int a)
{
a = a+10;                                                        # function with  parameter &  return type
return a;
}
#                                                                                               $   Polymorphism
#  Polymorphism = Poly + Morph => "many forms"
#                                                   Function Overloading
def add(a, b):
	return a + b
add(4,5)
#                   to add 3 numbers
def add(a, b, c):
	return a + b + c
#                   to add 4 numbers
def add(a, b, c, d):
	return a + b + c + d
#                                                   Operator Overloading
2 + 5
("Abith" + "Raj")
"Abith"*3

#                                                                                               $   Encapsulation (Object)
# storing or placing the data to make it readable & compact
# Enclosing Variables & methods inside class to safeguard it
# methods + Variables = Encapsulation
# variable = int b=1; , methods = public static void addition(); /n }
viod main()
{
      pen PenObject = new pen()
{
class pen:
{
    program to create a pen
}
}
#                                                                                               $   Abstraction(Class)
# hide internal functions & show only essential (class attributes)
# without creating an Object in Encapsulated
package sklearn
class Abith:
{
         int(a) == 10, int(b) == 20
         sum()
{
         a = a+10:
}                                                         # Encapsulation
     public static viod main(string args[])
{
         Abith AbithObject=new Abith();                        # Abstraction
     AbithObject.sum();
}
{
  javafunctions javaFunObject=new javafunctions();
  system.out.println(javaFunObject.b);
}     
}
#                                                                                                                  abstract method
import abc


class Myinterface( abc.ABC ):
    @abc.abstractclassmethod
    def disp( ):
        pass
print(" Hello from Myclass ")
class Myclass(Myinterface):
    def disp(s):
        print(" Hello from Myclass ")
o1=Myclass()
o1.disp()
#                                                        abstract class implement by multiple derive classes
import abc


class FourWheelVehicle (abc.ABC):
    @abc.abstractmethod
    def SpeedUp( self ):
        pass
class Car(FourWheelVehicle) :
    def SpeedUp(self):
        print(" Running! ")
class TwoWheelVehicle (abc.ABC) :
    @abc.abstractmethod
    def SpeedUp(self):
        pass
class Bike(TwoWheelVehicle) :
    def SpeedUp(self) :
        print(" Running!.. ")
a = Bike ()
s = Car()
print( isinstance(s, FourWheelVehicle))
print( isinstance(s, TwoWheelVehicle))
print( isinstance(a, FourWheelVehicle))
print( isinstance(a, TwoWheelVehicle))
# o.p = True, False, False, True

#                                                                                                               $ Inheritance
# function to call class using objects , to call father class using child class
# building blocks of any scalable & maintainable piece in a software
# one class to derive or inherit properties of another class, adding new features without modifying them
# existing classes can be modified by a new class
# Existing class = base class
# new class = derived class
# single-Inheritance = 1 base class, inherited by one derived class, derived class automatically invokes the base class Constructor
# Multiple-Inheritance = multi-base classes inherited by 1 derived class, the base class Constructor are invoked in order in which classes are derived
#                                                  $ derived types of Inheritance = combining two forms of Inheritance
# hierarchical Inheritance = 1 base class inherited by multiple derived classes, Objects share the class variables to different classes
# Multi-level Inheritance = A derived class serving as a base Class for another derived class, the base class Constructor are invoked recursively
# hybrid Inheritance = A combination of hierarchical & Multi-level inheritance, any combination of classes
#                                                                                                 $  Single Inheritance
class indian_cuisine(cuisine):                 # cuisine = class
    def __init__(self,type,place):                                  # creating class
        super().__init__(type)
        self.place = place           # used only in derived class, not visible to base class
        return indian_cuisine
        newcuisine('cooked','India')
#                                                                                          $    Hierarchical Inheritance
class italian_cuisine(cuisine):
    def __init__(type,self,place):    # __init__(self) = constructor
        super().__init(type)  # super() = access method from a parent class from within a childclass
        self.place = place
        return italian_cuisine
        newcuisine(cooked=None,'Italy')
#                                                                                               $  Multiple Inheritance
class fine_dine_cuisine(indian_cuisine,italian_cuisine):
    def __init__(self,type,place,portion_size):
        super(fine_dine_cuisine, self).__init__(type, place)
        self.portion_size = portion_size  # portion_size object parameter not shared to base classes
        return
    fine_dine_cuisine = new-cuisine("cooked',India",4)
# Diamond Inheritance
#                                                     issubclass()
class Parent:
  	var1 = 1
  	def func1(self):
  	    # do something
class Child(Parent):
  	var2 = 2
  	def func2(self):
  	    # do something else

issubclass(Child, Parent)
Parent p = Parent()
Child c = Child()
#                                   Determining the type of Inheritance
#
# (1) is instance(myObj,int) (2) is subclass(bool,int)
class Abith:
    a = 5
class Abi:
    a = 5
AbithInstance = Abith()
print(isinstance(AbithInstance, Abi))
#                                        Multiple Inheritance(4 Types) = Multiple Class
# Multiplier
#   $
def multiplier():
    Return[lambda]
    x, i = i:i * x
    for i in range(4)]
#                                                                                                                          Multiple Inheritance in Python
print([m(2) for m in multiplier()])
print([m(3) for m in multiplier()])
# syntax of multiple inheritances involving three base classes and a derived class
class Base_1:
pass
class Base_2:
pass
class Base_3:
pass
class DerivedClass(Base_1, Base_2, Base_3)
pass
class A:
def A(self):
print('This is class A.')
class B:
def B(self):
print('This is class B.')
class C(A,B):
def C(self):
print('This is class C which inherits features of both classes A and B.')
o = C()
o.A()
o.B()
o.C()
#                                    This class will derive length and breadth inputs from the respective base classes.
class length:
l = 0
def length(self):
return self.l
class breadth:
b = 0
def breadth(self):
return self.b
class rect_area(length, breadth):
def r_area(self):
print("The area of rectangle with length "+str(self.l)+" units and breadth "+
str(self.b)+" units is "+str(self.l * self.b)+" sq. units.")
o = rect_area()
o.l = int(input("Enter the required length for rectangle: "))
o.b = int(input("Enter the required breadth for rectangle: "))
o.r_area()
#                                                         convert the string input values to float (or) any decimal type
class length:
l = 0
def length(self):
return self.l
class breadth:
b = 0
def breadth(self):
return self.b
class rect_area(length, breadth):
def r_area(self):
print("The area of rectangle with length "+str(self.l)+" units and breadth "+
str(self.b)+" units is "+str(self.l * self.b)+" sq. units.")
o = rect_area()
o.l = float(input("Enter the required length for rectangle: "))
o.b = float(input("Enter the required breadth for rectangle: "))
o.r_area()
#                                                                                                                                    $ single inheritance
# a derived class is derived only from a single parent class & allows a class to derive behaviour & properties from single base class
# adding new features to a class
class Parent_class_Name:                               #  Parent_class code block
class Child_class_Name(Parent_class_name):             #  Child_class code block
class Parent_class(object):                           # Base class
def __init__(self, name, id):                         # Constructor
self.name = name
self.id = id
def Employee_Details(self):                          # To fetch employee details
return self.id , self.name
def Employee_check(self):
if self.id > 500000:                                  # To check if this  is a valid employee
return " Valid Employee "
else:
return " Invalid Employee "
class Child_class(Parent_class):                       # derived class or the sub class
def End(self):
print( " END OF PROGRAM " )

Employee1 = Parent_class( "Employee1" , 600445)                                                  # parent class object
print( Employee1.Employee_Details() , Employee1.Employee_check() )
Employee2 = Child_class( "Employee2" , 198754)                                                   # child class object
print( Employee2.Employee_Details() , Employee2.Employee_check() )
Employee2.End()

class Parent_class(object):                                  # Base class
def __init__(self, value1,value2):                          # Constructor
self.value1 = value1
self.value2 = value2
def Addition(self) :
print(" Addition value1 : " , self.value1)        # To perform addition
print(" Addition value2 : " , self.value2)
return self.value1 + self.value2
def multiplication(self) :
print(" multiplication value1 : " , self.value1)
print(" multiplication value2 : " , self.value2)
return self.value1 * self.value2
def subraction(self) :
print(" subraction value1 : " , self.value1)
print(" subraction value2 : " , self.value2)
return self.value1 - self.value2
class Child_class(Parent_class):       # derived class or the sub class
pass
                                                      # Driver code
Object1 = Child_class(10,15)                          # parent class object
print(" Added value :" , Object1.Addition() )
print( " " )
Object2 = Child_class(20,30)                         # parent class object
print(" Multiplied value :" , Object2.multiplication() )
print( " " )
Object3 = Child_class(50,30)                         # parent class object
print("Subracted value :" , Object3.subraction() )

#                                                                                           Interface
# template for designing classes
# class contains nonabstract methods. 
# Abstract methods are those methods without implementation without the body
# implementation of these abstract methods is defined by classes that implement an interface
# Python does not require that a class which is implements an interface to provide the definition for all the abstract methods of an interface
# to Create Interface = Informal Interfaces & Formal Interfaces
#                                                                                                       Informal Interfaces
# Protocols or Duck Typing. The duck typing is actually we execute a method on the object as we expected an object to have, instead of checking the type of an object.
# protocol because it is informal and cannot be formally enforced. 
# It is mostly defined by templates or demonstrates in the documentations. """
# methods we usually use – __len__, __iter__, __contains__
#                                     __len__, __contains__
class Fruits :
    def __init__( self, ele):
        self.__ele = ele
    def __contains__( self, ele):
        return ele in self.__ele
    def __len__( self ):
        return len( self.__ele)
Fruits_list = Fruits([ "Apple", "Banana", "Orange" ])  
print(len(Fruits_list))                                # protocol to get size
print("Apple" in Fruits_list)                          # protocols to get container
print("Mango" in Fruits_list)                          # check the membership by using the in operator.
print("Orange" not in Fruits_list)  

#                                                                      Formal Interfaces
# interface or base classes define as an abstract class in nature and the abstract class contains some methods as abstrac
# Abstract Base Classes
import abc


class Myinterface( abc.ABC ):
    @abc.abstractclassmethod
    def disp():
     pass
class Myclass( Myinterface ) :
    pass
#                                                    derived class defines an abstract method
import abc


class Myinterface( abc.ABC ):
    @abc.abstractclassmethod
    def disp( ):
        pass
#                            print(" Hello from Myclass ")
class Myclass(Myinterface):
    def disp( ):
        pass
    print(" Hello from Myclass ")
o1=Myclass()

#                             derived class which defines an abstract method with the proper definition
import abc


class Myinterface( abc.ABC ):
    @abc.abstractclassmethod
    def disp( ):
        pass
#                  print(" Hello from Myclass ")
class Myclass(Myinterface):
    def disp(s):
        print(" Hello from Myclass ")
o1=Myclass()
o1.disp()
#                                                           Example of object types

import abc


class FourWheelVehicle (abc.ABC):
    @abc.abstractmethod
    def SpeedUp( self ):
        pass
class Car(FourWheelVehicle) :
    def SpeedUp(self):
        print(" Running! ")
        s = Car()
        print( isinstance(s, FourWheelVehicle))

#                                                        abstract class implement by multiple derive classes
import abc


class FourWheelVehicle (abc.ABC):
    @abc.abstractmethod
    def SpeedUp( self ):
        pass
class Car(FourWheelVehicle) :
    def SpeedUp(self):
        print(" Running! ")
class TwoWheelVehicle (abc.ABC) :
    @abc.abstractmethod
    def SpeedUp(self):
        pass
class Bike(TwoWheelVehicle) :
    def SpeedUp(self) :
        print(" Running!.. ")
a = Bike ()
s = Car()
print( isinstance(s, FourWheelVehicle))
print( isinstance(s, TwoWheelVehicle))
print( isinstance(a, FourWheelVehicle))
print( isinstance(a, TwoWheelVehicle))
# o.p = True, False, False, True



#                                                                                                                            basic-Concepts
# function name = library name
# indentation statement ends with : , = = assign a value, == = decrement the values
# UniCode = u"This is Unicode"
# flow control statements are while, for, if. if number in (3, 4, 7, 9): / break / else: / continue / else: / pass
# def to declare fun, items memory location is passed, binding another object to variable
# func-var = lambda x: x + 1 / print func-var(1) / def passing_example(a_list, an_int=2, a_string="a default string"):
# a_list.append("New Item") / an_int = 4 / return a_list, an_int, a_string / my_list = [1, 2, 3] my_int = 10 / print / passing_example(my_list, my_int)
# bind names to class Instance = class MyClass(object): / common = 10 / def __init__(self): / self.variable = 3 / def myfunction(self, arg1, arg2):
# return self.variable / class instance = MyClass() / class instance.myfunction(1, 2) / class instance2 = MyClass() / class instance.common / def __init__(self, arg1): / self.variable = 3 / print arg1 / class instance = OtherClass("hello")
print "Hello, World!" ; print "This is second line"
# In python, you can use single quotes '', double quotes "" and even triple quotes  to represent string literals
word = 'word'
sentence = "This is a one line sentence."
para = """This is a paragraph 
which has multiple lines"""

#                                                                                                                        palindrome
Number = input('Enter the number to be verified : ')
# Try  block
try:
    #Casting of the entered input is also achieved here by implying         #variable casting process into place
    val = int(Number)
    # checking for a palindrome in the given string
    if Number == str(Number)[::-1]:
        print('The given number is PALINDROME')
    else:
        print('The given number is NOT a PALINDROME')
except ValueError:
    print("! ! ! A valid numeric input is not entered ! ! !")

# # This program performs                               palindrome check for a string #
# function which                                           return reverse of a string
def isPalindrome(s):
    # Calling reverse function
    if len(s) <= 1 :
        return True
    if s[0] == s[len(s) - 1] :
        return isPalindrome(s[1:len(s) - 1])
    else :
        return False
        #                                       Driver code
Palindrome_input_Variable = [ ' AnnA ' , ' SoloS ' , ' RotatoR ' , ' RadaR ' , ' SagaS ' , ' RotoR ' , ' TenT ' , ' RepapeR ' , ' CiviC ' , ' KayaK ' , ' Lever ' , ' MadaM ' , ' RacecaR ' , ' StatS ' , ' Redder ' , ' Wow ' , ' MoM ' , ' RefeR ' , ' NooN ']
print( " PALINDROME CHECK PROGRAM " )
for i in Palindrome_input_Variable:
    ans = isPalindrome(i)
    if ans == 1:
        print( " The given string  ", "'" , i , "' ","is a palindrome")
    else:
        print( " The given string  " , "'" , i , "' ","is not a palindrome")

#                               Casting of the entered input is also achieved here by implying
#variable casting process into place.
num = int( input ( " ENTER THE NUMBER: " ) )
temporary = num
rev = 0
# looping the given input and reversing the value
while temporary != 0:
    rev = ( rev * 10 ) + ( temporary % 10 )
    temporary = temporary // 10
if num == rev:
    print( " number is palindrome " )
else:
    print( " number is not palindrome " )

#                                    reversing the given number using a mathematical formula
rev = (rev * 10) + (temporary % 10)
temporary = temporary // 10

# convert data structures to strings with the use of the pickle library using file I/O :                                 $ Convert string using pickle lib
my-file.write("This is a sample string")
my file.close()
my file = open(r"C:\\text.txt")
print(my file.read())
'This is a sample string'
my file.close()
# Open the file for reading.
my file = open(r"C:\\binary.dat")
loaded-list = pickle.load(my-file)
my file.close()
print(loaded-list)
['This', 'is', 4, 13327]
# 
 #                                                                                                                         (With) File Handling
# dir(object) = object.__doc__ to find its document string
# pointer = points the position of the file to read / write from that position. is like text cursor which can be shifted freely (using arrow keys)  except that pointer can shift/read/write only through some functions.
# connect with programs to perform read, write, append,  modify the data.
# File types = Text, Binary. file(), open() , 1st create a file object $ myFile = open([path], [access mode], [buffer size])
# buffer size = how many chunk of data
# c: (or root) / myFile = open("file.txt") / file handling.py / file.txt
# access modes : Read = "r", "rb", for txt & binary : r+,rb+, eb+, w+ = read & write
# $ with open(file.txt, "r+"): class = file() or open(),
# myFile = open("file.txt", "r", "w", "a"), myFile.close(), a = append
# 'a+" = read/append, "ab+" = append/read modes on binary Files
#                                                                  Program for File Handling
import os


def listfile(types):
    current_path,filename = os.path.split(os.path.abspath(__file__))
#                                                                 Nested Looping Section in The Program
# Outer  For Loop
for path,dir,file in os.walk(current_path):
    file_name = str(file)
#                                                                  Inner For Loop
for type in types:
    if file_name.endswith(type):
        print(file_name)
def deletefile(types):
    choice2 = input("Please enter the file to delete : ")
    os.remove(choice2)
types = [".txt']",".srt]",".py]"]
#                                                                     Header Area
print(" = = = = = = = = = = = = = = = = = = = = = " )
print(" $$$$$$$$$$$$$ FILE HANDELING $$$$$$$$$$$$ ")
print(" = = = = = = = = = = = = = = = = = = = = = ")
# File Listing
File_list = listfile(types)
#                                                                  File Operation
# 
print("                      ")
print(" %%%%%%%%%%%%%%%%%%%%")
print(" SELECT AN OPERATION ")
print(" %%%%%%%%%%%%%%%%%%%%")
print( " DEL - Delete a file Type ")
print( " END - EXIT ")
choice = input(" Please enter the desired operation : ")
if choice == 'DEL':
    File_deletion = deletefile(types)
    listfile(types)
    exit
    if choice == 'END':
        Print( "Bye Bye" )
        exit
    else:
        Print( "Invalid Option" )
        exit
#                                                                                                                          $    dictionary
#                                                                                                                                Dictionary
# Un Ordered collection of key & value pairs as hashes
# Dict = {} $ print("Dict: ") = New Empty Dictionary
# Access a Dict Element using Key (Index Value Keys)
# Methods Used = copy(), clear(), pop(), popitem(), get(), dictionary_name.values(), str(), update(), setdefault(),
#                keys(), items(), has_key(), fromkeys(), type(), cmp(),
# AbithDict = {}
intDict = {10: "c++", 20: "java", 30: "PyThOn"}  #                                                          
identity = {"Name": "Abith", "Type": "Tech", "Link": "https://facebook.com/Abith.Raj", "tag": "My Profile"}
print(identity["Name"] + ": " + identity['tag'])
# 
update() # merging two Dictionaries to One
identity.update() # merging two List in Dict{}
#                                               creating a Dictionary        => Dict{"key-1":"element-1", 1: [0, 0, 0]}
AbithDict = {"Abith":"Raj", 1: [6, 1,9]}
print("\nDictionary with the use of Mixed Keys: ")
print(AbithDict)
# o/p = Dictionary with the use of Mixed Keys: 
# {'Abith': 'Raj', 1: [6, 1, 9]}
#                                                                 with dict() method
AbithDict = dict({1: 'Abith', 2: 'For', 3:'Internship'})
print("\nDictionary with the use of dict(): ")
print(AbithDict)
#                                                      with each item as pair
AbithDict = dict([(1, 'Abith'), (2, 'For')])
print("\nDictionary with each item as a pair: ")
print(AbithDict)

#  $ check weather the inserted items exists or not                            $   Checking Dictionary
A = 619
 abithDiction = {}
 for I in range(0, p) :
     char = 'Abith' [i%4] try:
         abithDiction[char] += 1
 except KeyError:
     abithDiction[char] = 1
print(abithDiction)

#                                     Accessing the Dictionary                                                             $ Accessing
# Accessing element using keys
print(AbithDict['Dict1'])
print(AbithDict['Dict1'][1])
print(AbithDict['Dict2']['Name'])
#                                 $ Accessing Keys
print(AbithDict.keys())
#                                Accessing values
print(AbithDict.values())
#                                                                   $ Nested Dictionary
AbithDict = {'Dict1': {1: 'Abith'}, 'Dict2': {'Abith': 'Raj'}}
#                                                                            Deleting element using keys
AbithDict = { 1: 'Abith', 2: 'Raj', 3: 'S' }
del AbithDict[2]
print(AbithDict)
#                                                    pop specific element 
AbithDict = { 1: 'Abith', 2: 'Raj', 3: 'S' }
AbithDict1.pop(1)
print(AbithDict1)
#                                                          pop element 
AbithDict = { 1: 'Abith', 2: 'Raj', 3: 'S' }
AbithDict2.popitem()
print(AbithDict2)
#                                                          Delete Dictionary
AbithDict = { 1: 'Abith', 2: 'Raj', 3: 'S' }
AbithDict3.clear()
print(AbithDict3)
#                                                       $ dictionary Functions
len(), clear(), values(), keys(), items(), has_key(), cmp()
# clear() = empty or delete
# items() = displays both key & values
# has_key() = check key exists, True or False
# cmp() = compare two Dictionaries = return 3 values = 1, 0, -1
# equal = 0, more elements = 1, less elements = -1
cmp(x, y)
#                                                                                    Using Dictionary Mapping Function
def get_week_day(argument):
    def zero():
        return "Sunday"
    def one():
        return "Monday"
switcher = {
    0: zero(),
    1: one(),
    }
#        return switcher.get(argument, "Invalid Day")
if __name__ == "__main__":
    print (get_week_day(0))
    print (get_week_day(1))
#                                                                                                Tuples(ImMutable, in)
tup = (6,1,9) or 6,1,9
tup[0] # = 6  # Indexing
tup[1:] # = 1,9  Slicing
tup[-1] # = 9
tup[:-1] # = 6,1
tup1 = 2,3,4
tup > tup1 #    Compare   = True or False
len(tup)
max(tup)
min(tup)
tup2 = tuple(list) #          generate list values
tup = (6,1,9) + 1,3 + (4,)
Abi = 6,1,9
type(Abi)
tup = Abi + (7,) #            add elements to tuple
print(tup*3)     #            all elements repeating 3 times
tup = (6,1,9) + (1,3) + (4,)
print(tup)
2 in tup
6 in tup
#                                                                                                SETS
# collection of Unordered or Ordered Data, mutable and Im-Mutable
# each Element must be Unique, Immutable, Duplicate Items are removed
# Object in SETS are Mutable
set.add(619)
set.clear()
set.copy()
set.discard(719)
set.remove(519)
set.update(916)
set.pop() # Deletes the First element in a SET
#                                   Creating, Declaring a Set
Days = {"Monday",
"Sunday"
}
print(Days)
print(type(Days))
print('Looping through the SetS Elements,,....')
for i in Days:
    print(i)
#                                   Un-Orderd Data 
set = {12,23,14,619,916}
type(set)
set #      O/P = {12, 14, 23, 619, 916}
#                                              MUTABLE                   Set Operations, Union()
# Union() = |, Intersection() = &, Difference() = -, Symmentric_difference() = ^
Days1 = {"Monday","Tuesday",}
Days2 = {"Saturday","Sunday"}
print(Days1|Days2)
print(Days1.union(Days2))
#                           Adding two sets without Duplicate value
set1 = {13,34,619,67,34,85}
print(set|set1)
print(set.intersection(set1))
print(set.intersection_update(set,set1)) # Update only common values
print(set1-set2)
print(set1.difference(set2))
print(set1^set2)
print(Days1.SymmetricDifference(Days2))
#                                         Frozen Set = Immutable
FrozenSet = frozenset([6,1,9])
print(type(FrozenSet))
for i in Frozenset:
    print(i)
Frozenset.add(6) # unable to add or change
set = frozenset(set1)
#                                                                                              String Manipulations & Functions

# len(s) in string counted with quotes in middle separate with coma or exclude with \
#  Array = (' ', " ", " ')
# S = '"Abith"', \t      Raj, \n S / print(S) O/P = Abith Raj
#  \t = tab    space, \n = next line
# Slicing the string = print(s[0:-2]) = Abi : -2 = last two Letters is removed        $ Slicing
# slicing[1:2] = 1:2-1 = 2 arguments = starting, ending -1, stepping value
# Concatenation = combining two statements : s1 = "Abith" 'Raj' / s1 = ("Abith",'Raj')
# / s2 = "-' / print(s2.join(s1)), 
# Stepping or Stepper : stepping[1:2] = 3 arguments = starting, ending -1, stepping value  
# a = "Abith" / b = ''Raj / sum = a + b / print(sum)
# Finding letters or values in string = print(s1.find(s2))
# Finding in Reverse = print(s1.rfind(s2))
rfind()
print('Illustration of find() with no start and end parameters')
string = "what comes easy won't last \nwhat lasts won't come easy"
print("Input String :")
print(string)
print("index of newline :", string.find('\n'))
print("index of (won't) :", string.find("won't"))
print("index of (come) :", string.find('come'))
print("index of (easier) :", string.find('easier'))
print('\n')
print('Illustration of find() with start and end parameters')
print("index of (won't) :", string.find("won't", 18)) # start : 18
print("index of (come) :", string.find('come', 5, 15)) # start : 5 and stop = 15
print("index of (come) :", string.find('come', 10)) # start : 10
# if s1.startswith(s2) : if s1.endswith(s2)

# if s1.islower(): , if s1.upper():

# print(s1.title()) , print(s1.swaps())
# print(s1.swaps().title().upper().lower())
#                                                                                                     Advanced Functions in string
# print(s1,centre(15)), print(s1.l just(15)), print(s1.r-just(15)), l-just = left justification
# to Check = if s1.isalpha():, if s1.isalnum():, if s1.isspace():, alpha = alphabet
# Extracting sub domain name from a given list of URls using                                                   strip() function
urls = ['www.facebook.com', 'www.yatra.com', 'www.youtube.com']
print("sub domains:")
for url in urls:
    print(url.strip('w.com'))
# strip([chars]), lstrip([char]) and rstrip([char]) when optiona parameter [char] is specified
string = '********Python Trim String**********'
print('Input String', string)
print('length :', len(string), 'chars')
print('\n')
print("strip()--> * will be removed from both ends")
str1 = string.strip('*')
print(str1)
print('length :', len(str1), 'chars')
print('\n')
print("lstrip()--> leading * from the string will be removed")
str2 = string.lstrip('*')
print(str2)
print('length :', len(str2), 'chars')
print('\n')
print("rstrip()--> trailing * from the string will be removed")
str3 = string.rstrip('*')
print(str3)
print('length :', len(str3), 'chars')
#                                                                                                       Split String
str = 'Python split strings article'
print(str.split())

items = 'Cheese, Curd, Butter, Milk '
print(items.split(', ', 2))
print(items.split(', ', 1))

txt = "apple, pineapple, custardapple"
print(txt.rsplit())
print(txt.rsplit('t', 1))
#                                                                                                                          Type Conversion 0r Casting
# Implicit = Automatically converts one data type to another data type int() to float()
# Explicit = users convert the data type of objects to required data type, use predefined functions like float() to int()
## int(), float(),  (Only Used)
num = int( input())
num = num + 1002
print (num)
#                                                       $    Converting int to float
x = 10
print(x,'is of type:',type(x))
x = float(x)
print(x,'is of type:',type(x))
#                                                              Adding Strings
year = 35
greeting = "this year is " + str(2020)
# greeting = o/p
#                                                                           Input()
num  = input (‘Enter the number: ‘)
# enter the number: 10
# Here 10 is not a number, this is a string.
# To convert this into a number we can use int( ) or float( ) functions.
int( ‘10’ )
# 3
float(‘10’)
# 3.0 = o/p
#                                                                  presenting or formatting output
variable='15'                                                                                      $ Explicit
print("the value of data is %s"%variable) = str()
variable=it("15")                                                           $ implicit
print("the value of data is %d"%variable) = int()
print("the value of data is %f"%variable) = 15.00 = float()
print("the value of data is %r"%variable) = raw data
"""
#                                                                                                                                       String Formatting
#                     Formatting the Output
# %s = String, %d = integer, %f = floating Value, %b = Boolean
# message4 = '{:     10.2f  } and {:d}'.format(1.234654587, 12)
# 
rollNo= 1
subject= "Maths"
print("the roll No. %s studies %s subject" % (rollNo, subject))
# the roll No. 1 studies Maths subject
"""
"""
#                                                                                    String Formatting                                            (.format)
rollNo = 1;
subject = "maths"
print(" The roll no. (0) studies (1) subject".format(rollNo, subject))
print(" The Roll No. (rollNo) studies (subject) subject". format(rollNo=10, subject="science"))
"""
val = (input())
if val,".30":
    print("Correct")
else:
    print("Wrong")

msg = (input())
print(msg)

msg = (input())
print("the value is", msg)

#                                                        String Formatter....

msg = (input())
print(f"the value is %s" % msg)

# String Formatting                                      (.format)...

msg = "Abith"
print("the value is (619)".format(msg))

rollNo = 1
subject = "maths"
print(" The roll no. (0) studies (1) subject".format(rollNo, subject))
print(" The Roll No. (rollNo) studies (subject) subject".format(rollNo=10, subject="science"))
#                                                                                                         with Spaces
# $ message3 = '{:10.2f} and {:d}'.format(1.234234234, 12)
# :10. => 10 Spaces before the decimal, 2f => 2 Spaces after the decimal
#                                                                                                              Range() function
# Generates List of Numbers in syntax with endValue = -1
range(start, end, step) #=> startValues, endValues, step = increment Value
range(3, 10) #=> [3, 4, 5, 6, 7, 8, 9]
range(4, 10, 2) #=> [4, 6, 8]
range(end)# => range(5) => [0, 1, 2, 3, 4]
for x in range(0,5):
    for i in range(0,x):
        print(i+1,end=' ')
    print("")
#                                     Finding Sum and Average of n Numbers
a = int(input('Enter Number: ')) # i/p = 619
sum = 0
avg = 0
for i in range(a):
    sum+=i
    avg = sum/a
    print(sum)
    print(avg) # o/p = 1238 Lines
#                                                                                         Check File Types & Existence

# os.path.exists(), os.path.isfile(), os.path.isdir(), os.path.getsize(), os.path.getmtime() = Returns TimeStamp

#                                                                                                                                $      LIST

# 1-D array : Tuples = any type, -ve number from end to beginning, :colon to access any range, 3rd parameter = N
# Two Methods = append() = Nested, extend()
# L = [1, "a" , "string" , 1+2] # print(l append)
# tuple => to fill a string with values use % operator and a tuple (eg) print "Name: %s Number: %s  string: %s" % (myclass.name, 3, 3 * "-")
# 
#                                                Remove Duplicates in a List :
#  """
mylist = ["a", "b", "a", "c", "c"]
# mylist = list(dict.fromkeys(mylist))
# print(mylist) """
# Note : Output is Generated in Random

# append() add elements at the end of the List & extend() add elements at the end of the List from another List
# _init_.py Importing a Module in a Directory $ import main dir.subdir.module
# print(x//y) Integer Division --> (i.e) quotient value is Rounded to the Next Smallest Whole Number.


# $ Unary + Binary = Operator - 7 Types = Arithmatic,Comparison,Assignment,Logical(or)Boolean,BitWise,Membership,Identity           Operator


#           Arithmatic Operator = 7 Types +,-,*,/,%,//,**  (eg) - print('x // y =',x//y)
# % = to find the remainder of the division
# // = floor division operator , the results are converted into whole numbers by adjusting the number to the left
# ** = exponent operator, operand raised to the power of right-side operator

# Comparison Operator ==,>,<,>=,<=,!=

# Assignment Operators =,+=,-=, *=, /=, %=, //=, **=,  (Unary Structure)
'''In[1]: a = 12
In[2]: a += 10
In[3]: print(str(a))
22
'''
# Unary Operator = 3 Types = Arithmatic, Boolean, Relational = Requires min two Operands                                        UNARY OPERATORS
# Arithmatic Unary Operators = +,-,*,/,%,//,**
# Boolean Unary Operator and, or, and not (True or False)
# Relational Operator = <, <=, >, >=, ==, !=,
# Object Identify Operator = ( == ), ( is ) or (" == "),(" is ")
# Bitwise Operator = ~ = Negation, ^ = Exclusive or, & = and, | = or, << = Left Shift, >> = Right Shift

# Boolean Operators = Boolean Value, Comparison, Binary Boolean, not,
# Boolean Value = bool_var = True  (True or False)
# Comparison Operator = <, <=, >, >=, ==, !=, **,
# Binary Boolean = Truth Table for and = Both Conditions must be true
#                  Truth Table for or = any1 Condition must be true
#                  Truth Table for not = True = False, False = True

# Combining Binary Boolean & Comparison operator: (5 > 3) and (7 != 8) and not False = True

#        Identity   Operator  = 2Types = is, is Not
#        Membership  Operator = in, not in (eg) x not in y

#        Remainder Operator = % ,
#                               Used in floating numbers, Range , Modulo, fmod(), try-except bocks,
# , (eg) x % y # print ("Remainder is:", r)
# (syntax)=> -5 % 3 = (1-2*3) % 3 = 1 : 5 % -3 = (-1*-2*-3) % 3 = -1

#    (eg) numpy.remainder() function can be used in List or Array,

# sample code = $
import numpy as np

arr1 = np.array([7, -6, 9])
arr2 = np.array([3, 4, 3])
rem_arr = np.remainder(arr1, arr2)
print("Dividend array is: ", arr1)
print("Divisor array is: ", arr2)
print("Remainder array is : ", rem_arr)
# $$ Output: /usr/bin/python3.9 /home/abith/Documents/work.py
# """ Dividend array is:  [ 7 -6  9]
# Divisor array is:  [3 4 3]
# Remainder array is :  [1 2 0]
# Process finished with exit code 0
"""
"""
#        BitWise   Operator   = operate on Binary Numbers                                                                          BitWise   Operator
# Bitwise Operators : & = and, | = or, ~x = not, ^ = xor, x>> = Right Shift, x<< = Left Shift
# Bitwise Assignment Operators : &= = and, |= = or, ^= = xor, >>= = Right Shift, <<= = Left Shift,

# Operator Precedence and Associativity : Determines the Priorities of Operation to proceed first
#  Operator Precedence = name = "Alex" $ age = 25 $ if name == "Alex" or name =="John" $ print("Hi!") $ else: $ print("TatA")
#  Operator Associativity used to Determine , Calculates or executes in left to right or right to left

a = 9
b = 65
print("Bitwise AND Operator On 9 and 65 is = ", a & b)
print("Bitwise OR Operator On 9 and 65 is = ", a | b)
print("Bitwise EXCLUSIVE OR Operator On 9 and 65 is = ", a ^ b)
print("Bitwise NOT Operator On 9 is = ", ~a)
print("Bitwise LEFT SHIFT Operator On 9 is = ", a << 1)
print("Bitwise RIGHT SHIFT Operator On 65 is = ", b >> 1)

# Modulus Operator : math.fmod(), -ve number, float, ZeroDivisionError, numpy,                                                       % Modulus
# math.fmod (eg) import math \ print(math.fmod(-5, 3))
a = 12.5
b = 0
try:
    print( f '{a} % {b} = {a % b}' )
    except ZeroDivisionErrr as zde:
        print("We cannot divide by 0")

#     NumPy modulus = import numpy as np
a = 10
b = 3
print(np.mod(a, b))
#    Numpy Array = import numpy as np
a = np.array([2, -4, 7])
b = np.array([2,3,4])
print(np.mod(a, b))

#                                                                                                                    """   Syntax Variable and DataTypes..."""

# a variable can be declared, store a value (temp) and can be Changed
# var = _ : var not= -
# boolean = only True or False , T,F in caps : No single or double quotes
# Exponenciation function and Modulo Operator = math operations , def function, return & print Exponential()
# String = Letter,Number,Symbols  can use string and integer within DOUBLE QUOTES ONLY Accessible
# Access by Index value - abith 12345 , 3 = i in a string
# String Method or Functions = Length , print-Lower,Upper
# String Formatting with %s and %
# for defining path use \ ... use / in program
# python GUI based app projects like hospital management sys using Tkinter - Library
# python Memory Stack Memory stored as: Variables ; Heap Memory stored as: Class & Objects
# Ram : Dynamic memory is Heap . eg(c=10+20) c= class or object
# Garbage Collector remove used or unwanted Objects to free some space & ending process
# code Structure : Source file->Compiler->Output : Library Modules for Virtual Machine->code+Lib
#
# Flow Control Statement = Python’s flow control statements are ‘while’, ‘for’ and ‘if’. For a switch, you need to use ‘if’. For enumerating through list members, use ‘for’. For obtaining a number list, use range (number).
rangelist = range(10)
print (rangelist)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in rangelist:
    if number in (3, 4, 7, 9):
        break
    else:
        continue
else:
    pass
if rangelist[1] == 2:
    print ("The second item (lists are 0-based) is 2")
elif rangelist[1] == 3:
    print ("The second item (lists are 0-based) is 3")
else:
    print ("Dunno")
while rangelist[1] == 1:
    pass
#                                                                                                                               $  Variable Scope
# Local Variables = Reached only within the defined scope 
def fun():
s = "This is a local variable"
print(s)
fun()
#  enclosed Variables = not local & Global
#                               Global Variables
def fun():
s = "local variable"
print (s)
s = "this is global scope"
fun()
print (s)
#     built-in Variables = loaded in startup
#                                                                                                                        dataTypes : 8 Types (no Declaration)
# Integer,Float, c = String,Boolean = True or False,List,Tuples,Set,Dictionaries
# to check Data-Type for (a=10)-->type(a)=class'int'
# List = [1,2,3] , tupple = (1,2,3) ;
# Set = (1,2,3) , dict = (1:2,2:3,3:4)

# Types of data
'''Numbers - int, float, Complex
Boolean
Sequences - Strings, Lists, Tuples
Sets
Dictionary - Mappings
'''
# Mutable DataType = List,Dictionary, Sets
# imMutable DataType = Numbers, Tuples, Strings

#                                                                                                                             Variable   Conditions

lst1 = [1, 2, 3]
lst2 = [3, 4, 5]
print([x * y for x in lst1 for y in lst2] [3, 4, 5, 6, 8, 10, 9, 12, 15])
print ([x for x in lst1 if 4 > x > 1] [2, 3]) # Check if a condition is true for any items.
# # "any" returns true if any item in the list is true.
any([i % 3 for i in [3, 3, 4, 4, 3]])
True
# # This is because 4 % 3 = 1, and 1 is true, so any()
# # returns True.
# # Check for how many items a condition is true.
# >>> sum(1 for i in [3, 3, 4, 4, 3] if i == 4)
# 2
# >>> del lst1[0] >>> print lst1
# [2, 3] >>> del lst1
#
#                                                                                                                           Global variables
number = 5
def myfunc():
    print (number)
# def another-func():
# # This raises an exception because the variable has not
# # been bound before printing. Python knows that it an
# # object will be bound to it later and creates a new, local
# # object instead of accessing the global one.
print number:
number = 3
def furtherance():
global number
#                  # This will correctly change the global.
number = 3

#                                                                                                                                     S Array's & NuMpy
#                                                               Array functions
# parameter + data type
# Index, Element, len(), append(), remove()
# array(datatype, value list()
# array(pos, value) => a.insert(2, 9) => insert 9 in 3rd place
array.append(value)
a.remove(value)
a.extend(arr) => add values in last
ar.pop(4) = remove an element
ar.index(value) => position of the index value
a.reverse()
arr.fromlist(list) => to add list to array
a.count(value) => number of occurrence of given value  

#                                                                                                                                     $ string Array
# capacity of a variable to contain more than one string value same time.
# Lists, negative indexing, accession by index, looping, appending, len(), removing => pop(), clear(), copy(), sort()
# looping => for x in Lists:
# append => list.append("elements to add")
# list.sort() <=> list.sort(reverse=True)
# range of index = print(list[1:4])
# change value of element = list[0]="element"
#                                                  check element exists or not, 
if "element" in list:
print(yes)
#                          $       list(()) = list constructor
newList = list(("1", "2", "3", "4"))
print(newList)

import array as arr
from array import *

array(typecode [,initializer])
for i in a
print a[i]

# TypeCode	PythonType	Value
#  i         int	    2
#  I         long	    2
#  b         int        1
#  B         int        1
#  h         int        2
#  H         int        2 
#  l         int        4
#  L         int        4
#  f         float      8
#  d         float      4
#                                                   Type $ code
import array as arr

a=arr.array('i', [10 , 20 ,30] )
print("Element at 0th index: " , a[0])
print("Element at 1st  index: " , a[1])
print("Element at 2nd index: " , a[2])
# array.typecode(), array.insert(index, element), Update=> arrayname[index] = value, array.remove(element), 
# array.append(element), array.reverse(), array.count(element), array.index(x), array.pop([ i ]), array.itemsize()
# len(array-name),
# pop() = removes and returns the element that has an index I


#                                                                                                                        $ Arrays = 2D, 3D, Multi-Dimensional
# 
# 
#                                                                                                                         $ searching 8 from array
for num in [1, 19, 8, 0, 9, 30, 29]:
    print(num)
#                                                        # # if number is 8 print message as found and break the loop
if(num==8):
    print("number 8 is found")
    break
in(break) = sum of 1st 5 integers
num = (1, 2, 3, 4, 5, 6, 7, 8, 9)
sum = 0
counter = 0
#                                                                      # # parsing the tuple
for i in num:
    sum = sum + i
    counter = counter + 1
    if counter == 5:
        break
    print("Sum of the first",counter)
    print("integers is: ",sum)
#                                                                          $   Array length
#                                         len( given_arr_name )
import array as arr1

print("Program to demonstrate array length using array module")
print("\n")
a=arr1.array('i', [1, 8, 4] )
print("The array created is as follows:")
print(a)
print("\n")
print("The length of the given array is as follows:")
print(len(a))
#                                                                                                           $ sorting Array
#                                                                                      $   bubble-Sorting
import array as arr

sample_array = arr.array('i',[4,2,5,9,1,8,6])
def bubble-sort(sample_array):
for j in range(len(sample_array)-1,0,-1):
for i in range(j):
if sample_array[i]> sample_array[i+1]:
temp = sample_array[i] sample_array[i] = sample_array[i+1] sample_array[i+1] = temp
bubble-sort(sample_array)
print(sample_array)
#                                                                                            selection-sort
import array as arr

sample_array = arr.array('i',[4,2,5,9,1,8,6])
def selection-sort(sample_array):
for i in range(len(sample_array)):
min_val = i
for j in range( i +1, len(sample_array)):
if sample_array[min_val] > sample_array[j]:
min_val = j
sample_array[i], sample_array[min_val] = sample_array[min_val], sample_array[i] sample_array = arr.array('i',[4,2,5,9,1,8,6])
selection-sort(sample_array)
print(sample_array)
#                                                                                              Insertion sorting
import array as arr

sample_array = arr.array('i',[4,2,5,9,1,8,6])
def insertion_sort(sample_array):
for i in range(1, len(sample_array)):
j = i-1
temp = sample_array[i] while (sample_array[j] > temp) and (j >= 0):
sample_array[j+1] = sample_array[j] j=j-1
sample_array[j+1] = temp
sample_array = arr.array('i',[4,2,5,9,1,8,6])
insertion_sort(sample_array )
print(sample_array )
# 


#                                                                                                                              Enumeration 
# if a value is given Indexing is taken from that value, if key and values are not in Dictionaries
# Enumeration is Looping a Multi-Dimensional Array, The list will have More than 1 column to be taken out
# # pets = ["cats", "dogs", "rabbits", "cow"]
# # for index, Looping-value in enumerate(pets)
# #  print(index, Looping-value)
#                                                                                                                             $   Sorting String
# sort only sameDataType (eg) int to int & string to string
# sorted() can be used in any List, Tuples, Dictionary
# iterable = Lists, Tuples, Sets, String, frozen set & Dictionary data Structures, 
# Reverse = descending order = True or False
# Tuples = () = immutable & not apply to index / print("Tuple = ", t) re=sorted(t)
# returnSecond() +> based on 2nd element of tuple
# (eg) def returnSecond( L ):
return L[1]
# list = [ ('a', 40), ('b', 30), ('c', 20), ('d', 10) ] / sorted list = sorted(list, key = returnSecond) / print(':', sortedList)
# sort (), list.sort(),fun= Ascending & Descending:  Reverse passing = True or False, tim-sort = merge & Time
# sort()=> list.sort(key = ..., reverse = ...)  $ help( lis.sort ) $ print("list = ", l) / l.sort()  .
# Sorting in Reverse arguments = print("list = ", l) / l.sort( reverse = True) / print("sorted list =", l) 
# default reverse value is False.
# sorted() +> $ print("sorted list =", l)
# functions are passed in key arguments , len() => used to pass the key argument
# sort based on length in ascending order using len()
# $ word = "hello"
length = len(word)
print( "the length of word is ", length)
l = [ "aaa", "bbbbba", "ccc", "d" ]
print("list = ", l)
print( "length of the list is ", len() )
l.sort( key = len )
print("sorted list = ", l)
l.sort(key = len, reverse = True)
print("sorted list with reverse = ", l)
sort based on 2nd character =  def / sort_onSecondChar(word): / return word[1] l.sort(key = sort_onSecondChar) /
print("sorted list based on second character = ", l) = returns new sorted list.
# Sorted fun with reverse parameter = 
print("List = ", l)re=sorted(l,reverse=True )
# Sorted fun with key parameters = 
print("List = ", l)re=sorted(l, key = len)
# sorting list of tuple with lambda => sortedList = sorted(list, key = lambda x : x[1]) 
print( "sorted list = ", sortedList ) --> altering the lambda function
sortedlist = sorted(students, key=lambda stud :
stud[2]) 
print("name","marks") / for x in stored list: / print(x[0],x[1])

# 
print (sorted(List))
print ("\nSorted list with Reverse sort by setting reverse keyword to True:",)
print (sorted(List, reverse = True) )
print ("\nOriginal list without any modifications :",)
print (List)
print (sorted(Set))
print (sorted(Dict))
print (sorted(str))
print (sorted(Tuple))
#                                                                                                                          Sorting string
# Syntax of python sort string sorted() method:
#                                    $ sorted(iterable, key = key, reverse = reverse)
"""                       Parameters: Iterable, Key, reverse = reverse
iterable: This is not an optional parameter, it is a sequence of string to be sort.
"""
#                                                                               python built in                                   sorted() method.
#
#                                            Code:
#                                # creating string
msg = "Hello!, how are you"
print("The original message is : ")
print(msg)
#                                                              # using sorted() method to get list of sorted characters
alt_msg = sorted(msg)
print( "The output of the sorted() method is :  " )
print( alt_msg )
#                                                                # using join() method to join list of sorted characters           join()
sort_msg = "".join(alt_msg)
print( "The sorted message is :  " )
print( sort_msg )

# sorting the string                                                                                                         sort using while loop
#                                   $ Code:
string = "Sample string to sort alphabetical order."
print( "The original string is : " )
print( string )
#                                          # using sorted() method to get list of sorted characters with ascending order
list_string=list( string )
print( "The list of string is : " )
print( list_string )
list_string = list(string)
i = 0
while i < len( list_string ):
    key = i
    j = i+1
    while j < len( list_string ):
    if list_string[key] > list_string[j]:
        key = j
        j += 1
list_string[i],list_string[key] = list_string[key],list_string[i] i += 1
print( "The list of sorted string is : " )
print( list_string )
new_string = "".join(list_string )
print( "The sorted string is : " )
print(new_string)
# using for loop in python which is also a implementation of bubble sort.                                                           Using for Loop
#                       $   Code:
#                           # creating string
string = "This is a sample string"
new_string = [] print( "The original string is : " )
print( string )
# # woith out using sorted() method to get list of sorted characters
list_string=list(string)
print( "The list of string is : " )
print(list_string)
list_string=list(string)
len_s=len(list_string)
for i in range(len_s-1):
for j in range(len_s-i-1):
    if list_string[j]>list_string[j+1]:
        list_string[j],list_string[j+1]=list_string[j+1],list_string[j]
        for m in list_string:
            new_string+=m
            print( "The list of sorted string is : " )
            print(new_string)
sort_string = "".join(new_string)
print( "The sorted string is : " )
print(sort_string)

#                                                                            Compare Strings
str1 = 'kaashiv'
str2 = 'kaashiv'
if str1 == str2:
    print("Strings are same")
else:
    print("Strings are different")

a = 2
b = 1
c = 2
if a is c:
    print("Same")
else:
    print("Different")
#                            (!=) operator
str1 = 'kaashiv'
str2 = 'kaashiv'
if str1 != str2:
    print("Strings are different")
else:
    print("Strings are same")
#                                    Greater than (>) and lesser than (<)
string_variable1 > string_variable2
string_variable1 < string_variable2
str1 = 'kaashiv training'
str2 = 'kaashiv'
if str1 > str2:
    print("True")
else:
    print("False")
#                          Greater than or equal to ( >=) operator
str1 = 'kaashiv training'
str2 = 'kaashiv '
if str1 >= str2:
    print("True")
else:
    print("False")
#                    less than or equal to (<=)
str1 = 'kaashiv '
str2 = 'kaashiv '
if str1 <= str2:
    print("True")
else:
    print("False")
#                                                                                                                                   Sorting Algorithms - Top 6 = Bubble Sort, Selection Sort, Insertion Sort, Merge Sort, Heap Sort, Radix Sort
#                                                                                                                                     Bubble sorting
# Sorting data in effortless, rational, recurring Exchange in Queue Structure, Low-Efficiency
# Whenever variables are swapped, a flag could be maintained to determine the sorting process’s re-execution. The flag should be set to false when no other swaps are needed.
# $ def bubble_Sort(array):
# length = len(array)
#                                                               # loop through each and every element which are keyed
# for iterator_1 in range(length):
# #loop through next element
# for iterator_2 in range(0, length-iterator_1-1):
#                                                     # From 0 to n-i-1 the array value needs to be looped upon
#                              # when an element greater than the next element then the collected element needs to be swapped.
if array[iterator_2] > array[iterator_2 + 1] :
    array[iterator_2], array[iterator_2 + 1] = array[iterator_2 + 1], array[iterator_2] # Driver code to test above
    array = [75,34,54,56,78,1] bubble_Sort(array)
    print ("Array values after sorting:")
for i in range(len(array)):
    print ("%d" %array[i])
#                                              First Run
# (6 1 4 3)  -> (1 6 4 2): Here 1st two elements get swapped if the order is not correct.
# (1 6 4 2)  -> (1 4 6 2): Here, the next two elements get swapped if the order is not correct. 
# (1 4 6 2) -> (1 4 2 6): Here, the next two elements get swapped if the order is not correct.
#                                                 Second Run
# (1 4 2 6)-> (1 4 2 6): Here 1st two elements get compared but didn’t swap as the order is correct.
# (1 4 2 6)-> (1 2 4 6): Here, the next two elements get swapped, as the order was not correct.
# (1 2  4  6) -> (1 2 4 6): Here last two elements get compared but didn’t swap as the order is
# Now we know the array looks sorted; however, one run is required without any swap to the algorithm to know if sorting is done.
#                                                    Third Run
# (1 2 4 6)  -> (1 2 4 6)  : No swap in1st two elements.
# (1 2 4 6) -> (1 2 4 6): No swap in next two elements.
# (1 2  4  6) -> (1 2 4 6) : No swap in last two elements.
#                                                                                                                $  Bubble sort
# def bubble_Sort(arr):
# m = len(arr)
#                                                                 # Traverse through all the array elements
for u in range(m):
for v in range(0, m-u-1):
#                                                                # traverse the array from 0 to m-u-1
#                                                       # Swap if the element is greater than adjacent next one
if arr[v] > arr[v+1] :
arr[v], arr[v+1] = arr[v+1], arr[v]
#  #                                                  # To print array after bubble sort, you need to follow code:
for i in range(len(arr)):
print("%d" %arr[i]),
#                                                      # here arr will be your array.
#                                                                                                      $ Code Format
for i in range(len(arr)):
print ("%d" %arr[i]),
#                                                                                                                   Selection Sort
# Finding min or least value & positioning from unsorted sets, unsorted sublist is the complete key list
import sys

Array = [63, 75, 13, 2, 441] # loop through each and every element in the array
for element1 in range(len(Array)):
 # To determine the least element in the remaining list
minimum_idx = element1
for element2 in range(element1+1, len(Array)):
if Array[minimum_idx] > Array[element2]:
min_idx = element2
# # swap the determined least element with the  previous element in the list
Array[element1], Array[minimum_idx] = Array[minimum_idx], Array[element1] # main code
print ("Array after getting sorted by selection sort")
for i in range(len(Array)):
print("%d" %Array[i])

#                                                                                                        Insertion Sorting
# Compared in a sequential order and then rearranged in one specific order, similar to arranging cards
# $ def insertion_Sort(array):
# # pass through 1 to len(array)
for temp_element1 in range(1, len(array)):
key = array[temp_element1] # Move elements of array[0..i-1], that are
# # greater than key, to one position ahead
# # of their current position
temp_element2 = temp_element1 -1
while temp_element2 >= 0 and key < array[temp_element2] :
    array[temp_element2 + 1] = array[temp_element2] temp_element2 -= 1
    array[temp_element2 + 1] = key
 # Driver code to test above
array = [75,34,54,56,78,1] insertion_Sort(array)
for i in range(len(array)):
    print ("% d" % array[i])

#                                                                                                                                      Merge Sort
# Divide & conquer Algorithm, input is sliced in 2 half , merge sorting in 1st & 2nd half then merged
#                                                                      recursive approach of implementing the merge sort
#                                                                                   Code:
def mergeSort(ar_list):
if len(ar_list) > 1:
mid = len(ar_list) // 2
left = ar_list[:mid] right = ar_list[mid:] # Recursive call on each half
mergeSort(left)
mergeSort(right)
# Two iterators for traversing the left and right half
i = 0
j = 0
# Iterator for the main list
k = 0
while i < len(left) and j < len(right):
if left[i] < right[j]:
# The value from the left half has been used
ar_list[k] = left[i] # Move the iterator forward
i += 1
else:
ar_list[k] = right[j] j += 1
k += 1
#                                  # For all the remaining values
while i < len(left):
    ar_list[k] = left[i] i += 1
    k += 1
while j < len(right):
    ar_list[k]=right[j] j += 1
    k += 1
    ar_list = [12, 7, 2, 9, 4, 15, 5] mergeSort(ar_list)
    print(ar_list)

#                                                                Bottom-up approach implementation of merge sort
def merge(left, right):
result = [] x, y = 0, 0
for k in range(0, len(left) + len(right)):
if x == len(left): # if at the end of 1st half,
    result.append(right[y]) # add all values of 2nd half
    y += 1
elif y == len(right): # if at the end of 2nd half,
    result.append(left[x]) # add all values of 1st half
    x += 1
elif right[y] < left[x]:
    result.append(right[y])
    y += 1
else:
    result.append(left[x])
    x += 1
    return result
def mergesort(ar_list):
    length = len(ar_list)
    size = 1
while size < length:
    size+=size # initializes at 2 as described
    for pos in range(0, length, size):
        start = pos
        mid  = pos + int(size / 2)
        end = pos + size
        left = ar_list[ start : mid ] right = ar_list[ mid : end ] ar_list[start:end] = merge(left, right)
        return ar_list
        ar_list = [33, 42, 9, 37, 8, 47, 5] print(mergesort(ar_list))

#                                                                        Sample()
# $ def mergeSort(array):
# if len(array) >1:
# mid = len(array)//2 #determining the mid of the array
# divide = array[:mid] # Dividing the array elements
# split = array[mid:] # splitting the array into 2 halves
# merge_Sort(divide) # first half of the sorting
# merge_Sort(split) # second half of the sorting
i = j = k = 0
#                            # Copy data to temp arrayays divide[] and split[] while i < len(divide) and j < len(split):
if divide[i] < split[j]:
    array[k] = divide[i] i+=1
else:
    array[k] = split[j] j+=1
    k+=1
#                                              # Checking if any element was left
while i < len(divide):
    array[k] = divide[i] i+=1
    k+=1
while j < len(split):
    array[k] = split[j] j+=1
    k+=1
#                                              # Code to print the list
def print divide ist(array):
    for i in range(len(array)):
        print(array[i],end=" ")
        print()
# # driver code to test the above code
if __name__ == '__main__':
    array = [12, 2, 93, 65, 76, 27] print ("Given array is", end="\n")
    print divide-list(array)
merge_Sort(array)
print("Sorted array is: ", end="\n")
print-individualistic(array)

#                                                                                                                                Heap Sort

# count(), len(), max(), range(). perform_heapsort = 3 args = var_array, count, num: var_array = Holds the values
# process = Max_Value from a list is Encountered and shifted to the last of array (recursive process)
# largest value in array will moveto the last of the array while sortig
# Sample Code
"""
"""
def perform_heapsort(val_arr, num, count):
    int = 100
counter1 = 2 * 100 + 1
counter2 = 2 * 100 + 2
if counter1 < num and val-arr[100] < val-arr[counter1]:
    max_val = counter1
if counter2 < num and val-arr[max_val] < val-arr[counter2]:
    max_val = counter2
if max_val != 100:
    val-arr[100]
    val-arr, [max_val] = val-arr[max-val],val-arr[100], perform_heapsort(val-arr, num, max_val)
    def heapSort(val_arr):
        NUM = len(val_arr)
        for COUNT in range(NUM, -1, -1):
            perform_heapsort(val_arr, NUM, COUNT)
            for COUNT in range(NUM - 1, 0, -1):
                val_arr[COUNT], val_arr[0] = val_arr[0], val_arr[COUNT]                                       # swap
                perform_heapsort(val_arr, COUNT, 0)
                val_arr = [ 52, 91, 64, 252, 36, 91, 5, 35, 28] heapSort(val_arr)
                (NUM) = len(val_arr)
print ("Values after performing heapsort")
for count in range(num):
    print ("%d" %val-arr[count]),

# like selection sorting, segregates the input as sorted & non-Sorted elements,  the algorithm loops in such a manner on the non sorted region so that on each loop, the largest value will be pushed into the sorted region. This process will be continued across all the elements in the unsorted region.
# A max heap is created from the given input list. The last value is then swapped with the first value repeatedly, and also, the value range is comparatively decreased by one. This process takes place until the range shrinks to 1.
def heap_sort(Ordering, number, i):
largest = i # Initialize largest as root
left= 2 * i + 1     # left = 2*i + 1
right= 2 * i + 2     # right = 2*i + 2
#                                                            # to verify the left child of root is greater than the root
if left< number and Ordering[i] < Ordering[left]:
    largest = left
# to verify the right child of root is greaterightthan the root
if right < number  and Ordering[largest] < Ordering[right]:
    largest = right
# # swap roots on necessity
if largest != i:
    Ordering[i],Ordering[largest] = Ordering[largest],Ordering[i] # swap
# # Heapify the root.
heap_sort(Ordering, number, largest)
# main function for Ordering sorting
def heapSort(Ordering):
    number = len(Ordering)
# max heap build process.
for i in range(number, -1, -1):
    heap_sort(Ordering, number, i)
# extract of all the elements in the given heap
for i in range(number-1, 0, -1):
    Ordering[i], Ordering[0] = Ordering[0], Ordering[i] # swap
    heap_sort(Ordering, i, 0)
# # main section of the code
Ordering = [ 12, 11, 13, 5, 6, 7 ,56 ,45 ,67 ,78 ,34 ,4 ,33] heapSort(Ordering)
number = len(Ordering)
print ( "Sorted Ordering value is" )
for i in range( number):
    print ( " %d " %Ordering[i])

#                                                                                                                                Radix Sort

# no comparing the keyed elements, This is achieved by means of generating a bucket according to the radix value for elements with more than one digit involved; the technique is applied for all the digits in the element. It is also termed as bucket sort. This sorting technique tends to be too quick in their suitable environments.
def radix_sort(The_list, base=10):
    if The_list == []:
        return
def Input_factory(numeral, base):
def Input(The_list, index):
    return ((The_list[index]//(base**numeral)) % base)
    return Input
    greatest = max(The_list)
    exponent = 0
while base**exponent <= greatest:
    The_list = sort_count(The_list, base - 1, Input_factory(exponent, base))
    exponent = exponent + 1
    return The_list
def sort_count(The_list, greatest, Input):
    count = [0]*(greatest + 1)
    for i in range(len(The_list)):
        count[Input(The_list, i)] = count[Input(The_list, i)] + 1
        # to determine the last index for each of the element
        count[0] = count[0] - 1
# zero-based indexing decrement
for i in range(1, greatest + 1):
    count[i] = count[i] + count[i - 1] output_value = [None]*len(The_list)
for i in range(len(The_list) - 1, -1, -1):
    output_value[count[Input(The_list, i)]] = The_list[i] count[Input(The_list, i)] = count[Input(The_list, i)] - 1
    return output_value
The_list = input('Enter the list of (non-negative) numbers: ').split()
The_list = [int(x) for x in The_list] sorted_list = radix_sort(The_list)
print( ' Radix oriented sorted output :  ' , end='')
print(sorted_list)
#

# $ Python -m pdb program.py Run a program in                                                                                            Debug Mode

# create empty numpy Array = (1) $ import numpy (next Line) numpy.array([])
# (2) $ numpy.empty(shade=(0,0))

# Copying Objects : (1) Shallow Clone = 2 objects in same address
#  (eg) fruits=["apples","banana","orange"]
x=fruits.copy()
print(x)
#
# (2) Deep Clone = Separate Address for each Object
x=fruits.deepcopy()

# Built-in Types : Mutable = Numbers,string,tuples : UnMutable = List,Dictionaries,Sets
# characteristics of a Class= template or blueprint
# Object = For accessing all class print(X.X) (i.e) X is the class and declared Object ID (eg) (X=Child class())
# Overload Constructor __init__
#                                                                                           Conditional Statements
#                              if condition True or False
savingAmt = 1000
withdrawAmt = int(input("Amount to Withdraw: "))
if withdrawAmt > savingAmt:
    print ("Insufficient balance")
else:
    savingAmt = savingAmt - withdrawAmt
    print("Account Balance:" + str(savingAmt))
#                               if, elif and else
time = 619
if (time >= 600) and (time < 1200):
    print("Morning")
elif (time == 1200):
    print("Noon")
elif (time > 1200) and (time <= 1700):
    print("Afternoon")
elif (time > 1700) and (time <= 2000):
    print("Evening")
elif ((time > 2000) and (time < 2400)) or ((time >= 0) and (time < 600)):
	print("Night")
else:
	print("Invalid time!")
#                                                              Nesting if-else statements
# writing if-else statements inside another if-else statements
if (time >= 600) and (time < 1200):
	print ("Morning")
else:
	if (time == 1200):
		print ("Noon")
	else:
		if (time > 1200) and (time <= 1700):
			print ("Afternoon")
		else:
			if (time > 1700) and (time <= 2000):
				print ("Evening")
			else:
				if ((time > 2000) and (time < 2400)) or ((time >= 0) and (time < 600)):
					print ("Night")
				else:
					print ("Invalid time!")
savingAmt = savingAmt - withdrawAmt if (savingAmt > withdrawAmt) else savingAmt
#                                              Syntax                                                                             if Statement
# if-statement : if, if-else, elif, Switch Statement, Nested-if. ==, =, !=, <, <=, >, >= if = Yes or No
# if p > r or q > r: / print
# if-else = if / print / else / print
#                                                   Sample
a = 619
if [a > 618]:
    print("initial if")
#                                                                                                             ELIF
#                                                                                                             => in end of statement:, ... / ... else-if code block
# Nested if = target of previous if statement. use :, []
check_variable = 619
if (check_variable == 219):
    print("Wrong Checking next val in elif")
elif (check_variable == 419):
    print("The Value is Incorrect")
elif (check_variable == 619):
    print("Hi Abith")
#                                                                                                           if-else
a = 10
b = 20
if a > b:
    print("a is greater than b")
else:
    print("b is greater than a")
#                                                                                                                                        LOOP
#                                                                                                parsing
# $ Below example is a use-case of finding first leap year from 2000 to 2005
# # parsing through the year from 2000 to 2005
for year in range(2000,2005):
# checking whether the year is leap year or not
if year%4==0 and year%100!=0:
    print("year is first leap year" ,year)
    break
#                                       print all prime numbers between 0 and 20.
for n in range(0, 20):
# # Since all the  prime numbers are always greater than 1
if n> 1:
for i in range(2, n):
if (n % i) == 0:
    break
else:
    print(n)
#                                                                                                                              While Loop
# While Loop = increment operator i=i+1 / print("Loop Completed") : import math to get float value to a number
#            executes group of statements until it is fulfilled
# """ import math  /     remainder=i%10
# i=143            /     sum=sum+remainder
# sum=0            /     i=math.floor(i/10)
# while i>0:       /     print(sum)       /    (Loop Completed)
#
I=1
While(1):
Print “We are in the loop”
If(i>10):
print ”Here break statement works”
break
I=i+1
print I
print “I am out of the loop”
#                                        search 9 using while loop
i = 0;
# While condition
while 1:
    print(i)
    i=i+1;
if i == 9:
    # break if 9 is found
    break;
    print("out of loop");
#
#               $       print the variable from 2 to 5 and decremented by 2
counter = 5
While counter >=2:
print("counter =", counter)
counter = counter -2
#                                             sum of 1st 5 integers
sum = 0
counter = 0
while(counter<10):
    sum = sum + counter
    counter = counter + 1
if counter == 5:
    break
print("Sum of the first ",counter)
print("integers is: ", sum)
#                                                                                                                             While  Decrement
counter = 0
while(counter<=10):
    print ("counter = "counter)
    counter = Counter -2
#                                                                                                               sorting the string using while loop in python.
#                                                Code:
#                                                      creating string
string = "Sample string to sort alphabetical order."
print( "The original string is : " )
print( string )
# using sorted() method to get list of sorted characters with ascending order
list_string=list( string )
print( "The list of string is : " )
print( list_string )
list_string = list(string)
i = 0
while i < len( list_string ):
    key = i
j = i+1
while j < len( list_string ):
    if list_string[key] > list_string[j]:
key = j
j += 1
list_string[i],list_string[key] = list.str[key],list.str[i], i += 1
print( "The list of sorted string is : " )
print( list_string )
new_string = "".join(list_string )
print( "The sorted string is : " )
print(new_string)
import random
#                                                                                                         do-While
# do
# {
# Statement(s)
# } while (condition);
#                                                                                                          while if
# while True:
# # statement (s)
# If not condition:
# break;
#                                                                                                                           Matching a string
import string
import time

#                                                                                 Variable section
# endeavourNext = ''
# completed = False
# iterator = 0
#                                                                          Propable Characters to Compare
# propableCharacter.s = string.ascii_lowercase + string.digits + string.ascii_uppercase + ' ., !?;:'
#                                                                             String to Be Generated
# t = input("Enter the expected string or word : ")
#                                                                        Generate the Initial Random String
# endeavourThis = ''.join(random.choice(propableCharacters)
# for i in range(len(t)))
#                                                                           Iterate While Completed Is False
while completed == False:
    print(endeavourThis)
    endeavourNext = ''
    completed = True
for i in range(len(t)):
if endeavourThis[i] != t[i]:
    completed = False
    endeavourNext += random.choice(propableCharacters)
else:
    endeavourNext += t[i]
    #                                                                         Increment the iterator += 1
endeavourThis = endeavourNext
time.sleep(0.1)
#                                                                          Driver Code
print("Target match found after " +
str(iterator) + " iterators")
#                                                                                                                                 ForLoop
# traverse or iterate over a sequence (list, tuple, string) or other iterable objects.
#  for Accessing index / $ a=[10,20,30,40,50] / for i in range(0,len(a),1): / print(i)
# for Accessing element using range: a=[10,20,30,40,50] \ for i in range(0,len(a),1): \ print(a[i])
#  for LOOP = break, continue                 : for / if / break / else / print():
# Nested for Loop = for loop inside a for Loop : range(,): , List = L = print[]
# for i in L: / print(i,end=" ,. ") , Char, int, float
"""for i in range(1,11): / for(j in range(1,3)):
print(i)                   print(j)              """
#
a=[ ‘A’,’B’,’C’,’D’,’E’,’F’,’G’,’H’] for I in a:
print “We are in loop with”
print i
if i==’G’:
    print ”Here Break statement is triggered”
    break
print ”We are outside the loop”
#                                                                                                                        Iterating on String (Loop through it)
print("\nString Iteration")
string1 = "hello"
for i in string1 :
    print(i)
#                                                                          $ Iterating Looping fetching values from list
pets = ["cats", "dogs", "rabbits", "cow"]
for Looping-value in pets:
    print (Looping-value)
#                                                                                                                                 Enumeration
# Enumeration is Looping a Multi-Dimensional Array, The list will have More than 1 column to be taken out
pets = ["cats", "dogs", "rabbits", "cow"]
for index, Looping-value in enumerate(pets)
print(index, Looping-value)
#                                                                                                                          Turtle Graphing Technique
# Function eg
import turtle


def border(obj1, panel_x, panel_y):
    obj1.penup()
    obj1.home()
    obj1.forward(panel_x / 2)
    obj1.right(90)
    obj1.forward(panel_y / 2)
    obj1.setheading(180)
    obj1.pencolor('red')
    obj1.pendown()
    obj1.pensize(10)
for distance in (panel_x, panel_y, panel_x, panel_y):
    obj1.forward(distance)
    obj1.right(90)
    obj1.penup()
    obj1.home()
def square(obj1, size, color):
    obj1.pencolor(color)
    obj1.pendown()
for i in range(4):
    obj1.forward(size)
    obj1.right(90)
def main():
    panel = turtle.Screen()
    panel.title('Square Demo')
    panel_x, panel_y = panel.screensize()
    obj1 = turtle.Turtle()
    border(obj1, panel_x, panel_y)
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'violet'] obj1.pensize(3)
for i, color in enumerate(colors):
    square(obj1, (panel_y / 2) / 10 * (i+1), color)
    print('Hit any key to exit')
    dummy = input()
#                                                                                            Main Program Call
# if __name__ == '__main__':
# main()
#                                                                                                                               Enumeration
myDictionary = {"peter":38, },
myDictionary = {"key1 :value1 , key2:value2, key3:value3}
print ( myDictionary["peter"])
myDictionary = dict{ "peter":38, "":51 )
print ( mydictionary, ["peter"])
# range(start, end, step) = values from start value to end values  $                                                                 Range
#                                                                Sorting the string using for loop in python which is also a implementation of bubble sort.
#                                                          creating string
string = "This is a sample string"
new_string = []
print( "The original string is : " )
print( string )
#                                                           without using sorted() method to get list of sorted characters
list_string=list(string)
print( "The list of string is : " )
print(list_string)
list_string=list(string)
len_s=len(list_string)
for i in range(len_s-1):
    for j in range(len_s-i-1):
if list_string[j]>list_string[j+1]:
    list_string[j],list_string[j+1]=list-str[j+1],list-str[j]
    for m in list_string, new_string= += m
print( "The list of sorted string is : " )
print(new_string)
sort_string = "".join(new_string)
print( "The sorted string is : " )
print(sort_string)
#                                                                                                                      concatenate two LISTS into a dictionary
#                                                                            Variable declaration
# Key_elements=[] value_elements=[]
#                                                                                     Count to be processed
# var1=int(input("Count of elements for the dictionry:"))
#                                                                                  print (Key Elements)
for x in range(0,var1):
    element=int(input("Element item entered" + str(x+1) + ":"))
    Key_elements.append(element)
#                                                                                Print (Value Elements)
for x in range(0,var1):
    element=int(input("Element item entered" + str(x+1) + ":"))
    value_elements.append(element)
    d=dict(zip(Key_elements,value_elements))
#Print Section
print("The formulated dictionary is:")
print(d)
#                                                                                                                               Infinite Loops
# A loop becomes infinite loop if the condition given never becomes false. It keeps on running
a = 1
while(a == 1)
n=int(input("enter the number"))
print("you entered:" , n)
#                                                                                                                                Nested loops
for iterating_variable#1 in sequence#1:
for iterating_variable#2 in sequence#2:
    statements(s)
    statements(s)
while expression#1:
    while expression#2:
        statement(s)
        statement(s)
#                                                                                                                               Switch Statement
# Switch Statement = while LOOP = while condition statisfy do the process : Continue Loop
# if-else-if ladder statement = > Switch-case => not an inbuilt function
# if-else-if = def get_week_day(argument): / if (argument == 0): / day="Sunday" / elif(argument == 1): day="Monday" /
# else: / day="Invalid Day" / return day / if __name__ == "__main__": / print(get_week_day(6))
# call get() fun of dictionary (input key & default Value)
# get() to access the item of the dictionary by passing the arguments as keys & optional default value
# <dictionary-name>.get(<key-argument>, <default value[optional]>) /
# switcher.get(argument, "Invalid day")
# switcher = dictionary variable ,
#
# switcher=                    / key_n: value_n/method_n(),
# {                            / }
# key_1: value_1/method_1(),   / key = N
# key_2: value_2/method_2(),   / value = switcher.get(key, "default")
# key_3: value_3/method_3(),
# ::
#
def get_week_day(argument) : #          (argument=day)
    switcher = {
        0: "Sunday",
        1: "monday",
        }
        return switcher.get(argument, "Invalid Day")
if __name__ == "__main__":
    print(get_week_day(0))
    print(get_week_day(1))


#                                                                                                                        Break statement in the Nested Loop

num = [1, 2, 3] # Array of Character
str = ['y' ,'x', 'z'] # outer loop
for i in num:
    print("Number of items: " ,i)
# inner loop
for j in str:
if j == 'z':
    break
print(" String of items: " ,j)

# """                                                                  Loop control statements =                          break, Continue, Pass
# """
# Break Statement = for LOOP = Continues : it comes out of the program when it matches (i==""a)
# for i in ""Abith: / if(i=="t"): / break / else: / print(i) O/P = A / b / i
#
# $ (eg)                                                                  Loop Control Code (eg)
var_a = 1
var_b = 2
while var_a < var_b:
    print(" Code enters while loop ")
var_c = ["SUV","sedan","hatchback","End"] for iterator in var_c:
if iterator == "SUV":
    print("Hyundai creata")
    print("Mahindra bolero")
    print("---------------")
if iterator == "sedan":
    #                                                                                                                           Loop Control Statement: Pass
    pass
if iterator =="hatchback":
    print("Renault Kwid")
    print("suzuki alto")
    print("---------------")
if iterator == "End":
    #                                                                                                                         Loop Control Statement: Break
    break
var_a = var_a+1
#                                                                                                                               Continues Loop

# Continues Loop = for / if / continue / else / print() :
# for i in ""Abith: / if(i=="t"): / continue / else: / print(i) O/P = A / b / i / h
#  (i=='a')        i is missed or rejected and continues with other unmatched
#  Continue = skip the execution of remainder
# Pass = terminate, divert the flow of loops in a program , break statement to exit the loop, while used in inner loop the flow of execution if diverted to the next statement in outer loop
# def prod():/ for in range(10) ; / for j in range(): / print i*j / if i*j>50 / return = break function
#                                              to use without calling function :
for in range(10);
for j in range(10):
    print i*j
if i*j>50:
    break
else:
    continue                                     # this will be executed if the loop ended normally (no break)
break                               # this will be executed if 'continue' was skipped (break)                               Break
#  if the product of two numbers is > 50 then break if true,
#
a=[‘a’,’b’,’1’] for I in a;
if (i.is_numeric()):
    break
print a
print ‘Found a number in the list’
#
#                                            # Prints out
0,1,2,3,4 count = 0
while True:
    print(count)
    count += 1 if
    count >= 5:
    break
#                                                                                                                                  $ Continue
#                                 # Prints out only odd numbers - 1,3,5,7,9
for x in range(10):
#                                 # Check if x is even
if x % 2 == 0:
    continue

#                                                                                                                          Exception & ErroR Handling

# use try and except blocks
# try = pass error code : except = catches the exception and executes the specified statements
# try block = try:
# except block = except(): => Continue execution, Multiple exceptions in one block,
# except(ValueError, ZeroDivisionError): / print("")
# Generic except block = Unknown exceptions: except: / print("")
# import random / from time import clock / random-int = random.randint(1, 100) / print random-int
#                                                                  Try-exception-else
# pointing & controlling an error, by raising value error
except ValueError as err
print(err)
#                                     Try-if-raise-else-except-valueError
try:
    age = int(input("Enter the fuckin Age :"))
    if(age<18):
        raise ValueError
    else:
        print("the age is valid")
except ValueError:
    print("it's not an valid input")
#                                     try:if:raise:else:except:ArithmeticError
try:

    if b is 0:
        raise ArithmeticError
    else:
        print("a/b = ",a/b)
except ArithmeticError:
    print("the value of b cannot be 0")
#                                                                                                              Exception-handling
def some_function():
    try:
        10 / 0
    except ZeroDivisionError:
        print("Oops, invalid.")
        else:
            pass
        print("We're done with that.")
# custom exception
class User_Exception1( Exception ):
class User_Exception2( Exception ):
    try:                 # Executed on top of suspicious code
        except User_Exception1:
            except User_Exception2:
                else:
#   This piece will be executed when a user_exception 1 is triggeredexcept User_Exception2:   This piece will be executed when a user_exception 1 is triggered else:
#                                                                      raise
a = 10
b = 9
try:
    # condition for checking for negative values
    if a < 0 or b < 0:
        # raising exception using raise keyword
        raise ZeroDivisionError
    print(a/b)
except ZeroDivisionError:
    print("Please enter valid integer value")
# raise Without Specifying Exception Class
a = 10
b = 0
try:
    print(a/b)
except ZeroDivisionError:
    raise
#                                       raise With an Argument
raise ValueError("Incorrect Value")
#                                                                                  Indentation Error
#  PEP8 whitespace ethics, 4 whitespaces used between any alternative or iteration
for i in range(1,24):
    print(i)
    if i == 8:
        break
#                             Example
site = 'kaashivv'
if site == 'kaashiv':
print('Logging in to kaashiv!')
else:
print('Please type the URL again.')
print('You are ready to go!')
#                             Example
j = 1
while(j<= 5):
    print(j)
    j = j + 1
#                                                                             I/O Error
#  to write program in a way that it can catch the expected errors
import sys

file = open('myfile.txt')
lines = file.readline()
slines = int(lines.strip())
# FileNotFoundError: [Errno 2] No such file or directory: 'myfile.txt'
#                                           using try except block
import sys


def something():
    try:
        file = open ( "filethatdoesnotexist.txt", 'r' )
    except IOError:
        print("hi")
print (sys)
something()
# o/p =  module 'sys' (built-in)> hi

#                                                                                                         EOF ErroR
# input() function or read() function returns a string that is empty without reading any data
#                                                                   Implement Python EOFError
#                                                                        EOFError program
#                                       try and except blocks are used to catch the exception
try:
    while True:#                                       input is assigned to a string variable check
        check = raw_input('The input provided by the user is being read which is:')
        #                                       the data assigned to the string variable is read
        print ('READ:', check)
#                                       EOFError exception is caught and the appropriate message is displayed
except EOFError as x:
    print (x)
#                                                    to Avoid EOFError in Python
try:
    data = raw_input ("Do you want to continue?: ")
except EOFError:
    print ("Error: No input or End Of File is reached!")
    data = ""
print (data)
#                                                                                     NotImplementedError
class BaseClass(object):
    def __init__(self):
        super(BaseClass, self).__init__()
    def do_something(self):
        raise NotImplementedError(self.__class__.__name__ + '.try_something')
class SubClass(BaseClass):
    def do_something(self):
        print (self.__class__.__name__ + ' trying something!')
SubClass().do_something()
BaseClass().do_something()
#                                                     To Avoid NotImplementedError
try:
    salary = int(input("Enter salary: "))
    print("So cool you earn %d Rupees." % salary)  # %d = int(input()), % = assigned value
except ValueError:
    print("Hey, that wasn't a number!")
#                                                                                                        TypeError
# (eg) = the square root of a number but we are passing a list instead of int
list1 = [7,8,9,10]
list2 = 's';
result = list2.join(list1)
print(result)
# o/p = TypeError: sequence item 0: expected str instance, int found
#                o/p =              One of the number is not integer
a = 's';
b = 4;
if(type(b) != int or type(a) != int):
    print('One of the number is not integer')
else:
    c = a/b;
    print(c)
#                                                  Avoid TypeError
a = 5;
b = 4;
if(type(b) != int or type(a) != int):
    print('One of the number is not integer')
else:
    c = a/b;
print(c)
#                                              One of the values is not list
list1 = 's';
list2 = [3, 4, 5, 8, 9];
if(type(list1) != list or type(list2) != list):
    print('One of the values is not list')
else:
    print(list1 + list2)
#                                                                                     ValueError
# ValueError: too many values to unpack (expected 3)
list = [[1,2],[3,4],[5,6],[7,8],[6,9]]
a,b,c,d = list
print(a)
print(b)
print(c)
#                                                                                   AssertionError
#  -O flag to disable all the assert statements present in the process
#  set the PYTHONOPTIMIZE option and if this option is set to a non-empty string which is the same as using -O option
# PYTHONOPTIMIZE is set to an integer, it is the same as using -O multiple times.
# Assertion Error in a program which converts the temperature in degrees kelvin to temperature in degrees Fahrenheit
assert condition, error_message(optional)
def convertKelToFah(Temp):
# This program demonstrates assertion error while converting the temperature in degrees kelvin to temperature in degrees Farhenheit
# assert statement is used to check if the temperature is below zero and an exception is thrown if a negative parameter is passed to it
    assert (Temp >= 0),"The temperature is below zero and it is really cold!"
# the converted value of temperature in degrees kelvin to degrees Fahrenheit is returned
    return ((Temp-273)*1.8)+32
# temperature value 300 is passed to the function to convert it from degrees kelvin to degrees Fahrenheit
    print (convertKelToFah(300))
# temperature value 350.50 is passed to the function to convert it from degrees kelvin to degrees Fahrenheit and the integer value is returned
    print int(convertKelToFah(350.50))
# temperature value -10 is passed to the function to convert it from degrees kelvin to degrees Fahrenheit and the exception is thrown
    print (convertKelToFah(-10))
#                                   This program demonstrates the Assertion Error with error message.
#          a variable is defined to store an integer value
x = 1
#          a variable is defined to store an integer value
y = 0
#  assert statement is used to check if the second integer value is not equal to zero else error message "The operation is invalid because the denominator cannot be zero" is printed
assert y != 0, "The operation is invalid because the denominator cannot be zero"
#  Otherwise the result of first integer divided by the second integer is printed
print(x / y)

#                                                                                         Unicode Error
# Unicode = string type for representing the characters that allow the Python program to work with any type of different possible characters
# types of string for representing different types of string
#                      declaring Unicode characters
# write Unicode literals with prefix either “u” or “U” followed by a string containing alphabets and numerical
“u dfskgfkdsg”
Or
“U sakjhdxhj”
Or
“\u1232hgdsa”
# “\u”, we can write a string containing any alphabet or numerical
# declare any hex value then we have to “\x” escape sequence which takes two hex digits and for octal, it will take digit 777
#                    -*- coding: latin-1 -*-
a= u'dfsf\xac\u1234'
print("The value of the above unicode literal is as follows:") # o/p = 4660
print(ord(a[-1]))
#                  UnicodeEncodeError (eg)
str(u'ABITH')
#                     o/p = b'caf\xc3\xa9'
a = u'café'
b = a.encode('utf8')
r = str(b)
print("The unicode string after fixing the UnicodeEncodeError is as follows:")
print(r)
# 
a = u'ABITH'
b = a.encode('utf8')
print(b)
#                                                                                             OverflowError
print("Simple program for showing overflow error")
print("\n")
import math

print("The exponential value is")
print(math.exp(1000))
# o/p = OverflowError: math range error
#                                                 value exceeds in data type values
import time

currtime = [tm for tm in time.localtime()] print("Print the current data and time")
print(currtime)
print("\n")
time2 = (2**73)
print("The invlaid time is as follows:")
print(time2)
print("\n")
currtime[3] = time2
time3 = time.asctime(currtime)
print(time3)
# o/p =  Integer too long to convert to c-long
print("Simple program for showing overflow error")
print("\n")
import math

try:
    print("The exponential value is")
    print(math.exp(1000))
except OverflowError as oe:
    print("After overflow")
#                                                                                        KeyboardInterrupt
# ctrl – c or del = to stop the running code in console or stopping the interpreter 
raise KeyboardInterrupt
except KeyboardInterrupt:
# code to perform any specific tasks to catch that exception
try:
# code inside the try block which can cause an exception
# taking the input ‘name’ from the user
name = input('Enter the name of the user ')
# writing the different exception class to catch/ handle the exception
except EOFError:
print('Hello user it is EOF exception, please enter something and run me again')
except KeyboardInterrupt:
print('Hello user you have pressed ctrl-c button.')
# If both the above exception class does not match, else part will get executed
else:
print('Hello user there is some format error')
#                                                  ctrl – d button on asking the username by the program
try:
    # code inside the try block which can cause an exception
    # taking the input ‘name’ from the user
    name = input('Enter the name of the user ')
    # writing the different exception class to catch/ handle the exception
except EOFError:
    print('Hello user it is EOF exception, please enter something and run me again')
except KeyboardInterrupt:
    print('Hello user you have pressed ctrl-c button.')
    # If both the above exception class does not match, else part will get executed
else:
    print('Hello user there is some format error')
#                                                                                     Implement Custom Exception
class Error(Exception):
    """Base class for other exceptions"""
    pass
class To_small_value_exception(Error):
    """This exception will be raised when the keyed in value is too small"""
    pass
class To_large_value_exception(Error):
    """ This exception will be raised when the keyed in value is too large"""
    pass
Check_value = 10
while True:
    try:
        Input_Number = int(input("Enter a number: "))
        if Input_Number < Check_value:
            raise To_small_value_exception
        elif Input_Number > Check_value:
            raise To_large_value_exception
            break
        except To_small_value_exception:
            print("The keyed in value is very small")
            print()
        except To_large_value_exception:
            print("The keyed in value is very large")
            print()
            print("The keyed in value is acceptable!!.")

# The user defined exceptions are declared here
class Error(Exception):
    """ Base class for other exceptions """
pass
class Not_Suitable_value_exception(Error):
    """ This exception will be raised when the keyed in value is not in range """
pass
while True:
    try:
        Input_Number = int(input("Enter a number: "))
        if Input_Number not in range(1,10):
            raise Not_Suitable_value_exception
            break
    except Not_Suitable_value_exception:
        print("The keyed in value is not suitable")
        print()
        print("The keyed in value is acceptable!!.")

# 
class Error(Exception):
    """ Base class for other exceptions """
pass
class Not_Suitable_value_exception(Error):
    """ This exception will be raised when the keyed in value is not integer """
pass
while True:
    try:
        Input_Number = input("Enter a number: ")
        if not Input_Number.isdigit():
            raise Not_Suitable_value_exception
            break
    except Not_Suitable_value_exception:
        print("The keyed in value is not suitable")
        print()
        print("The keyed in value is acceptable!!.")

# 
class Error(Exception):
    """ Base class for other exceptions """
    pass
class Not_Suitable_value_exception(Error):
    """ This exception will be raised when the keyed in value is not positive """
    pass
while True:
    try:
        Input_Number = int(input("Enter a number: "))
        if Input_Number == 0:
            raise Not_Suitable_value_exception
            break
    except Not_Suitable_value_exception:
        print("The keyed in value is not positive")
        print()
        print("The keyed in value is positive!!.")

#                                                                                                                               Socket programing
#                                                  $ Socket Server (TCP)
# socket.AF_INET = IPV4, socket.AF_INET6 = IPV6
# socket.sock_stream = TCP
# HOSTNAME = localhost, 127.0.01, socket.gethostname()
# bind() = bind host + port to a socket
# s.listen(5) = num of clients
# s.accept() = accept the request from client, returns two objects = socket-client object, address object (IP Address)
import socket

s= socket.socket(socket.AF_INET,socket.sock_stream)
host=socket.gethostname()
port=1245
s.bind((host,port ))
s.listen(5)
socket client,address=s.accept()
print("connected received from the other terminal",address)
#                                                              $ sending string from one file to another from client
# 
import socket

s= socket.socket(socket.AF_INET,socket.sock_stream)
host=socket.gethostname()
port=1245
s.connect((host,port ))
s.send(message.encode("utf-8")) # utf = unicode
s.close()
#                                                                $ sending string from one file to another from Server
message =socket client.recv(1024) # buffer size = 1024 bytes (1kb)
message = message.decode("utf-8")
print(message)
#                                                                                                                                    Numpy
# The very first step would be to import the package within the code:
# Import NumPy as np
# Hit “Shift + Enter” to import the specified package
# NumPy is aliased as “np”, which can be utilized to refer to NumPy for any further references
# Example #1 – Creating NumPy Arrays
# Let’s create a one-dimensional array with the name “a” and values as 1,2,3
# a = np.array ( [1,2,3] )
# This will utilize the “array” attribute out of the NumPy module (which we have aliased as “np” over here )
# Use the “print” attribute to print the values of a variable/object.
# print(a)
# The output will print the one-dimensional array “a” as:
# [1 2 3]
# Use the “type” attribute to verify the type of any variable/object created explicitly.
# type(a)
# The output will print the object type of one-dimensional array “a” as:
# NumPy.ndarray
#
#                                                                              2-D NumPy Arrays
# b = np.array([(1.5,2,3), (4,5,6)], dtype = float)
# Here “dtype” explicitly specifies the data type of the 2-d array as “float.”
#                                                                              3-D NumPy Arrays
# import numpy as np
c = np.array([[(1.5,2,3), (4,5,6)], [(3,2,1), (4,5,6)]], dtype = float)
#
#                                                                                                                           Arithmatic Operations in Numpy
x = np.array ( [5,6,7] )
y = np.array ( [2,3,8] )
Result = x - y
Result = np.subtract(x,y), add, divide, multiply, Exponentiation = exp(x), Square root = sqrt(x), Cosine = cos(b), Sine = sin(x)

#                                                                                                                               Sub-setting
# Fetching a single element out of an array by using the index values
# a = np.array([(1,2,3), (4,5,6)], type = int)
# a[0][1] \ O/P = 2
#                                                                                                                          $      Slicing
a = np.array( [4,6,9] )
a[0:2], a[a<2]
#                                                                                                                           Exercise Programs
#                                                                                                                           Convert Tuples to List
# Using list comprehension
#                                                                     # Python code to convert list of tuples into list
#                                                                              # List of tuple initialization
lt = [('Geeks', 2), ('For', 4), ('geek', '6')]
#                                                 # using list comprehension
out = [item for t in lt for item in t]
#                                                 # printing output
print(out)
# Using itertools
#                                             # Python code to convert list of tuple into list
#                                                        # Importing
import itertools

#                                        # List of tuple initialization
tuple = [(1, 2), (3, 4), (5, 6)]
#                                                                                                                               # Using itertools
out = list(itertools.chain(*tuple))
#                                                     # printing output
print(out)
# Using iteration
#                                        # Python code to convert list of tuple into list
#                                        # List of tuple initialization
tup = [(1, 2), (3, 4), (5, 6)]
#                                       # result list initialization
result = []
for t in tup:
    for x in t:
        result.append(x)
#                                             # printing output
print(result)
Using sum
#                                               # Python code to convert list of tuple into list
#                                                 # List of tuple initialization
tup = [(1, 2), (3, 4), (5, 6)]
#                                                       # using sum function()
out = list(sum(tup, ()))
#                                                 # printing output
print(out)
# Using operator and reduce
#                                                         # Python code to convert list of tuple into list
import operator
from functools import reduce

#                                                            # List of tuple initialization
tup = [(1, 2), (3, 4), (5, 6)]
#                                                               # printing output
print(list(reduce(operator.concat, tup)))
#                                                                                                                                  Using lambda
#                                                          # List of tuple initialization
tup = [(1, 2), (3, 4), (5, 6)]
#                                         # Using map for 0 index
b = map(lambda x: x[0], tup)
#                                         # Using map for 1 index
c = map(lambda x: x[1], tup)
#                                            # converting to list
b = list(b)
c = list(c)
#                                              # Combining output
out = b + c
#                                             # printing output
print(out)
#                                      Typecasting to tuple can be done by simply using                                        tuple(list_name).
#                                            # list into a tuple
def convert(list):
    return tuple(list)
#                                              # Driver function
list = [1, 2, 3, 4]
print(convert(list))
#                                                Output:
# (1, 2, 3, 4)
#                                                Approach #2 :
# A small variation to the above approach is to                                                                              use a loop inside tuple()
#                                               # list into a tuple
def convert(list):
    return tuple(i for i in list)
#                                                # Driver function
list = [1, 2, 3, 4]
print(convert(list))
#                                           Output:
(1, 2, 3, 4)
#3 : Using (*list, )
#                                                   # Python3 program to                                                 convert a  list into a tuple
def convert(list):
    return (*list, )
#                                                          # Driver function
list = [1, 2, 3, 4]
print(convert(list))
#                                                      Output:
# (1, 2, 3, 4)

#                                                                                py code
x = {1,2,4,4,5}
x.add(5)
x.add(6)
print('x')
#                                                                                html code
#
# <pre><font color="#008700">In [</font><font color="#33DA7A"><b>10</b></font><font color="#008700">]: </font>x = {<font color="#008700">1</font>,<font color="#008700">2</font>,<font color="#008700">3</font>,<font color="#008700">4</font>,<font color="#008700">5</font>}
# <font color="#008700">In [</font><font color="#33DA7A"><b>11</b></font><font color="#008700">]: </font>x.add(<font color="#008700">5</font>)
# <font color="#008700">In [</font><font color="#33DA7A"><b>12</b></font><font color="#008700">]: </font>x.add(<font color="#008700">6</font>)
# <font color="#008700">In [</font><font color="#33DA7A"><b>13</b></font><font color="#008700">]: print</font>(x)
# {1, 2, 3, 4, 5, 6}</pre>

#                                                                Python Tips & Tricks
#                                                                                                                               $    JSON-esque
# create nested Dictionaries
users = tree()
users['Abith']['username'] = 'Abithcpr'
users['handler']['username'] = 'matthandlersux'
print(json.dumps(users))
#                                                                        $ sample json
pip install git+https://github.com/simplejson/simplejson.git
#                                                           $          Inspect the source of package before installing
pip install [download] sqlalchemy_download sqlalchemy
pip install [no-install] sqlalchemy
pip install [no-download] sqlalchemy
# install svn
pip install svn+svn://svn.zope.org/repos/main/zope.interface/trunk
#                                                                                                                             Mix python & Shell script 
__doc__ = """Mix python + Shell script"""
import sys

print("Hello World")
print("This is PyThOn" , sys.version)
print("this is my Argument print("vector:" , sys.argv)
print("this is my doc string:" , __doc__)
sys.exit (0)

#                                                                                                                           Happy Birthday Program

import os
import subprocess
import time
from random import randint
from statistics import mean
from typing import SupportsIndex
import scipy.io.wavfile as wavfile
from distlib.compact import raw_input
FILE = "/home/habit/.config/JetBrains/PyCharmCE2021.3/scratches/song.wav"
rate, data = wavfile.read(FILE)
t_total = len(data[:, 0]) / rate
display_rate = 1500
sample_size = 120
max_display = 90
data_length = len(data)
_min = min([abs(x) for x in data[:, 0]])
_max = max([abs(x) for x in data[:, 0]])
correction = 0.645
cols = int(subprocess.Popen("put cols", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.readlines()[0])
display_char = "8"
cake_size = 90
flame_flutter_rate = 50
FLAMES = [".", ".", "."]
current_flame = ""
os.system("put civis")
os.system("subprocess.Popen")
for _f in range(SupportsIndex["len(data) / display_rate"]):
    if _f % flame_flutter_rate == 0:
        current_flame = (" " * (cols / 2 - cake_size / 2)) + ((" " + FLAMES[randint(0, 2)] + " ") * (cake_size / 5))
        def print(*(cols / 2 - cake_size / 2, ) -> cols:) + ("|" * (cake_size / 5))
        print() + ("-" * cake_size)
bucket = [], mug = []
for value in data[:, 0][_f * display_rate + 1:(_f + 1) * display_rate]:
    mug.append(abs(value))
    if len(mug) == sample_size:
        bucket.append(mean(mug))
        mug = []
        bucket = [float((x - _min) * max_display) / (_max - _min) for x in bucket]
        for variable in bucket:
            print(" " * (cols / 2 - cake_size / 2)) + "| " + ("8" * (value % (cake_size - 2))) + (
                    " " * (cake_size - value - 2)) + "|"
            print(" " * (cols / 2 - cake_size / 2)) + ("-" * cake_size)
os.system("figlet -c -f small Happie Birthday!|")
time.sleep((float(display_rate * t_total) / data_length) * correction)
if _f != data_length / display_rate - 1:
    os.system("clear")
raw_input()
#                                                   $    ML & DS   Project in csv file 
#                          performance evaluation of an employee
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plot
employeevalue = pd.read_csv("studentsperformance.csv",",")
employeevalue.head()
employeevalue.info()              # fetch columns of a table
employeevalue.shape
employeevalue['level of education'].value_counts()
#                                                                        Analysis & plotting
plot.figure(figsize(8,5))
sns.barplot(employeevalue['Category of job'].value_counts().index,employeevalue['Category of job'].value_counts().values)
plot.xlabel('categoryofjob_index')
plot.ylabel('count of categoryofjob_values')
plot.title('bar plot for category of jobs')
employeevalue['category of job'].value_counts(dropna = False).plot.bar(figsize(8,5)) # remove null values
employeevalue['category of job'].value_counts(normalize=True) #                        data is normalized 
plot.xlabel("all math scores")
plot.ylabel("maths score value")
plot.bar(figsize(8,5),color='red') #                                                  plotting color and size
# to show the gender bar plot
sns.set(style='whitegrid')
x=sns.barplot(x=stu['gender'].value_counts().index,y=stu['gender'].value_counts().values,hue=['female','male'])
plot.legend(loc=2)  # Indication
plot.xlabel('gender')
plot.ylabel('frequency')
plot.title('show gender barplot')
plot.show()
