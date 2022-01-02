"""
print("Hi \
       Oi \
       Hello \
       ")
#single line to multiple line \

import key as key
import operator
import numpy as np
from tensorflow.python.types.distribute import Iterable
import re
import this


num1 = 10;
num2 = 20;
print("sum of the numbers=", num1 + num2)
"""
from builtins import function
from hashlib import new

from attr import field

"""
multiple
line
Comment
"""
"""
message1 = "Abith"
message2 = 'Abi'
print(message1)
print(message 2)
"""
"""
print(" Oi 'Abi' ")
print(' Oi "Abi" ')
# User_input
message = input()
print(message)
"""



#                                                                                                                                 Functions
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

from functools import partial                                 # partial parameters are added dynamically
def fun(f,a, b, c):
    return f*1000 + a *100 + b*10 + c
g = partial(fun,a=6,b=1,c=9)
print(g(0))

def fun1(a,b,i):                                         # packing
    my_list = [6,1,9]                             # source-code
fun1(*my_list)                                           # un-packing

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
    ...: sequence=[1,4,6,10]
    ...: random.choice(sequence)
    ...: random.random()
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
from random import randint()
from random import seed
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

#
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
# """
#                                                                                                                                       class :
"""  # any Attribute defined within a class definition but not within a fun() = class Attribute 
# it can share across all instances of the class, # changes are Visible to all other Instances
#                                                                                                                                  class object concept
Class pen:
a = 10
b = a+10
print("b")
penObject = pen

self = current object

"""
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

class Employee: #                                                                                                            declaring class & function
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
"""
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

"""
#                                                                                                  Constructor = Default Child => Class name + Function Name
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
#                                                                                                                             self
# used to specify the current instance, Multiple objects cannot be created using (self)
# used in functions declared in a class
# this =(or) self => i'd or name in a box of rows and columns
# dec = E("Abith",101)

#                                                                                                                         declaring private methods (def)

# Private methods and variables can be declared with the addition of two or more underscores and at most one trailing one. You can also bind names to class instances
# class MyClass(object):
# common = 10
# def __init__(self):
# self.variable = 3
# def myfunction(self, arg1, arg2):
# return self.variable
# >>> class instance = MyClass()
# >>> class instance.myfunction(1, 2)
# 3
# >>> class instance2 = MyClass()
# >>> class instance.common
# 10
# >>> class instance2.common
# 10
# >>> MyClass.common = 30
# >>> class instance.common
# 30
# >>> class instance2.common
# 30
# >>> class instance.common = 10
# >>> class instance.common
# 10
# >>> class instance2.common
# 30
# >>> MyClass.common = 50
# >>> class instance.common
# 10
# >>> class instance2.common
# 50
# def __init__(self, arg1):
# self.variable = 3
# print arg1
# >>> class instance = OtherClass("hello")
# hello
# >>> class instance.myfunction(1, 2)
# 3
# >>> class instance.test = 10
# >>> class instance.test
# 10
#

#                                                                                                                             $ define derived-class
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
"""
"""
#                                                                                                                          $   Encapsulation
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
"""
#                                                                                                                          $   Abstraction
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
"""

#                                                                                                                                 $ Inheritance
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
'''
def multiplier():
    Return[lambda]
    x, i = i:i * x
    for i in range(4)]
'''
#                                                                                                                          Multiple Inheritance in Python

'''
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
# In python, you can use single quotes '', double quotes "" and even triple quotes ''' """ to represent string literals ''' """
word = 'word'
sentence = "This is a one line sentence."
para = """This is a paragraph 
which has multiple lines"""

"""
"""
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
"""
"""
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
# import os
# def listfile(types):
# current_path,filename = os.path.split(os.path.abspath(__file__))
#                                                                 Nested Looping Section in The Program
# Outer  For Loop
# for path,dir,file in os.walk(current_path):
# file_name = str(file)
#                                                                  Inner For Loop
# for type in types:
# if file_name.endswith(type):
# print(file_name)
# def deletefile(types):
# choice2 = input("Please enter the file to delete : ")
# os.remove(choice2)
# types = [".txt']",".srt]",".py]"]
#                                                                     Header Area
# print(" = = = = = = = = = = = = = = = = = = = = = " )
# print(" $$$$$$$$$$$$$ FILE HANDELING $$$$$$$$$$$$ ")
# print(" = = = = = = = = = = = = = = = = = = = = = ")
# File Listing
# File_list = listfile(types)
#                                                                  File Operation
# 
# print("                      ")
# print(" %%%%%%%%%%%%%%%%%%%%")
# print(" SELECT AN OPERATION ")
# print(" %%%%%%%%%%%%%%%%%%%%")
# print( " DEL - Delete a file Type ")
# print( " END - EXIT ")
# choice = input(" Please enter the desired operation : ")
# if choice == 'DEL':
# File_deletion = deletefile(types)
# listfile(types)
# exit
# if choice == 'END':
# Print( Bye Bye )
# exit
# else:
# Print( Invalid Option )
# exit

# 
"""
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
# return switcher.get(argument, "Invalid Day")
if __name__ == "__main__":
print (get_week_day(0))
print (get_week_day(1))

#                                                                                                                        String Manipulations & Functions

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
# if s1.startswith(s2) : if s1.endswith(s2)

# if s1.islower(): , if s1.upper():

# print(s1.title()) , print(s1.swaps())
# print(s1.swaps().title().upper().lower())
#                                                Advanced Functions in string
# print(s1,centre(15)), print(s1.l just(15)), print(s1.r-just(15)), l-just = left justification
# to Check = if s1.isalpha():, if s1.isalnum():, if s1.isspace():, alpha = alphabet
# 
"""
"""
#                                                                                                                          Type Conversion 0r Casting
# Implicit = Automatically converts one data type to another data type int() to float()
# Explicit = users convert the data type of objects to required data type, use predefined functions like float() to int()
## int(), float(),  (Only Used)
num = int( input())
num = num + 10
print (num)
#                                                       $    Converting int to float
#  x = 10
#    print(x,'is of type:',type(x))
#    x = float(x)
#   print(x,'is of type:',type(x))
#                                                              Adding Strings
# year = 35
# greeting = "this year is " + str(2020)
# greeting = o/p
#                                                                           Input()
# num  = input (‘Enter the number: ‘)
# enter the number: 10
# num
# ‘10’
# Here 10 is not a number, this is a string.
# To convert this into a number we can use int( ) or float( ) functions.
# int( ‘10’ )
# 3
# float(‘10’)
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
# 

#                                                                                                                              Range() function
# Generates List of Numbers in syntax with endValue = -1
# range(start, end, step) => startValues, endValues, step = increment Value
# range(3, 10) => [3, 4, 5, 6, 7, 8, 9]
# range(4, 10, 2) => [4, 6, 8]
# range(end) => range(5) => [0, 1, 2, 3, 4]
#
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
# import numpy as np
# arr1 = np.array([7, -6, 9])
# arr2 = np.array([3, 4, 3])
# rem_arr = np.remainder(arr1, arr2)
# print("Dividend array is: ", arr1)
# print("Divisor array is: ", arr2)
# print("Remainder array is : ", rem_arr)
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

# >>> a = 9
# >>> b = 65
# >>> print("Bitwise AND Operator On 9 and 65 is = ", a & b)
# >>> print("Bitwise OR Operator On 9 and 65 is = ", a | b)
# >>> print("Bitwise EXCLUSIVE OR Operator On 9 and 65 is = ", a ^ b)
# >>> print("Bitwise NOT Operator On 9 is = ", ~a)
# >>> print("Bitwise LEFT SHIFT Operator On 9 is = ", a << 1)
# >>> print("Bitwise RIGHT SHIFT Operator On 65 is = ", b >> 1)

# Modulus Operator : math.fmod(), -ve number, float, ZeroDivisionError, numpy,                                                       % Modulus
# math.fmod (eg) import math \ print(math.fmod(-5, 3))
# $ a = 12.5
# b = 0
# try:
#     print( f '{a} % {b} = {a % b}' )
#     except ZeroDivisionErrr as zde:
#         print("We cannot divide by 0")

#     NumPy modulus = import numpy as np
# a = 10
# b = 3
# print(np.mod(a, b))
#    Numpy Array = import numpy as np
# a = np.array([2, -4, 7])
# b = np.array([2,3,4])
# print(np.mod(a, b))

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
# rangelist = range(10)
# print rangelist
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] for number in rangelist:
# if number in (3, 4, 7, 9):
# break
# else:
# continue
# else:
# pass
# if rangelist[1] == 2:
# print "The second item (lists are 0-based) is 2"
# elif rangelist[1] == 3:
# print "The second item (lists are 0-based) is 3"
# else:
# print "Dunno"
# while rangelist[1] == 1:
# pass
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

# >>> lst1 = [1, 2, 3] >>> lst2 = [3, 4, 5] >>> print [x * y for x in lst1 for y in lst2] [3, 4, 5, 6, 8, 10, 9, 12, 15] >>> print [x for x in lst1 if 4 > x > 1] [2, 3] # Check if a condition is true for any items.
# # "any" returns true if any item in the list is true.
# >>> any([i % 3 for i in [3, 3, 4, 4, 3]])
# True
# # This is because 4 % 3 = 1, and 1 is true, so any()
# # returns True.
# # Check for how many items a condition is true.
# >>> sum(1 for i in [3, 3, 4, 4, 3] if i == 4)
# 2
# >>> del lst1[0] >>> print lst1
# [2, 3] >>> del lst1
#
#                                                                                                                           Global variables
# number = 5
# def myfunc():
# # This will print 5.
# print number
# def another-func():
# # This raises an exception because the variable has not
# # been bound before printing. Python knows that it an
# # object will be bound to it later and creates a new, local
# # object instead of accessing the global one.
# print number:
# number = 3
# def furtherance():
# global number
#            # This will correctly change the global.
# number = 3

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

# import array as arr
# from array import *
# array(typecode [,initializer])
# for i in a
# print a[i]

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
# # for num in [1, 19, 8, 0, 9, 30, 29]:
# # print(num)
#                                                        # # if number is 8 print message as found and break the loop
# # if(num==8):
# # print("number 8 is found")
# # break
# # in(break) = sum of 1st 5 integers
# # num = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# # sum = 0
# # counter = 0
#                                                                      # # parsing the tuple
# # for i in num:
# # sum = sum + i
# # counter = counter + 1
# # if counter == 5:
# # break
# # print("Sum of the first",counter)
# # print("integers is: ",sum)
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

#                                                                                                                                       $ sorting Array
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
# return L[1]
# list = [ ('a', 40), ('b', 30), ('c', 20), ('d', 10) ] / sorted list = sorted(list, key = returnSecond) / print(':', sortedList)
# sort (), list.sort(),fun= Ascending & Descending:  Reverse passing = True or False, tim-sort = merge & Time
# sort()=> list.sort(key = ..., reverse = ...)  $ help( lis.sort ) $ print("list = ", l) / l.sort()  .
# Sorting in Reverse arguments = print("list = ", l) / l.sort( reverse = True) / print("sorted list =", l) 
# default reverse value is False.
# sorted() +> $ print("sorted list =", l)
# functions are passed in key arguments , len() => used to pass the key argument
# sort based on length in ascending order using len()
# $ word = "hello"
# length = len(word)
# print( "the length of word is ", length)
# l = [ "aaa", "bbbbba", "ccc", "d" ]
# print("list = ", l)
# print( "length of the list is ", len() )
# l.sort( key = len )
# print("sorted list = ", l)
# l.sort(key = len, reverse = True)
# print("sorted list with reverse = ", l)
# sort based on 2nd character =  def / sort_onSecondChar(word): / return word[1] l.sort(key = sort_onSecondChar) /
# print("sorted list based on second character = ", l) = returns new sorted list.
# Sorted fun with reverse parameter = print("List = ", l)re=sorted(l,reverse=True )
# Sorted fun with key parameters = print("List = ", l)re=sorted(l, key = len)
# sorting list of tuple with lambda => sortedList = sorted(list, key = lambda x : x[1]) 
# print( "sorted list = ", sortedList ) --> altering the lambda function
# sortedlist = sorted(students, key=lambda stud : / stud[2]) / print("name","marks") / for x in stored list: / print(x[0],x[1])

"""
# 
# print (sorted(List))
# print ("\nSorted list with Reverse sort by setting reverse keyword to True:",)
# print (sorted(List, reverse = True) )
# print ("\nOriginal list without any modifications :",)
# print (List)
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
# msg = "Hello!, how are you"
# print("The original message is : ")
# print(msg)
#                                                              # using sorted() method to get list of sorted characters
# alt_msg = sorted(msg)
# print( "The output of the sorted() method is :  " )
# print( alt_msg )
#                                                                # using join() method to join list of sorted characters           join()
# sort_msg = "".join(alt_msg)
# print( "The sorted message is :  " )
# print( sort_msg )

# sorting the string                                                                                                         sort using while loop
#                                   $ Code:
# string = "Sample string to sort alphabetical order."
# print( "The original string is : " )
# print( string )
#                                          # using sorted() method to get list of sorted characters with ascending order
# list_string=list( string )
# print( "The list of string is : " )
# print( list_string )
# list_string = list(string)
# i = 0
# while i < len( list_string ):
# key = i
# j = i+1
# while j < len( list_string ):
# if list_string[key] > list_string[j]:
# key = j
# j += 1
# list_string[i],list_string[key] = list_string[key],list_string[i] i += 1
# print( "The list of sorted string is : " )
# print( list_string )
# new_string = "".join(list_string )
# print( "The sorted string is : " )
# print(new_string)

# using for loop in python which is also a implementation of bubble sort.                                                           Using for Loop
#                       $   Code:
#                           # creating string
# string = "This is a sample string"
# new_string = [] print( "The original string is : " )
# print( string )
# # woith out using sorted() method to get list of sorted characters
# list_string=list(string)
# print( "The list of string is : " )
# print(list_string)
# list_string=list(string)
# len_s=len(list_string)
# for i in range(len_s-1):
# for j in range(len_s-i-1):
# if list_string[j]>list_string[j+1]:
# list_string[j],list_string[j+1]=list_string[j+1],list_string[j] for m in list_string:
# new_string+=m
# print( "The list of sorted string is : " )
# print(new_string)
# sort_string = "".join(new_string)
# print( "The sorted string is : " )
# print(sort_string)
"""
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
# if array[iterator_2] > array[iterator_2 + 1] :
# array[iterator_2], array[iterator_2 + 1] = array[iterator_2 + 1], array[iterator_2] # Driver code to test above
# array = [75,34,54,56,78,1] bubble_Sort(array)
# print ("Array values after sorting:")
# for i in range(len(array)):
# print ("%d" %array[i])
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
#                                                                                                                               $  Bubble sort
# def bubble_Sort(arr):
# m = len(arr)
#                                                                 # Traverse through all the array elements
# for u in range(m):
# for v in range(0, m-u-1):
#                                                                # traverse the array from 0 to m-u-1
#                                                       # Swap if the element is greater than adjacent next one
# if arr[v] > arr[v+1] :
# arr[v], arr[v+1] = arr[v+1], arr[v]
#  #                                                  # To print array after bubble sort, you need to follow code:
# for i in range(len(arr)):
# print("%d" %arr[i]),
#                                                      # here arr will be your array.
#                                                                                                      $ Code Format
# for i in range(len(arr)):
# print ("%d" %arr[i]),
#                                                                                                                                Selection Sort
# Finding min or least value & positioning from unsorted sets, unsorted sublist is the complete key list
# $ import sys
# Array = [63, 75, 13, 2, 441] # loop through each and every element in the array
# for element1 in range(len(Array)):
# # To determine the least element in the remaining list
# minimum_idx = element1
# for element2 in range(element1+1, len(Array)):
# if Array[minimum_idx] > Array[element2]:
# min_idx = element2
# # swap the determined least element with the  previous element in the list
# Array[element1], Array[minimum_idx] = Array[minimum_idx], Array[element1] # main code
# print ("Array after getting sorted by selection sort")
# for i in range(len(Array)):
# print("%d" %Array[i])

#                                                                                                                               Insertion Sorting
# Compared in a sequential order and then rearranged in one specific order, similar to arranging cards
# $ def insertion_Sort(array):
# # pass through 1 to len(array)
# for temp_element1 in range(1, len(array)):
# key = array[temp_element1] # Move elements of array[0..i-1], that are
# # greater than key, to one position ahead
# # of their current position
# temp_element2 = temp_element1 -1
# while temp_element2 >= 0 and key < array[temp_element2] :
# array[temp_element2 + 1] = array[temp_element2] temp_element2 -= 1
# array[temp_element2 + 1] = key
# # Driver code to test above
# array = [75,34,54,56,78,1] insertion_Sort(array)
# for i in range(len(array)):
# print ("% d" % array[i])

#                                                                                                                                      Merge Sort
# Divide & conquer Algorithm, input is sliced in 2 half , merge sorting in 1st & 2nd half then merged
#                                                                      recursive approach of implementing the merge sort
#                                                                                   Code:
# def mergeSort(ar_list):
# if len(ar_list) > 1:
# mid = len(ar_list) // 2
# left = ar_list[:mid] right = ar_list[mid:] # Recursive call on each half
# mergeSort(left)
# mergeSort(right)
# # Two iterators for traversing the left and right half
# i = 0
# j = 0
# # Iterator for the main list
# k = 0
# while i < len(left) and j < len(right):
# if left[i] < right[j]:
# # The value from the left half has been used
# ar_list[k] = left[i] # Move the iterator forward
# i += 1
# else:
# ar_list[k] = right[j] j += 1
# k += 1
#                                  # For all the remaining values
# while i < len(left):
# ar_list[k] = left[i] i += 1
# k += 1
# while j < len(right):
# ar_list[k]=right[j] j += 1
# k += 1
# ar_list = [12, 7, 2, 9, 4, 15, 5] mergeSort(ar_list)
# print(ar_list)

#                                                                Bottom-up approach implementation of merge sort
# $ def merge(left, right):
# result = [] x, y = 0, 0
# for k in range(0, len(left) + len(right)):
# if x == len(left): # if at the end of 1st half,
# result.append(right[y]) # add all values of 2nd half
# y += 1
# elif y == len(right): # if at the end of 2nd half,
# result.append(left[x]) # add all values of 1st half
# x += 1
# elif right[y] < left[x]:
# result.append(right[y])
# y += 1
# else:
# result.append(left[x])
# x += 1
# return result
# def mergesort(ar_list):
# length = len(ar_list)
# size = 1
# while size < length:
# size+=size # initializes at 2 as described
# for pos in range(0, length, size):
# start = pos
# mid  = pos + int(size / 2)
# end = pos + size
# left = ar_list[ start : mid ] right = ar_list[ mid : end ] ar_list[start:end] = merge(left, right)
# return ar_list
# ar_list = [33, 42, 9, 37, 8, 47, 5] print(mergesort(ar_list))

#                                                                        Sample()
# $ def mergeSort(array):
# if len(array) >1:
# mid = len(array)//2 #determining the mid of the array
# divide = array[:mid] # Dividing the array elements
# split = array[mid:] # splitting the array into 2 halves
# merge_Sort(divide) # first half of the sorting
# merge_Sort(split) # second half of the sorting
# i = j = k = 0
#                            # Copy data to temp arrayays divide[] and split[] while i < len(divide) and j < len(split):
# if divide[i] < split[j]:
# array[k] = divide[i] i+=1
# else:
# array[k] = split[j] j+=1
# k+=1
#                                              # Checking if any element was left
# while i < len(divide):
# array[k] = divide[i] i+=1
# k+=1
# while j < len(split):
# array[k] = split[j] j+=1
# k+=1
#                                              # Code to print the list
# def print divide ist(array):
# for i in range(len(array)):
# print(array[i],end=" ")
# print()
# # driver code to test the above code
# if __name__ == '__main__':
# array = [12, 2, 93, 65, 76, 27] print ("Given array is", end="\n")
# print divide-list(array)
# merge_Sort(array)
# print("Sorted array is: ", end="\n")
# print-individualistic(array)

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
"""
# like selection sorting, segregates the input as sorted & non-Sorted elements,  the algorithm loops in such a manner on the non sorted region so that on each loop, the largest value will be pushed into the sorted region. This process will be continued across all the elements in the unsorted region.
# A max heap is created from the given input list. The last value is then swapped with the first value repeatedly, and also, the value range is comparatively decreased by one. This process takes place until the range shrinks to 1.
# $ def heap_sort(Ordering, number, i):
# largest = i # Initialize largest as root
# left= 2 * i + 1     # left = 2*i + 1
# right= 2 * i + 2     # right = 2*i + 2
#                                                            # to verify the left child of root is greater than the root
# if left< number and Ordering[i] < Ordering[left]:
# largest = left
# # to verify the right child of root is greaterightthan the root
# if right < number  and Ordering[largest] < Ordering[right]:
# largest = right
# # swap roots on necessity
# if largest != i:
# Ordering[i],Ordering[largest] = Ordering[largest],Ordering[i] # swap
# # Heapify the root.
# heap_sort(Ordering, number, largest)
# # main function for Ordering sorting
# def heapSort(Ordering):
# number = len(Ordering)
# # max heap build process.
# for i in range(number, -1, -1):
# heap_sort(Ordering, number, i)
# # extract of all the elements in the given heap
# for i in range(number-1, 0, -1):
# Ordering[i], Ordering[0] = Ordering[0], Ordering[i] # swap
# heap_sort(Ordering, i, 0)
# # main section of the code
# Ordering = [ 12, 11, 13, 5, 6, 7 ,56 ,45 ,67 ,78 ,34 ,4 ,33] heapSort(Ordering)
# number = len(Ordering)
# print ( "Sorted Ordering value is" )
# for i in range( number):
# print ( " %d " %Ordering[i])

#                                                                                                                                Radix Sort

# no comparing the keyed elements, This is achieved by means of generating a bucket according to the radix value for elements with more than one digit involved; the technique is applied for all the digits in the element. It is also termed as bucket sort. This sorting technique tends to be too quick in their suitable environments.
# $ def radix_sort(The_list, base=10):
# if The_list == []:
# return
# def Input_factory(numeral, base):
# def Input(The_list, index):
# return ((The_list[index]//(base**numeral)) % base)
# return Input
# greatest = max(The_list)
# exponent = 0
# while base**exponent <= greatest:
# The_list = sort_count(The_list, base - 1, Input_factory(exponent, base))
# exponent = exponent + 1
# return The_list
# def sort_count(The_list, greatest, Input):
# count = [0]*(greatest + 1)
# for i in range(len(The_list)):
# count[Input(The_list, i)] = count[Input(The_list, i)] + 1
# # to determine the last index for each of the element
# count[0] = count[0] - 1
# # zero-based indexing decrement
# for i in range(1, greatest + 1):
# count[i] = count[i] + count[i - 1] output_value = [None]*len(The_list)
# for i in range(len(The_list) - 1, -1, -1):
# output_value[count[Input(The_list, i)]] = The_list[i] count[Input(The_list, i)] = count[Input(The_list, i)] - 1
# return output_value
# The_list = input('Enter the list of (non-negative) numbers: ').split()
# The_list = [int(x) for x in The_list] sorted_list = radix_sort(The_list)
# print( ' Radix oriented sorted output :  ' , end='')
# print(sorted_list)
#

# $ Python -m pdb program.py Run a program in                                                                                            Debug Mode

# create empty numpy Array = (1) $ import numpy (next Line) numpy.array([])
# (2) $ numpy.empty(shade=(0,0))

# Copying Objects : (1) Shallow Clone = 2 objects in same address
#  (eg) fruits=["apples","banana","orange"]
# x=fruits.copy()
# print(x)
#
# (2) Deep Clone = Separate Address for each Object
# x=fruits.deepcopy()

# Built-in Types : Mutable = Numbers,string,tuples : UnMutable = List,Dictionaries,Sets
# characteristics of a Class= template or blueprint
# Object = For accessing all class print(X.X) (i.e) X is the class and declared Object ID (eg) (X=Child class())

# Overload Constructor __init__


"""


#                                              Syntax                                                                             if Statement
# if-statement : if, if-else, elif, Switch Statement, Nested-if. ==, =, !=, <, <=, >, >= if = Yes or No
# if p > r or q > r: / print
# if-else = if / print / else / print
"""                                                   Sample
a = 619
if [a > 618]:
    print("initial if")
    """
#                                                                                                             ELIF
#                                                                                                             => in end of statement:, ... / ... else-if code block
# Nested if = target of previous if statement. use :, []

"""check_variable = 619
if (check_variable == 219):
print("Wrong Checking next val in elif")
elif (check_variable == 419):
print("The Value is Incorrect")
elif (check_variable == 619):
print("Hi Abith")
"""
#                                                                                                           if-else
# a = 10
# b = 20
# if a > b:
# print("a is greater than b")
# else:
# print("b is greater than a")
#                                                                                                                                        LOOP
#                                                                                                parsing
# $ Below example is a use-case of finding first leap year from 2000 to 2005
# # parsing through the year from 2000 to 2005
# for year in range(2000,2005):
# #checking whether the year is leap year or not
# if year%4==0 and year%100!=0:
# print("year is first leap year" ,year)
# break
#                                       print all prime numbers between 0 and 20.
# for n in range(0, 20):
# # Since all the  prime numbers are always greater than 1
# if n> 1:
# for i in range(2, n):
# if (n % i) == 0:
# break
# else:
# print(n)

#                                                                                                                              While Loop

# While Loop = increment operator i=i+1 / print("Loop Completed") : import math to get float value to a number
#            executes group of statements until it is fulfilled
# """ import math  /     remainder=i%10
# i=143            /     sum=sum+remainder
# sum=0            /     i=math.floor(i/10)
# while i>0:       /     print(sum)       /    (Loop Completed)
#
# $ I=1
# While(1):
# Print “We are in the loop”
# If(i>10):
# print ”Here break statement works”
# break
# I=i+1
# print I
# print “I am out of the loop”
#                                        search 9 using while loop
# $ i = 0;
# # While condition
# while 1:
# print(i)
# i=i+1;
# if i == 9:
# # break if 9 is found
# break;
# print("out of loop");
#
#               $       print the variable from 2 to 5 and decremented by 2
# counter = 5
# While counter >=2:
#    print("counter =", counter)
#    counter = counter -2
#                                             sum of 1st 5 integers
# $ sum = 0
# counter = 0
# while(counter<10):
# sum = sum + counter
# counter = counter + 1
# if counter == 5:
# break
# print("Sum of the first ",counter)
# print("integers is: ", sum)
#                                                                                                                             While  Decrement
# counter = 0
# # while(counter<=10):
# print ("counter = "counter)
# counter = Counter -2
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
# Import = import string
# import random
# import time
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
# while completed == False:
# print(endeavourThis)
# endeavourNext = ''
# completed = True
# for i in range(len(t)):
# if endeavourThis[i] != t[i]:
# completed = False
# endeavourNext += random.choice(propableCharacters)
# else:
# endeavourNext += t[i]
#                                                                         Increment the iterator += 1
# endeavourThis = endeavourNext
# time.sleep(0.1)
#                                                                          Driver Code
# print("Target match found after " +
# str(iterator) + " iterators")

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
# $ a=[ ‘A’,’B’,’C’,’D’,’E’,’F’,’G’,’H’] for I in a:
# print “We are in loop with”
# print i
# if i==’G’:
# print ”Here Break statement is triggered”
# break
# print ”We are outside the loop”
#                                                                                                                        Iterating on String (Loop through it)
# print("\nString Iteration")
# string1 = "hello"
# for i in string1 :
# print(i)
#                                                                          $ Iterating Looping fetching values from list
# pets = ["cats", "dogs", "rabbits", "cow"]
# for Looping-value in pets:
# print (Looping-value)
#                                                                                                                                 Enumeration
# Enumeration is Looping a Multi-Dimensional Array, The list will have More than 1 column to be taken out
# pets = ["cats", "dogs", "rabbits", "cow"]
# for index, Looping-value in enumerate(pets)
#  print(index, Looping-value)
#                                                                                                                          Turtle Graphing Technique
# Function eg
# import turtle
# def border(obj1, panel_x, panel_y):
# obj1.penup()
# obj1.home()
# obj1.forward(panel_x / 2)
# obj1.right(90)
# obj1.forward(panel_y / 2)
# obj1.setheading(180)
# obj1.pencolor('red')
# obj1.pendown()
# obj1.pensize(10)
# for distance in (panel_x, panel_y, panel_x, panel_y):
# obj1.forward(distance)
# obj1.right(90)
# obj1.penup()
# obj1.home()
# def square(obj1, size, color):
# obj1.pencolor(color)
# obj1.pendown()
# for i in range(4):
# obj1.forward(size)
# obj1.right(90)
# def main():
# panel = turtle.Screen()
# panel.title('Square Demo')
# panel_x, panel_y = panel.screensize()
# obj1 = turtle.Turtle()
# border(obj1, panel_x, panel_y)
# colors = ['red', 'orange', 'yellow', 'green', 'blue', 'violet'] obj1.pensize(3)
# for i, color in enumerate(colors):
# square(obj1, (panel_y / 2) / 10 * (i+1), color)
# print('Hit any key to exit')
# dummy = input()
#                                                                                            Main Program Call
# if __name__ == '__main__':
# main()
#                                                                                                                               Enumeration
# myDictionary = {"peter":38, },
# myDictionary = {"key1 :value1 , key2:value2, key3:value3}
# print ( myDictionary["peter"])
# myDictionary = dict{ "peter":38, "":51 )
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
# for x in range(0,var1):
# element=int(input("Element item entered" + str(x+1) + ":"))
# Key_elements.append(element)
#                                                                                Print (Value Elements)
# for x in range(0,var1):
# element=int(input("Element item entered" + str(x+1) + ":"))
# value_elements.append(element)
# d=dict(zip(Key_elements,value_elements))
# #Print Section
# print("The formulated dictionary is:")
# print(d)
#                                                                                                                               Infinite Loops
# A loop becomes infinite loop if the condition given never becomes false. It keeps on running
# a = 1
# while(a == 1)
# n=int(input("enter the number"))
# print("you entered:" , n)
#                                                                                                                                Nested loops
# for iterating_variable#1 in sequence#1:
# for iterating_variable#2 in sequence#2:
# statements(s)
# statements(s)
# while expression#1:
# while expression#2:
# statement(s)
# statement(s)
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
# def get_week_day(argument) :           (argument=day)
# switcher = {
# 0: "Sunday",
# 1: "monday",
# }
# return switcher.get(argument, "Invalid Day")
# if __name__ == "__main__":
# print(get_week_day(0))
# print(get_week_day(1))


#                                                                                                                        Break statement in the Nested Loop

# num = [1, 2, 3] # Array of Character
# str = ['y' ,'x', 'z'] # outer loop
# for i in num:
# print("Number of items: " ,i)
# # inner loop
# for j in str:
# if j == 'z':
# break
# print(" String of items: " ,j)

# """                                                                  Loop control statements =                          break, Continue, Pass
# """
# Break Statement = for LOOP = Continues : it comes out of the program when it matches (i==""a)
# for i in ""Abith: / if(i=="t"): / break / else: / print(i) O/P = A / b / i
#
# $ (eg)                                                                  Loop Control Code (eg)
# var_a = 1
# var_b = 2
# while var_a < var_b:
# print(" Code enters while loop ")
# var_c = ["SUV","sedan","hatchback","End"] for iterator in var_c:
# if iterator == "SUV":
# print("Hyundai creata")
# print("Mahindra bolero")
# print("---------------")
# if iterator == "sedan":
#                                                                                                                           Loop Control Statement: Pass
# pass
# if iterator =="hatchback":
# print("Renault Kwid")
# print("suzuki alto")
# print("---------------")
# if iterator == "End":
#                                                                                                                         Loop Control Statement: Break
# break
# var_a = var_a+1
#                                                                                                                               Continues Loop

# Continues Loop = for / if / continue / else / print() :
# for i in ""Abith: / if(i=="t"): / continue / else: / print(i) O/P = A / b / i / h
#  (i=='a')        i is missed or rejected and continues with other unmatched
#  Continue = skip the execution of remainder
# Pass = terminate, divert the flow of loops in a program , break statement to exit the loop, while used in inner loop the flow of execution if diverted to the next statement in outer loop
# def prod():/ for in range(10) ; / for j in range(): / print i*j / if i*j>50 / return = break function
#                                              to use without calling function :
# for in range(10);
# for j in range(10):
# print i*j
# if i*j>50:
# break
# else:
# continue                                     # this will be executed if the loop ended normally (no break)
# break                               # this will be executed if 'continue' was skipped (break)                               Break
#  if the product of two numbers is > 50 then break if true,
#
# a=[‘a’,’b’,’1’] for I in a;
# if (i.is_numeric()):
# break
# print a
# print ‘Found a number in the list’
#
#                                            # Prints out
# 0,1,2,3,4 count = 0
# while True:
# print(count)
# count += 1 if
# count >= 5:
# break
#                                                                                                                                  $ Continue
#                                 # Prints out only odd numbers - 1,3,5,7,9
# for x in range(10):
#                                 # Check if x is even
# if x % 2 == 0:
# continue

#                                                                                                                          Exception & ErroR Handling

# use try and except blocks
# try = pass error code : except = catches the exception and executes the specified statements
# try block = try:
# except block = except(): => Continue execution, Multiple exceptions in one block,
# except(ValueError, ZeroDivisionError): / print("")
# Generic except block = Unknown exceptions: except: / print("")
# import random / from time import clock / random-int = random.randint(1, 100) / print random-int

#                                                                                                                              Exception
# def some_function():
# try:
# 10 / 0
# except ZeroDivisionError:
# print "Oops, invalid."
# else:
# pass
# finally:
# print "We're done with that."
# >>> some_function()
# Oops, invalid.
# We're done with that




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
# x = np.array ( [5,6,7] )
# y = np.array ( [2,3,8] )
# Result = x - y
# Result = np.subtract(x,y), add, divide, multiply, Exponentiation = exp(x), Square root = sqrt(x), Cosine = cos(b), Sine = sin(x)

#                                                                                                                               Sub-setting
# Fetching a single element out of an array by using the index values
# a = np.array([(1,2,3), (4,5,6)], type = int)
# a[0][1] \ O/P = 2
#                                                                                                                          $      Slicing
# a = np.array( [4,6,9] )
# a[0:2], a[a<2]

#                                                                                                                           Exercise Programs

#                                                                                                                           Convert Tuples to List
# Using list comprehension
#                                                                     # Python code to convert list of tuples into list
#                                                                              # List of tuple initialization
# lt = [('Geeks', 2), ('For', 4), ('geek', '6')]
#                                                 # using list comprehension
# out = [item for t in lt for item in t]
#                                                 # printing output
# print(out)
# Using itertools
#                                             # Python code to convert list of tuple into list
#                                                        # Importing
# import itertools
#                                        # List of tuple initialization
# tuple = [(1, 2), (3, 4), (5, 6)]
#                                                                                                                               # Using itertools
# out = list(itertools.chain(*tuple))
#                                                     # printing output
# print(out)
# Using iteration
#                                        # Python code to convert list of tuple into list
#                                        # List of tuple initialization
# tup = [(1, 2), (3, 4), (5, 6)]
#                                       # result list initialization
# result = []
# for t in tup:
#     for x in t:
#         result.append(x)
#                                             # printing output
# print(result)
# Using sum
#                                               # Python code to convert list of tuple into list
#                                                 # List of tuple initialization
# tup = [(1, 2), (3, 4), (5, 6)]
#                                                       # using sum function()
# out = list(sum(tup, ()))
#                                                 # printing output
# print(out)
# Using operator and reduce
#                                                         # Python code to convert list of tuple into list
# import operator
# from functools import reduce
#                                                            # List of tuple initialization
# tup = [(1, 2), (3, 4), (5, 6)]
#                                                               # printing output
# print(list(reduce(operator.concat, tup)))
#                                                                                                                                  Using lambda
#                                                          # List of tuple initialization
# tup = [(1, 2), (3, 4), (5, 6)]
#                                         # Using map for 0 index
# b = map(lambda x: x[0], tup)
#                                         # Using map for 1 index
# c = map(lambda x: x[1], tup)
#                                            # converting to list
# b = list(b)
# c = list(c)
#                                              # Combining output
# out = b + c
#                                             # printing output
# print(out)
#                                      Typecasting to tuple can be done by simply using                                        tuple(list_name).
#                                            # list into a tuple
# def convert(list):
#     return tuple(list)
#                                              # Driver function
# list = [1, 2, 3, 4]
# print(convert(list))
#                                                Output:
# (1, 2, 3, 4)
#                                                Approach #2 :
# A small variation to the above approach is to                                                                              use a loop inside tuple()
#                                               # list into a tuple
# def convert(list):
#     return tuple(i for i in list)
#                                                # Driver function
# list = [1, 2, 3, 4]
# print(convert(list))
#                                           Output:
# (1, 2, 3, 4)
# Approach #3 : Using (*list, )
#                                                   # Python3 program to                                                 convert a  list into a tuple
# def convert(list):
#     return (*list, )
#                                                          # Driver function
# list = [1, 2, 3, 4]
# print(convert(list))
#                                                      Output:
# (1, 2, 3, 4)

#                                                                                py code
# x = {1,2,4,4,5}
# x.add(5)
# x.add(6)
# print('x')
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
"""
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
"""
#
