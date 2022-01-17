# hi we are entering into one of the advanced concepts of python regular expressions
# the problem is to find the list of letters in a string
import re
pattern=re.compile(‘[a-d]’)
print(pattern.findall(“This is venkat from kaashiv infotech”))

——————————————
——————————————

pattern=re.compile(‘\d+’)
print(pattern.findall(“You can meet me at 11 am sharp or else at 12 pm sharp”))

——————————————
——————————————

variable=15
print(“The value of the data is %s”%variable) #implicit type conversion
print(“The value of the data is %d”%variable)
print(“The value of the data is %f”%variable)
print(“The value of the data is %r”%variable)

——————————————
——————————————

variable=int(’15’) #explicit type casting
print(“The value of the data is %d”%variable)

——————————————
——————————————

#create matrix
import numpy as np
matrix = np.array([[1, 4],
[2, 5]])

——————————————
——————————————

#Another way of Transposing the matrix
matrix=[(1,2,3),(4,5,6),(7,8,9),(10,11,12)]
for row in matrix:
print(row)
print(“\n”)
t_matrix = zip(*matrix)
for row in t_matrix:
print(row )

——————————————
——————————————

#Another way of Transposing the matrix
# Numpy transpose returns similar result when applied on 1D matrix
import numpy
matrix=[(1,2,3),(4,5,6),(7,8,9),(10,11,12)]
print(matrix)
print(“\n”)
print(numpy.transpose(matrix))

——————————————
——————————————

#Find rank of the matrix
np.linalg.matrix_rank(matrix)

——————————————
——————————————

# Return diagonal elements
# Create matrix
matrix = np.array([[1, 2, 3],
[4, 5, 6],
[7, 8, 9]])
matrix.diagonal()

——————————————
——————————————

# Calculate the trace of the matrix
matrix.diagonal().sum()

from sklearn import datasets
import matplotlib.pyplot as plt

# Load iris dataset
iris = datasets.load_iris()
#print(iris)
# Create feature matrix
X = iris.data

# View the first observation’s feature values
X
Y=iris.target
Y

lis = [2, 1, 3, 5, 4]

——————————————
——————————————

#in operator
if(4 in lis):
print(“the value is available in the list(IN condition)”)
#not in operator
if(4 not in lis):
print(“the value is not available in the list(NOT IN condition)”)
else:
print(“the value is available in the list(NOT IN condition)”)
# using len() to print length of list
print (“The length of list is : “, end=””)
print (len(lis))

——————————————
——————————————

# using min() to print minimum element of list
print (“The minimum element of list is : “, end=””)
print (min(lis))
——————————————
——————————————

# using max() to print maximum element of list
print (“The maximum element of list is : “, end=””)
print (max(lis))

——————————————
——————————————

#functions with variables pass by value… functions with parameters
def fun(message):
print(message)
fun(“Welcome to kaashiv infotech by venkat”)

——————————————
——————————————

#functions with variables pass by value… functions with parameters
def fun(name,age):
print(“The name of the student is ‘” + name +”‘ and the age is “+age)
fun(“venkat”,”26″)

——————————————
——————————————

#functions call with array of parameters
def fun(*field):
print(“The guy is good in ‘” + field[2])
fun(“venkat”,”26″,”Specialist in ML”) # 0 ,1, 2

——————————————
——————————————

def square(value):
return value*5
print(square(8))

——————————————
——————————————

# This function uses global variable s
def f():
#local scope
s=”Welcome to KaaShiv Infotech”
print (s)

# Global scope
s = “Venkat director of kaashiv infotech”
f()
print (s)

——————————————
——————————————

#parameters are not completely given.. partially given .. and dynamically added
from functools import partial

def fun(f,a,b,c):
return f*1000 + a *100 + b*10 + c # 4*1000 + 2*100 + 1*10 + 8
#4000 + 200 +10 + 8

g = partial(fun,4,2,1)

print(g(8))

——————————————
——————————————

#parameters are not completely given.. partially given .. and dynamically added
from functools import partial

def fun(a,b,c,d):
return a*1000 + b *100 + c*10 + d # 4*1000 + 2*100 + 1*10 + 8
#4000 + 200 +10 + 8

g = partial(fun,4,2,1)

print(g(8))

——————————————
——————————————

#parameters are not completely given.. partially given .. and dynamically added
from functools import partial

def fun(a,b,c,d):
return a*1000 + b *100 + c*10 + d # 8*1000 + 4*100 + 2*10 + 1
#8000 + 400 +20 + 1

g = partial(fun,b=4,c=2,d=1)

print(g(8))

——————————————
——————————————

from functools import partial

def fun(a,b,c,d):
return a*1000 + b *100 + c*10 + d # 8*1000 + 4*100 + 2*10 + 1
#8000 + 400 +20 + 1

g = partial(fun,a=4,b=2,c=1)

print(g(d=8))

——————————————
——————————————

# A Python program to demonstrate need
# of packing and unpacking

# A sample function that takes 4 arguments
# and prints them.
def fun1(a, b, c, d):
print(a, b, c, d)

# Driver Code
my_list = [1, 2, 3, 4]

# unpacking list
fun1(*my_list)

——————————————
——————————————

# A sample program to demonstrate unpacking of
# dictionary items using **
def fun(a, b, c):
print(a, b, c)

# A call with unpacking of dictionary
d = {‘a’:2, ‘b’:4, ‘c’:10}
fun(**d)

#################################Remove Missing Values#############

# Load library
import numpy as np
import pandas as pd
# Create feature matrix
X = np.array([[1, 2],
[6, 3],
[8, 4],
[9, 5],
[np.nan, 4]])
# Load data as a data frame
df = pd.DataFrame(X, columns=[‘feature_1’, ‘feature_2’])

# observations
df

# Remove observations with missing values
df.dropna()

################################# Create Data Frame #############

# Import required packages
from sklearn import preprocessing
import pandas as pd

raw_data = {‘patient’: [1, 1, 1, 2, 2],
‘obs’: [1, 2, 3, 1, 2],
‘treatment’: [0, 1, 0, 1, 0],
‘score’: [‘strong’, ‘weak’, ‘normal’, ‘weak’, ‘strong’]}
df = pd.DataFrame(raw_data, columns = [‘patient’, ‘obs’, ‘treatment’, ‘score’])

# Create a label (category) encoder object
le = preprocessing.LabelEncoder()

# Fit the encoder to the pandas column
le.fit(df[‘score’])

# View the labels (if you want)
list(le.classes_)

# Apply the fitted encoder to the pandas column
le.transform(df[‘score’])

#################################Preprocessing Iris Data#############

from sklearn import datasets
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
# Load the iris data
iris = datasets.load_iris()

# Create a variable for the feature data
X = iris.data

# Create a variable for the target data
y = iris.target

iris

# Random split the data into four new datasets, training features, training outcome, test features,
# and test outcome. Set the size of the test data to be 30% of the full dataset.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

############# Encoding Ordinal Categorical Features #########

# Load library
import pandas as pd
# Create features
df = pd.DataFrame({‘Score’: [‘Low’,
‘Low’,
‘Medium’,
‘Medium’,
‘High’]})

# View data frame
df

# Create mapper
scale_mapper = {‘Low’:1,
‘Medium’:2,
‘High’:3}

# Map feature values to scale
df[‘Scale’] = df[‘Score’].replace(scale_mapper)

# View data frame
df

############# Handling Outliers #########

# Load library
import pandas as pd

# Create DataFrame
houses = pd.DataFrame()
houses[‘Price’] = [534433, 392333, 293222, 4322032]
houses[‘Bathrooms’] = [2, 3.5, 2, 116]
houses[‘Square_Feet’] = [1500, 2500, 1500, 48000]

houses

houses = pd.DataFrame(
{
‘Price’ : [534433, 392333, 293222, 4322032],
‘Bathrooms’ : [2, 3.5, 2, 116],
‘Square_Feet’ : [1500, 2500, 1500, 48000]
}
)
houses

# Drop observations greater than some value
houses[houses[‘Bathrooms’] < 20]

# Load library
import numpy as np

# Create feature based on boolean condition
houses[‘Outlier’] = np.where(houses[‘Bathrooms’] < 20, 0, 1)

# Show data
houses

# Log feature
houses[‘Log_Of_Square_Feet’] = [np.log(x) for x in houses[‘Square_Feet’]]

# Show data
houses

###Discretize Features#######

############# Binarization is the process of transforming data
############# features of any entity into vectors of binary numbers
############# to make classifier algorithms more efficient.
############# In a simple example, transforming an image’s gray-scale
############# from the 0-255 spectrum to a 0-1 spectrum is binarization.
############# Binarization is the process of transforming data features of
############# any entity into vectors of binary numbers to make classifier
############# algorithms more efficient. In a simple example,
############# transforming an image’s gray-scale from the 0-255 spectrum
############# to a 0-1 spectrum is binarization. #########

# Load libraries
from sklearn.preprocessing import Binarizer
import numpy as np

# Create feature
age = np.array([[6],
[12],
[20],
[36],
[65]])

# Create binarizer
binarizer = Binarizer(35)

# Transform feature
binarizer.fit_transform(age)

# Bin feature
np.digitize(age, bins=[5,20,90])

——————————————
——————————————

OOPS Concept – Class Object Concepts

——————————————
——————————————

class venkatclass:

def venkatfun(self):
print (“This is venkat function available in the class Access it from the object”)

venkatObj = venkatclass()
venkatObj.venkatfun()

——————————————
——————————————

class venkatclass:

def venkatfun(self):
print (“This is venkat function available in the class Access it from the object”)
def venkatfun1(self):
print (“This is venkat function1 available in the class Access it from the object”)

venkatObj = venkatclass()
venkatObj.venkatfun()
venkatObj.venkatfun1()

——————————————
——————————————

## __init__ is the constructor
class venkatclass:
def __init__(self,name):
self.name= name
def venkatfun(self):
print(“The given name along with object creation is ” + self.name)

venkatObj = venkatclass(“venkat”)
venkatObj.venkatfun()

——————————————
——————————————

## __init__ is the constructor
class venkatclass:
def __init__(self,a,b):
self.a= a
self.b= b
def venkatfun(self):
print(“The sum of the values are ” + str(self.a + self.b))

venkatObj = venkatclass(10,20)
venkatObj.venkatfun()

——————————————
——————————————

Inheritance in Python

——————————————
——————————————

class FatherClass: ##base class
def venkatFatherFun(self):
print(“Father class Accessed”)

class ChildClass(FatherClass): ##child class
def venkatChildFun(self):
print(“Child class Accessed”)
#Simple inheritance one father to one child
venkatChildObject = ChildClass()
venkatChildObject.venkatChildFun()
venkatChildObject.venkatFatherFun() #create child object and access father methods

——————————————
——————————————

class FatherClass: ##base class
def _venkatFatherFun_(self):
print(“Father class Accessed”)

class ChildClass(FatherClass): ##child class
def venkatChildFun(self):
print(“Child class Accessed”)
#Simple inheritance one father to one child
venkatChildObject = ChildClass()
venkatChildObject.venkatChildFun()

venkatFatherObject = FatherClass()
venkatFatherObject._venkatFatherFun_() #create child object and access father methods

——————————————
——————————————

class FatherClass: ##base class
def _venkatFatherFun_(self):
print(“Father class Accessed”)

class ChildClass(FatherClass): ##child class
def venkatChildFun(self):
print(“Child class Accessed”)
#Simple inheritance one father to one child
venkatChildObject = ChildClass()
venkatChildObject.venkatChildFun()

venkatChildObject._venkatFatherFun_() #create child object and access father methods

——————————————
——————————————

class FatherClass: ##base class
def __venkatFatherFun__(self):
print(“Father class Accessed”)

class ChildClass(FatherClass): ##child class
def venkatChildFun(self):
print(“Child class Accessed”)
#Simple inheritance one father to one child
venkatChildObject = ChildClass()
venkatChildObject.venkatChildFun()

venkatChildObject.__venkatFatherFun__() #create child object and access father methods

——————————————
——————————————

class FatherClass: ##base class
def venkatFatherFun(self):
print(“Father class Accessed”)

class ChildClass(FatherClass): ##child class
def venkatChildFun(self):
print(“Child class Accessed”)

class GrandChildClass(ChildClass): ##Grand child class
def venkatGrandChildFun(self):
print(“GrandChild class Accessed”)

venkatGrandChildObject = GrandChildClass()
venkatGrandChildObject.venkatGrandChildFun()
venkatGrandChildObject.venkatChildFun()
venkatGrandChildObject.venkatFatherFun()

——————————————
——————————————

Try Catch in Python

#program to dynamically get input values
a = int(input(‘Enter the value of a’))
b = int(input(‘Enter the value of b’))
c=a/b
print(“The value of c is ” + str(c))

——————————————
——————————————

#no error while running .. no compilation error…
try:
a = int(input(‘Enter the value of a’))
b = int(input(‘Enter the value of b’))
c=a/b
print(“The value of c is ” + c)
except:
print(“We received the run time error”)
#got a run time error and it is handled clearly using try except loop

——————————————
——————————————

#no error while running .. no compilation error…
try:
a = int(input(‘Enter the value of a’))
b = int(input(‘Enter the value of b’))
c=a/b
print(“The value of c is ” +str( c))
except:
print(“We received the run time error”)
else:
print(“After a valid works this else loop will work”)

——————————————
——————————————

# Handling specific error
try:
a = int(input(‘Enter the value of a’))
if a>10:
print(“Valid data”)
else:
raise ValueError

except ValueError:
print(“Machi there is a big issue with data”)
