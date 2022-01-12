#                                                          Projects
#                                                 The Data Analysis Process
""" Problem definition
    Data extraction
    Data cleaning
    Data transformation
    Data exploration
    Predictive modeling
    Model validation/test
    Visualization and interpretation of results
    Deployment of the solution"""

# Dictionary = {5:1, 6:9}, Data & Array = ['1,2,3']

#  Mean, Variance, propability mass Function
from numpy.char import index
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
values={
    'batsman' : ['Abith','Arun', '619','Raj'],
    'score' : [10,20,30,40]
}
#                                                                                         calculate the mean of data
df = pd.DataFrame(values)
df['score'].mean()
#                                                    Triming the data
stats.trim_mean(df['score'],propotiontocut=0.2)
stats.trimboth(df['score'],proportiontocut=0.2).mean()  # trims 20% data in boh sides
#                                     tail = trim1
stats.trim1(df['score'],proportiontocut=0.2,tail='right')
stats.trim1(df['score'],proportiontocut=0.2,tail='right').mean()

#                                                                                          propability mass Function
data=[3,2,1,6,5,619,4,8,9,7,4,65,1,]
count={}
for values in data :
    count[values]=count.get(values,0)+1
for observation in data:
    count[observation]=count.get(observation,0)+1  # looping in count of values
count  #                                                 count unique values
n=len(data)  #                                         count the length of data
probability_mass_function={}
for unique_variable,count in count.items():
    probability_mass_function[unique_variable]=count/n
probability_mass_function
plt.bar(list(probability_mass_function.keys()), probability_mass_function.values(),color='g')
#                                                                   encryption(+) & Decryption(-)
alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = 4
newmsg = ' '
message=input('Enter the Message : ')
for character in message:
    position = alphabet.find(character)
    newposition = (position+key)%26      #   (-) for decryption
    newchar = alphabet[newposition]
    print("Encrypted new character is ",newchar)
    newmsg+=newchar
print("the encrypted final message is ", newmsg)
#                                                                       GUI-Based project using Tkinter
#          basic-Code
from tkinter import *
from typing import Sized
top=Tk()                                          # main class
L1=Label(top,text="UserName")                     # top = area
L1.grid(column=0,row=0)                           # grid = window

E1=Entry(top,bd=5) # text box
E1.grid(column=1,row=0)
E2=Entry(top,bd=5)                                # border = 5
E2.grid(column=2,row=0)
def submit():
    messagebox.showinfo( "CONFIRMATION",E1.get()+"-Your Data")     # def messagebox
redbutton=Button(top,text="Abith Button",fg="red" ,command=submit) # colorbutton, to call this function click this button
redbutton.grid(column=1,row=1)
top.mainloop()
#                                                            To get the Staticstical data
import pandas as pd
import quandl
df = quandl.get("WIKIPEDIA/GOOGL")
print(df.head())

#                                                                                                                       Numpy - Basic Opeartions
#                                                  Arithmetic Operators
a = np.arange(4)      # O/p = array([0, 1, 2, 3])
a
a+4
a*2
b = np.arange(4,8) # b = array([4, 5, 6, 7])
np.sin(b)          # array([–0.        , –0.95892427, –0.558831  ,  1.9709598 ])
a * np.sqrt(b)     # array([ 0.        ,  2.23606798,  4.89897949,  7.93725393])
A = np.arange(0, 9).reshape(3, 3)      # Multi-Dimensional
B = np.ones((3, 3))
np.dot(A,B)        # Dot product
A.dot(B)
np.dot(B,A)
#                                               Increment and Decrement Operators
a = np.arange(4) # o/p = array([0, 1, 2, 3])
a += 1           # o/p = array([1, 2, 3, 4])
a -= 1           # o/p = array([0, 1, 2, 3])
#                                                     Universal Functions (ufunc)
np.sqrt(a)
np.sin(a)
np.log(a)
#                                                          Aggregate Functions
# the sum of all the elements in an array is an aggregate function
a = np.array([3.3, 4.5, 1.2, 5.7, 0.3])
a.sum()
a.min()
a.max()
a.mean()
a.std()
#                                                                                                 Indexing, Slicing, and Iterating
#                                                      indexing = [,,]
a = np.arange(10, 16) # array([10, 11, 12, 13, 14, 15])
a[4,-1]
#                                                       Slicing
# extract portions of an array to generate new ones (copies)
# arrays are views onto the same underlying buffer
# sequence of numbers separated by colons (‘:’) within the square brackets
a = np.arange(10, 16)
# array([10, 11, 12, 13, 14, 15])
a[1:5] # array([11, 12, 13, 14])
# extract from the previous portion an item, skip a specific number of following items, then extract the next, and skip again ...,
# you can use a third number that defines the gap in the sequence of the elements between one element and the next one to take. 
# For example, with a value of 2, the array will take the elements in an alternating fashion.
a[1:5:2] # array([11, 13])
a[1:5] # Out[8]: array([11, 12, 13, 14])
# to extract from the previous portion an item, skip a specific number of following items, then extract the next, and skip again 
a[1:5:2] # Out[9]: array([11, 13])
a[::2]   # Out[10]: array([10, 12, 14])
a[:5:2]  # Out[11]: array([10, 12, 14])
a[:5:]   # Out[13]: array([10, 11, 12, 13, 14])
A = np.arange(10, 19).reshape((3, 3))
A[0,:]   # Out[16]: array([10, 11, 12]), selects only columns
A[:,0]   # array([10, 13, 16])
# if you want to extract a smaller matrix then you need to explicitly define all intervals with indexes that define them.
A[0:2, 0:2]  # array([[10, 11],
#                    [13, 14]])
#                                  array of indexes
A[[0,2], 0:2] # array([[10, 11],
#                     [16, 17]])

#                                                                                               Numpy - Conditions & Boolean Arrays
# indexes in a numerical form. An alternative way to perform the selective extraction of the elements in an array is to use the conditions and Boolean operators.
# making selections of parts of arrays
A = np.random.random((4, 4))
A < 0.5 # all the positions in which the values are less than 0.5.
A[A < 0.5]  # obtain a new array

#                                                                                        Numpy - General/Advanced concepts
# difference between copies and views will be illustrated especially when they return values
#                                                                       functions of NumPy
#                                           Copies or Views of Objects 
# 
a = np.array([1, 2, 3, 4])
b=a
b #                                     return value either a copy or a view of the array
a[2]=0
c = a[0:2]  # the object returned is only a view of the original array
a[0] = 0
#             to generate a complete copy and distinct array you can use the copy() function
c = a.copy()
c
a[0] = 0
c

#                                                                          Vectorization
#  absence of explicit loop during the developing of the code
# more concise and readable code, and you can say that it will appear more “Pythonic”
# many operations take on a more mathematical expression
#                                                                          Broadcasting
# allows an operator or a function to act on two or more arrays to operate even if these arrays do not have exactly the same shape
# classify multidimensional arrays through the shape that is a tuple representing the length of the elements for each dimension
# #  two arrays may be subjected to broadcasting when all their dimensions are compatible
A = np.arange(16).reshape(4, 4)
b = np.arange(4)
A #                                                    4*4 Array
b # 4*0 Array
#  add a 1 to each missing dimension, 4 x 44 x 1The rule of compatibility is met
# the missing elements (size, length 1) are filled with replicas of the values contained in extended sizes
# the two arrays have the same dimensions, the values inside may be added together
A + b 
m = np.arange(6).reshape(3, 1, 2) # two arrays have different shapes but each of them is smaller than the other only for some dimensions
n = np.arange(6).reshape(3, 2, 1)
m + n # addition operator between the two arrays, operating  element-wise
#                                                                                                   Structured Arrays
# This type of array contains structs or records instead of the individual items
# Specify a list of comma-separated specifiers to indicate the elements that will constitute the struct, along with its data type and order
"""bytes                 b1
int                   i1, i2, i4, i8
unsigned ints         u1, u2, u4, u8
floats                f2, f4, f8
complex               c8, c16
fixed length strings  a"""
#                                         three types of data in the dtype 
structured = np.array([(1, 'First', 0.5, 1+2j),(2, 'Second', 1.3, 2-2j),
(3, 'Third', 0.8, 1+3j)],dtype=('i2, a6, f4, c8'))>>> structuredarray([(1, 'First', 0.5, (1+2j)),
(2, 'Second', 1.2999999523162842, (2-2j)),
(3, 'Third', 0.800000011920929, (1+3j))],
dtype=[('f0', '
#                                        data type explicitly specifying int8, uint8, float16, complex64,
structured = np.array([(1, 'First', 0.5, 1+2j),(2, 'Second', 1.3,2-2j),
(3, 'Third', 0.8, 1+3j)],dtype=('int16, a6, float32, complex64'))
structured
#                 3 rd Type
structured
array([(1, 'First', 0.5, (1+2j)),
(2, 'Second', 1.2999999523162842, (2-2j)),
(3, 'Third', 0.800000011920929, (1+3j))],
dtype=[('f0', '
structured[1](2, 'Second', 1.2999999523162842, (2-2j)) # reference index, obtain the corresponding row which contains the struct
# refer to all the elements of the same type, or of the same ‘column'
structured['f1']
array(['First', 'Second', 'Third'],dtype='|S6')
# specify the names with something more meaningful, progressive integer that indicates the position in the sequence.
structured = np.array([(1,'First',0.5,1+2j),(2,'Second',1.3,2-2j),(3,'Third',0.8,1+3j)],
dtype=[('id','i2'),('position','a6'),('value','f4'),('complex','c8')])
# Redefining the tuples of names assigned to the dtype attribute of the structured array
structured.dtype.names = ('id','order','value','complex')
# use meaningful names for the various types of fields
structured['order']
array(['First', 'Second', 'Third'],
dtype='|S6')
#                                                                        Array Manipulation
#                                     Joining Arrays
# stacking, providing a number of functions 
A = np.ones((3, 3))
B = np.zeros((3, 3))
np.vstack((A, B)) # vertical stacking with the vstack() function, second array as new rows of the first array.
np.hstack((A,B)) #  the hstack() function performs horizontal stacking, second array is added to the columns of the first array
a = np.array([0, 1, 2])
b = np.array([3, 4, 5])
c = np.array([6, 7, 8])
np.column_stack((a, b, c))
np.row_stack((a, b, c))
#                                  Splitting Arrays
# horizontally with the hsplit() function and vertically with the vsplit() function.
A = np.arange(16).reshape((4, 4))
A
[B,C] = np.hsplit(A, 2) # width of the array divided into two parts
B    #                   4x4, 2x4
C
#  height of the array divided into two parts, 4x4, 4x2
[B,C] = np.vsplit(A, 2)
B
C
# divide the matrix into three parts
lso includes the functionalities of the vsplit() and hsplit() functions.
[A1,A2,A3] = np.split(A,[1,3],axis=1)  # split by column
[A1,A2,A3] = np.split(A,[1,3],axis=0) # split by row

#                                                           Read Write Array Data on Files
#                                           Loading and Saving Data in Binary Files(Format)
# save() function, specifying as arguments the name of the file, to which .npyextension will be automatically added
np.save('saved_data',data)
# recover the data stored within a .npy file, you can use the load() function
loaded_data = np.load('saved_data.npy')
#                                                       Reading File with Tabular Data
# column headings have become the names of the field.
# two loops: the first reads a line at a time, and the second separates and converts the values contained in it,
# genfromtxt() function replaces the blanks in the file with nan values
data = np.genfromtxt('data.csv', delimiter=',', names=True)
#                                                                       Iterating an Array
# apply an iteration to apply a function on the rows or on the columns or on an individual item
# launch an aggregate function that returns a value calculated for every single column or on every single row = apply_along_axis()
# apply_along_axis() = 3args = the aggregate function, the axis, the array
# if the axis equals 0, then the iteration evaluates the elements column by column
# if the axis equals 1 then the iteration evaluates the elements row by row
for i in a:
    print(i)
# to make an iteration element by element use the for loop on A.flat
for item in A.flat:
    print(item)
#                                                                        apply_along_axis()
np.apply_along_axis(np.mean, axis=0, arr=A) # array([13., 14., 15.])
np.apply_along_axis(np.mean, axis=1, arr=A) # array([11., 14., 17.])
# using a ufunc is how to perform one iteration element-by-element.
# iteration both by column and by row
def foo(x):
    return x/2
np.apply_along_axis(foo, axis=1, arr=A)
np.apply_along_axis(foo, axis=1, arr=A) # same o/p

# Create Vector, matrix, Dot product
# calculating the impact of an environment with object using vector directions
vector_a = np.array([1, 2, 3])
vector_b = np.array([3, 4, 5])
#                                            calculate dot product of vectors
np.dot(vector_a,vector_b) # o/p = 26
vector_a @ vector_b  #    # o/p = 26
#                                                                                          create a matrix
matrix = np.array(
    [
        [0, 4, 7],
        [2, 5, 8],
        [6, 1, 9]
    ]
)
matrix[1, 1] # o/p = 5
matrix.T     #  o/p = array([[1, 2],
#                          [4, 5]])
for i in matrix:
    print(i)
    matrix_transpose = zip(*matrix) # * = taking the value of the matrix
    print(matrix_transpose)
    for i in matrix_transpose:
        print(i)
# o/p = [1 4] /n <zip object at 0x7f666d354400> /n (1, 2) /n (4, 5) /n [2 5] /n <zip object at 0x7f666dea2880> /n (1, 2) /n (4, 5)
print(np.transpose(matrix))
#                                                     to find the rank of the matrix
np.linalg.matrix_rank(matrix)   # o/p = 2
#                                                           return diagonal elements
matrix.diagonal()
#                                                          calculate the trace of matrix
matrix.diagonal().sum()
#                                                              return minimum element
np.min(matrix)
np.max(matrix)  #                                                 return maximum element
#                                                        find maximum element in each row 
np.max(matrix, axis=0)
#                                                       find maximum element in each column
np.max(matrix, axis=1)
#                                                            return determinant of matrix
np.linalg.det(matrix)
#                                                                 return mean of matrix
np.mean(matrix)
#                                                              return standard deviation of matrix
np.std(matrix)
#                                                                 add & subtract two matrix
np.add(matrix_a,matrix_b)
np.subtract(matrix_a,matrix_b)
#                                                              find the variance of the matrix
np.var(matrix)



#                                                                                                                        Extract features from Dictionary
import Numpy as np
import pandas as pd
from sklearn.feature_extraction import DictVectorizer  # Import Library

staff = [{'Name': 'Abith Raj', 'age': 33}]          # create Dictionary
vec = DictVectorizer()                              # convert Dict to feature Object
vec.fit_transform(staff).toarray()                  # Fit then transform the Dict with vec,then
vec.get_feature_names()                             # View Feature names

#                                                      Creating a Chart
x = np.arange(0,10) 
y = x ^ 2 
#                                                          Simple Plot
plt.plot(x,y)

#                                                   Labling the Axes
x = np.arange(0,10) 
y = x ^ 2 
#                                                  Labeling the Axes and Title
plt.title("Graph Drawing") 
plt.xlabel("Time") 
plt.ylabel("Distance") 
#                                                  Simple Plot
plt.plot(x,y)

#                                           Formatting Line type and Colour
x = np.arange(0,10) 
y = x ^ 2 
#                                   Labeling the Axes and Title
plt.title("Graph Drawing") 
plt.xlabel("Time") 
plt.ylabel("Distance") 
#                                     Formatting the line colors
plt.plot(x,y,'r')
#                                  Formatting the line type  
plt.plot(x,y,'>')

#                                                                                        Saving the Chart File
x = np.arange(0,10) 
y = x ^ 2 
#                      Labeling the Axes and Title
plt.title("Graph Drawing") 
plt.xlabel("Time") 
plt.ylabel("Distance") 

#                           Formatting the line colors
plt.plot(x,y,'r')

#                             Formatting the line type  
plt.plot(x,y,'>') 

#                                  save in pdf formats
plt.savefig('timevsdist.pdf', format='pdf')

#                                                                                           Chart Styling
#                                                                         Annotations 
x = np.arange(0,10) 
y = x ^ 2 
z = x ^ 3
t = x ^ 4 
# Labeling the Axes and Title
plt.title("Graph Drawing") 
plt.xlabel("Time") 
plt.ylabel("Distance") 
plt.plot(x,y)

#                            Annotate
plt.annotate(xy=[2,1], s='Second Entry') 
plt.annotate(xy=[4,6], s='Third Entry')

#                                                    Adding Legends
# Whenever you create a chart in Excel, a legend for the chart is automatically generated at the same time. 
x = np.arange(0,10) 
y = x ^ 2 
z = x ^ 3
t = x ^ 4 
#                                            Labeling the Axes and Title
plt.title("Graph Drawing") 
plt.xlabel("Time") 
plt.ylabel("Distance") 
plt.plot(x,y)
#                                              Annotate
plt.annotate(xy=[2,1], s='Second Entry') 
plt.annotate(xy=[4,6], s='Third Entry') 
#                                                 Adding Legends
plt.plot(x,z)
plt.plot(x,t)
plt.legend(['Race1', 'Race2','Race3'], loc=4)

#                                                                        Chart presentation Style
# Pedigree Chart Templates = PPT
#                                                      Style the background
plt.style.use('fast')
plt.plot(x,z)

#                                                            Heatmap
# heatmap contains values representing various shades of the same colour for each value to be plotted as a matrix of values
#                                                 two-dimensional plot of values which are mapped to the indices and columns
data=[{2,3,4,1},{6,3,5,2},{6,3,5,4},{3,7,5,4},{2,8,1,5}]
Index= ['I1', 'I2','I3','I4','I5']
Cols = ['C1', 'C2', 'C3','C4']
df = DataFrame(data, index=Index, columns=Cols)
plt.pcolor(df)
plt.show()

#                                                                                               Bubble Charts - 3D 
# display three variables without using 3D graphs;
#                                                            Drawing a Bubble Chart
DataFrame.plot.scatter()
#                               create data
x = np.random.rand(40)
y = np.random.rand(40)
z = np.random.rand(40)
colors = np.random.rand(40) 
#                                        use the scatter function
plt.scatter(x, y, s=z*1000,c=colors)
plt.show()

#                                                              scatter plot, scatter graph, and correlation
#           x = Independent, y = Dependent
df = pd.DataFrame(np.random.rand(50, 4), columns=['a', 'b', 'c', 'd'])
df.plot.scatter(x='a', y='b') 

#                                                                                                              3D Charts
# 3dPlot is drawn by mpl_toolkits.mplot3d to add a subplot to an existing 2d plot.
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt

chart = plt.figure()
chart3d = chart.add_subplot(111, projection='3d')
#                                                                   Create some test data.
X, Y, Z = axes3d.get_test_data(0.08)
#                                                                      Plot a wireframe.
chart3d.plot_wireframe(X, Y, Z, color='r',rstride=15, cstride=10)
plt.show()

#                                                                      Time Series
# take the value of stock prices every day for a quarter for a particular stock symbol.
# We capture these values as a csv file and then organize them to a dataframe 
# set the date field as index of the dataframe by recreating the additional Valuedate column as index and deleting the old valuedate column
# sample data for the price of the stock on different days of a given quarte
"""valueDate	Price
01-01-2018,	1042.05
02-01-2018,	1033.55
03-01-2018,	1029.7
04-01-2018,	1021.3
05-01-2018,	1015.4
...
...                        # save as stock.csv
...
...
23-03-2018,	1161.3
26-03-2018,	1167.6
27-03-2018,	1155.25
28-03-2018,	1154"""

#                                                                 Adding Further Elements to the Chart
#                                    Adding Text
ipython qtconsole
import matplotlib.pyplot as plt
plt.axis([0,5,0,20])
plt.title('My first plot')
plt.xlabel('Counting')
plt.ylabel('Square values')
plt.plot([1,2,3,4],[1,4,9,16],'ro')
# changing the font and increasing the size of the characters. Also you can modify the color of the axis labels
plt.axis([0,5,0,20])
plt.title('My first plot',fontsize=20,fontname='Times New Roman')
plt.xlabel('Counting',color='gray')
plt.ylabel('Square values',color='gray')
plt.plot([1,2,3,4],[1,4,9,16],'ro')
# text().text(x,y,s, fontdict=None, **kwargs)
# coordinates of the four points of the plot shifted slightly on the y axis
plt.axis([0,5,0,20])
plt.title('My first plot',fontsize=20,fontname='Times New Roman')
plt.xlabel('Counting',color='gray')
plt.ylabel('Square values',color='gray')
plt.text(1,1.5,'First')
plt.text(2,4.5,'Second')
plt.text(3,9.5,'Third')
plt.text(4,16.5,'Fourth')
plt.plot([1,2,3,4],[1,4,9,16],'ro')
# to integrate LaTeX expressions allowing you to insert mathematical expressions within the chart.
plt.axis([0,5,0,20])
plt.title('My first plot',fontsize=20,fontname='Times New Roman')
plt.xlabel('Counting',color='gray')
plt.ylabel('Square values',color='gray')
plt.text(1,1.5,'First')
plt.text(2,4.5,'Second')
plt.text(3,9.5,'Third')
plt.text(4,16.5,'Fourth')
plt.text(1.1,12,r'$y = x^2$',fontsize=20,bbox={'facecolor':'yellow','alpha':0.2})
plt.plot([1,2,3,4],[1,4,9,16],'ro')
#                                  Adding a Grid
plt.axis([0,5,0,20])
plt.title('My first plot',fontsize=20,fontname='Times New Roman')
plt.xlabel('Counting',color='gray')
plt.ylabel('Square values',color='gray')
plt.text(1,1.5,'First')
plt.text(2,4.5,'Second')
plt.text(3,9.5,'Third')
plt.text(4,16.5,'Fourth')
plt.text(1.1,12,r'$y = x^2$',fontsize=20,bbox={'facecolor':'yellow','alpha':0.2})...: plt.grid(True)
plt.plot([1,2,3,4],[1,4,9,16],'ro')
#                                         Adding a Legend
plt.axis([0,5,0,20])
plt.title('My first plot',fontsize=20,fontname='Times New Roman')
plt.xlabel('Counting',color='gray')
plt.ylabel('Square values',color='gray')
plt.text(2,4.5,'Second')
plt.text(3,9.5,'Third')
plt.text(4,16.5,'Fourth')
plt.text(1.1,12,'$y = x^2$',fontsize=20,bbox={'facecolor':'yellow','alpha':0.2})
plt.grid(True)
plt.plot([1,2,3,4],[1,4,9,16],'ro')
plt.legend(['First series'])
#                                  move the legend in the upper-left corner
"""Location Code            Location String
--------------------------------------------------------
0                               best
1                               upper-right
2                                upper-left
3                              lower-right
4                               lower-left
5                                   right    
6                                center-left
7                                center-right
8                               lower-center
9                                upper-center
10                                   center"""
# correspond to the order of the text labels passed as argument to the legend() function.
import matplotlib.pyplot as plt
plt.axis([0,5,0,20])
plt.title('My first plot',fontsize=20,fontname='Times New Roman')
plt.xlabel('Counting',color='gray')
plt.ylabel('Square values',color='gray')
plt.text(1,1.5,'First')
plt.text(2,4.5,'Second')
plt.text(3,9.5,'Third')
plt.text(4,16.5,'Fourth')
plt.text(1.1,12,'$y = x^2$',fontsize=20,bbox={'facecolor':'yellow','alpha':0.2})
plt.grid(True)
plt.plot([1,2,3,4],[1,4,9,16],'ro')
plt.plot([1,2,3,4],[0.8,3.5,8,15],'g^')
plt.plot([1,2,3,4],[0.5,2.5,4,12],'b*')
plt.legend(['First series','Second series','Third series'],loc=2)
#                                                                                 Saving_charts
%save my_first_chart 171
# 
import matplotlib.pyplot as plt
plt.axis([0,5,0,20])
plt.title('My first plot',fontsize=20,fontname='Times New Roman')
plt.xlabel('Counting',color='gray')
plt.ylabel('Square values',color='gray')
plt.text(1,1.5,'First')
plt.text(2,4.5,'Second')
plt.text(3,9.5,'Third')
plt.text(4,16.5,'Fourth')
plt.text(1.1,12,'$y = x^2$',fontsize=20,bbox={'facecolor':'yellow','alpha':0.2})
plt.grid(True)
plt.plot([1,2,3,4],[1,4,9,16],'ro')
plt.plot([1,2,3,4],[0.8,3.5,8,15],'g^')
plt.plot([1,2,3,4],[0.5,2.5,4,12],'b*')
plt.legend(['First series','Second series','Third series'],loc=2)
#                                                                 Reload Saved Chart
ipython qtconsole --matplotlib inline -m my_first_chart.py
%load my_first_chart.py
%run my_first_chart.py # To run during a session
#                                         Saving Your Chart Directly as an Image
# This file will be named my_chart.png containing the image of your chart
plt.axis([0,5,0,20])
plt.title('My first plot',fontsize=20,fontname='Times New Roman')
plt.xlabel('Counting',color='gray')
plt.ylabel('Square values',color='gray')
plt.text(1,1.5,'First')
plt.text(2,4.5,'Second')
plt.text(3,9.5,'Third')
plt.text(4,16.5,'Fourth')
plt.text(1.1,12,'$y = x^2$',fontsize=20,bbox={'facecolor':'yellow','alpha':0.2})
plt.grid(True)
plt.plot([1,2,3,4],[1,4,9,16],'ro')
plt.plot([1,2,3,4],[0.8,3.5,8,15],'g^')
plt.plot([1,2,3,4],[0.5,2.5,4,12],'b*')
plt.legend(['First series','Second series','Third series'],loc=2)
plt.savefig('my_chart.png')
#                                                                                           Pandas - Data Structures
# 2 Types = Series, DataFrame
#                                             The Series
# Object, 1-D data structures, Index & Value
#                                             Declaring a Series
s = pd.Series([12,-4,7,9]) # dtype: int64
#  pandas will assign numerical values increasing from 0 as labels
s = pd.Series([12,-4,7,9], index=['a','b','c','d'])
s.values /n s.index # to see the array
# specify the label 
s['b'] # Label
s[0:2] # index
# specifying the list of labels within an array
s[['b','c']]
#                                                                  Assigning Values to the Elements
s[1] = 0 # by selecting index
s['b'] = 1 # Label
#                          Defining Series from NumPy Arrays
arr = np.array([1,2,3,4])
s3 = pd.Series(arr)
s4 = pd.Series(s)
arr[2] = -2
#                             Filtering Values
s[s > 8]
# DataFrame = index + Columns
data = {
    'color' : ['blue','green','yellow','red','white'],
    'object' : ['ball','pen','pencil','paper','mug'],
    'price' : [1.2,1.0,0.6,0.9,1.7]}
frame = pd.DataFrame(data)    # specify a sequence of columns
frame2 = pd.DataFrame(data, columns=['object','price']) # sequence regardless of how they are contained within the object dict
#  to assign labels to the indexes of a DataFrame, you have to use the index option assigning it
frame2 = pd.DataFrame(data, index=['one','two','three','four','five'])
#                                                                                    define within the constructor = 3 Args
# a data matrix, then an array containing the labels assigned to the index option, 
# and finally an array containing the names of the columns assigned to the columns option
frame3 = pd.DataFrame(np.arange(16).reshape((4,4)),
index=['red','blue','yellow','white'],
columns=['ball','pen','pencil','paper'])
#                                                                Selecting Elements
frame.columns
Index([u'colors', u'object', u'price'], dtype='object')
#                                      to get the list of indexes, specify the index attribute
frame.index
Int64Index([0, 1, 2, 3, 4], dtype='int64')
# get the entire set of data using the values attribute.
frame.values
array([['blue', 'ball', 1.2],
['green', 'pen', 1.0],
['yellow', 'pencil', 3.3],
['red', 'paper', 0.9],
['white', 'mug', 1.7]], dtype=object)
#                             select only the contents of a column
frame['price']
#                         ix attribute with the index value of the row that you want to extract
frame.ix[2]
frame.ix[[2,4]] # an array with the sequence of rows to insert
frame[0:1] # Extract a portion of a DataFrame, 
frame[1:3] # more than one line
# to achieve is a single value within a DataFrame
frame['object'][3]
#                                                 Assigning Values
# assign a label, using the name attribute,
frame.index.name = 'id'; frame.columns.name = 'item'
frame['new'] = 12 # add a new column, assigning a value to the instance of the DataFrame specifying a new column name
# update of the contents of a column, you have to use an array
frame['new'] = [3.0,1.3,2.2,0.8,1.1]
# columns of a data frame can also be created by assigning a Series to one of them
ser = pd.Series(np.arange(5))
ser
frame['new'] = ser # Creating a column
frame['price'][2] = 3.3 # change a single value

#                                             Membership of a Value
isin( ) # 
frame.isin([1.0,'pen']) # Boolean values
frame[frame.isin([1.0,'pen'])] # With NAN values
#                         Deleting a Column
del frame['new']
#                                                                   Filtering
frame[frame < 12] # Other values replaced with NAN
#                                                                                            Series as Dictionaries
# create a series from a dict previously defined
mydict = {'red': 2000, 'blue': 1000, 'yellow': 500, 'orange': 1000}
myseries = pd.Series(mydict)
#                                Operations between Series
mydict2 = {'red':400,'yellow':1000,'black':700}
myseries2 = pd.Series(mydict2)
myseries + myseries2
#                                                                                                Nested dict
nestdict = { 'red': { 2012: 22, 2013: 33 },
'white': { 2011: 13, 2012: 22; 2013: 16},
'blue': {2011: 17, 2012: 27; 2013: 18}}
frame2 = pd.DataFrame(nestdict)
#                                                    Transposition of a DataFrame
frame2.T # the columns become rows and rows columns
#                                                                                              Function Application and Mapping
#                                            Functions by Element
frame = pd.DataFrame(np.arange(16).reshape((4,4)),
index=['red','blue','yellow','white'],
columns=['ball','pen','pencil','paper'])
#  calculate the square root of each value within the data frame, np.sqrt()
np.sqrt(frame)
#                                 Functions by Row or Column
# define a lambda function that calculates the range covered by the elements in an array
f = lambda x: x.max() - x.min()
# 
def f(x):
    return x.max() - x.min()
# apply the function just defined on the DataFrame
frame.apply(f)
frame.apply(f, axis=1) # apply the function by row
# Return Series
def f(x):
    return pd.Series([x.min(), x.max()], index=['min','max'])
#                                                                                                  Statistics Functions
frame.sum()
frame.mean()
frame.describe() # to obtain a summary statistics at once
#                                                                                    Sorting and Ranking
# sort_index( ) = returns a new object which is identical to the start
ser = pd.Series([5,0,3,8,4], index=['red','blue','yellow','white','green'])
ser.sort_index()
# set the opposite order, using the ascending option set to False.
ser.sort_index(ascending=False)
# to order by columns, you will need to use the axis options set to 1.
frame = pd.DataFrame(np.arange(16).reshape((4,4)),
index=['red','blue','yellow','white'],
columns=['ball','pen','pencil','paper'])
frame.sort_index(axis=1)
# to order the series, you will use the order( ) function.
ser.order()
# order the values in a DataFrame
frame.sort_index(by='pen') # assign an array containing the names of the columns to the by option
# 
ser.rank(method='first') # without a sorting operation)
ser.rank()
ser.rank(ascending=False)
#                                 Correlation and Covariance, corr( ) and cov( )
seq2 = pd.Series([3,4,3,4,5,4,3,2],['2006','2007','2008','2009','2010','2011','2012','2013'])
seq = pd.Series([1,2,3,4,4,3,2,1],['2006','2007','2008','2009','2010','2011','2012','2013'])
seq.corr(seq2)0.77459666924148329
seq.cov(seq2)0.8571428571428571
#                               covariance and correlation are applied to a single DataFram
frame2 = DataFrame([[1,4,3,6],[4,5,6,1],[3,3,1,5],[4,1,6,4]],
index=['red','blue','yellow','white'],
columns=['ball','pen','pencil','paper'])
frame2.corr()
frame2.cov()
# corrwith( ) = pairwise correlations between the columns or rows of a data frame
frame2.corrwith(ser)
frame2.corrwith(frame)
#                                                                            Hierarchical Indexing and Leveling
# # multiple levels of indexes on a single axis
# creating a structure with two levels. = creating a series containing two arrays of indexes
# reshaping the data and group-based operations such as creating a pivot-table
mser = pd.Series(np.random.rand(8),
index=[['white','white','white','blue','blue','red','red','red'],
['up','down','right','up','down','up','down','left']])
mser.index
MultiIndex(levels=[[u'blue', u'red', u'white'], [u'down', u'left', u'right', u'up']],
labels=[[2, 2, 2, 0, 0, 1, 1, 1], [3, 0, 2, 3, 0, 3, 0, 1]])ù
# select values for a given value of the second index
mser[:,'up']
# to select a specific value
mser['white','up']
# unstack( ) = converts the Series with hierarchical index in a simple DataFrame,
# where the second set of indexes is converted into a new set of columns.
mser.unstack()
# stack() = convert a DataFrame in a Series,
frame.stack()
#                                                to define a hierarchical index both for the rows and for the columns
mframe = pd.DataFrame(np.random.randn(16).reshape(4,4),
index=[['white','white','red','red'], ['up','down','up','down']],
columns=[['pen','pen','paper','paper'],[1,2,1,2]])
#                                                                         Reordering and Sorting Levels
# swaplevel( ) =  rearrange the order of the levels on an axis or do a sorting for values at a specific level
mframe.columns.names = ['objects','id']
# interchange, and returns a new object with the two levels interchanged between them
mframe.index.names = ['colors','status']
mframe.swaplevel('colors','status')
mframe.sortlevel('colors')
#                                                                                            Summary Statistic by Level
mframe.sum(level='colors') # specify the level option with level name
# to make a statistic for a given level of the column
mframe.sum(level='id', axis=1)
#                                               Read and Write file
"""read_csv                to_csv
read_excel             to_excel
read_hdf                to_hdf
read_sql                to_sql
read_json              to_json
read_html             to_html
read_stata            to_stata
read_clipboard      to_clipboard
read_pickle           to_pickle
read_msgpack     to_msgpack (experimental)
read_gbq              to_gbq (experimental)"""
# convert it to DataFrame
csvframe = read_csv('myCSV_01.csv')
read_table('ch05_01.csv',sep=',')
# to assign default names to the columns by using the header option set to None
read_csv('ch05_02.csv', header=None)
read_csv('ch05_02.csv', names=['white','red','blue','green','animal'])
# assigning all the columns to be converted into indexes
read_csv('ch05_03.csv', index_col=['color','status'])
#                                                                                              Using RegExp for Parsing TXT Files
#  files on which to parse the data do not show separators well defined as a comma or a semicolon
# TXT file, has values separated by spaces or tabs in an unpredictable order
wildcard /s*. /s # for indicating tab /t is used
"""Table Metacharacters
-------------------------------------------------------------------
.    single character, except newline
\d    digit
\D    non-digit character
\s    whitespace character
\S    non-whitespace character
\n    new line character
\t    tab character
\uxxxx    unicode character specified by the hexadecimal number xxxx"""
read_table('ch05_04.txt',sep='\s*') # in random order
#             to extract the numeric part from a TXT file, separator characters as alphanumeric characters
read_table('ch05_05.txt',sep='\D*',header=None)
# With the skiprows option you can exclude all the lines you want
# to exclude the first five lines, then you have to write skiprows = 5
# to rule out the fifth line you have to write skiprows = [5]
read_table('ch05_06.txt',sep=',',skiprows=[0,1,3,6])
#                                                                                        Reading TXT Files into Parts or Partially
read_csv('ch05_02.csv',skiprows=[2],nrows=3,header=None)  # to apply any iterations
# specify the number of lines on which to parse
#                                                                  Writing Data in CSV
frame2.to_csv('ch05_07.csv')
# default behavior can be changed by placing the two options index and header set to False 
frame2.to_csv('ch05_07b.csv', index=False, header=False)
#                                                                                          Operations and Mathematical Functions
# mathematical functions that are applicable to NumPy array can be extended to objects Series.
# specify the function referenced with np and the instance of the Series passed as argument
np.log(s)
#                                                     Evaluating Values
# counting duplicates and whether a value is present or not in the Series, declare a series in which there are many duplicate values
serd = pd.Series([1,0,2,1,2,3], index=['white','white','blue','green','green','yellow'])
# To know all the values contained within the Series excluding duplicates, unique( )
serd.unique()
value_counts( )  # Calculates occurrences within a Series
serd.value_counts()
# unction that evaluates the membership
serd.isin([0,3])
#                                                                           NaN Values
# calculations of logarithms of negative values, or exceptions during execution of some calculation or function
# explicitly define and add this value in a data structure, such as Series. Within the array containing the values
np.NaN
s2 = pd.Series([5,-3,np.NaN,14])
#  notnull( ) = to identify the indexes without a value
s2[s2.notnull( )]
s2[s2.isnull( )]
#                                                                                               Reading Data from XML
# structured data are available in XML format
# eading and writing of data in XML format, lxml library,
from lxml import objectify
xml = objectify.parse('books.xml') # object tree
root = xml.getroot() # define the root
# separate tags with points, with hierarchy of nodes in the tree
root.Book.Author
root.Book.PublishDate
root.getchildren() # access various nodes and elements
# name of the tag corresponding to the child node
 [child.tag for child in root.Book.getchildren()]
['Author', 'Title', 'Genre', 'Price', 'PublishDate']
[child.text for child in root.Book.getchildren()]
['Ross, Mark', 'XML Cookbook', 'Computer', '23.56', '2014-22-01']
# Convert lxml.etree tree structure into a data frame
# analyzing the entire contents of a eTree to fill a DataFrame line by line
def etree2df(root):
    column_names = []
    for i in range(0,len(root.getchildren()[0].getchildren())):
       column_names.append(root.getchildren()[0].getchildren()[i].tag)
       xml:frame = pd.DataFrame(columns=column_names)
    for j in range(0, len(root.getchildren())):
       obj = root.getchildren()[j].getchildren()
       texts = []
       for k in range(0, len(column_names)):
          texts.append(obj[k].text)
          row = dict(zip(column_names, texts))
          row_s = pd.Series(row)
          row_s.name = j
          xml:frame = xml:frame.append(row_s)
          return xml:frame...>>> etree2df(root)
#                                                                                                          Read Write on Excel
pd.read_excel('data.xls')
pd.read_excel('data.xls','Sheet2')
pd.read_excel('data.xls',1)
#                                to convert a data frame in a spreadsheet on Excel
frame = pd.DataFrame(np.random.random((4,4)),
index = ['exp1','exp2','exp3','exp4'],
columns = ['Jan2015','Fab2015','Mar2015','Apr2005'])
#                                  a new Excel file containing the data
frame.to_excel('data2.xlsx')
#                                                                                                 Reading and Writing HTML Files
# to convert complex data structures such as DataFrame directly in HTML tables
# read_html(), to_html()
#                                           Writing Data in HTML 
#  The internal structure of the data frame is automatically converted into nested tags
# to directly convert the DataFrame in an HTML table
frame = pd.DataFrame(np.arange(4).reshape(2,2))
print(frame.to_html())
# create a data frame with labels of the indexes and column names
frame = pd.DataFrame( np.random.random((4,4)),
index = ['white','black','red','blue'],
columns = ['up','down','right','left'])
#                            writing an HTML page through the generation of a string
s = ['
']
s.append('My DataFrame')
s.append('')
s.append(frame.to_html())>>> s.append('')
html = ''.join(s)
html_file = open('myFrame.html','w')
html_file.write(html)
html_file.close()
#                                                                                             Reading Data from an HTML File
#                                         parsing the HTML file
web_frames = pd.read_html('myFrame.html')
web_frames[0]
#                                                                                            Operations between Data Structures
frame1.add(frame2)
# indexes and column names differ greatly from one series to another
# Operations between DataFrame and Series
# 
frame = pd.DataFrame(np.arange(16).reshape((4,4)),
index=['red','blue','yellow','white'],  #            define 2 Structure
columns=['ball','pen','pencil','paper'])
ser = pd.Series(np.arange(4), index=['ball','pen','pencil','paper'])
frame - ser # minus
ser['mug'] = 9 # new column with that index only that all its elements will be NaN
#                                                                                                JSON (JavaScript Object Notation)
# convert DataFrame into JSON File, efine a DataFrame and then call the to_json() function
frame = pd.DataFrame(np.arange(16).reshape(4,4),
index=['white','black','red','blue'],
columns=['up','down','right','left'])
frame.to_json('frame.json')
pd.read_json('frame.json')
# JSON files do not have a tabular structure, convert the structure dict file in tabular form
# Load the contents of the JSON file and convert it into a string.
from pandas.io.json import json_normalize
file = open('books.json','r')
text = file.read()
text = json.loads(text)
json_normalize(text,'books')  # extract a table that contains all the books
# add other columns by inserting a key list as the third argument of the function
json_normalize(text2,'books',['writer','nationality'])
#                                                                                                Load or Write Data with SQLite3
# Create a data frame that you will use to create a new table on the SQLite3 database
frame = pd.DataFrame( np.arange(20).reshape(4,5),
columns=['white','red','blue','black','green'])
engine = create_engine('sqlite:///foo.db') # implement the connection to the SQLite3 database
frame.to_sql('colors',engine)  # Convert the DataFrame in a table within the database
pd.read_sql('colors',engine)
import sqlite3
query = """
... CREATE TABLE test
... (a VARCHAR(20), b VARCHAR(20),
...  c REAL,        d INTEGER
... );"""
con = sqlite3.connect(':memory:')
con.execute(query)
con.commit()
# enter data through the SQL INSERT statement
data = [('white','up',1,3),
('black','down',2,8),('green','up',4,4),
('red','down',5,5)]
stmt = "INSERT INTO test VALUES(?,?,?,?)"
con.executemany(stmt, data)
con.commit()
# query the database to get the data you just recorded
cursor = con.execute('select * from test')
cursor
rows = cursor.fetchall()
rows #   pass the list of tuples to the constructor of the DataFrame
[(u'white', u'up', 1.0, 3), (u'black', u'down', 2.0, 8), (u'green', u'up', 4.0, 4),  (u'red', 5.0, 5)]
cursor.description
pd.DataFrame(rows, columns=zip(*cursor.description)[0])
#                                                                                                           Adv - Data Preparation
# to prepare the data and assemble them in the form of data structures
# pandas.concat() function concatenates the objects along an axis
# pandas.DataFrame.combine_first( )
#                                                                                                                 Merging
# 
frame1 = pd.DataFrame( {'id':['ball','pencil','pen','mug','ashtray'],
'price': [12.33,11.44,33.21,13.23,33.62]})
frame2 = pd.DataFrame( {'id':['pencil','pencil','ball','pen'],
'color': ['white','red','red','black']})
pd.merge(frame1,frame2)
pd.merge(frame1,frame2,on='id')
# The left_on and right_on options that specify the key column for the first and for the second DataFrame.
pd.merge(frame1, frame2, left_on='id', right_on='sid')
# The outer join produces the union of all keys,
pd.merge(frame1,frame2,on='id',how='outer')
pd.merge(frame1,frame2,on='id',how='left')
pd.merge(frame1,frame2,on='id',how='right')
pd.merge(frame1,frame2,on=['id','brand'],how='outer')  # merge of multiple keys
#                                                                                 Merging on Index
# left_index or right_index options to True to activate them
pd.merge(frame1,frame2,right_index=True, left_index=True)
ame2.columns = ['brand2','id2']
frame1.join(frame2)

#                                                                                                Data Transformation
# simple DataFrame with some duplicate rows.
dframe = pd.DataFrame({ 'color': ['white','white','red','red','white'],
'value': [2,1,3,3,2]})
dframe.duplicated() # find duplicate Elements
dframe[dframe.duplicated()] # find duplicate row
dframe[dframe.duplicated()] # # delete duplicate rows
#                                                                             Mapping
# to bind a value to a particular label or string.To define a mapping there is no better object than dict objects
map = {
   'label1' : 'value1,
   'label2' : 'value2,
   }
"""replace(): replaces values
map(): creates a new column
rename(): replaces the index values"""
#                                                                          Replacing Values via Mapping
frame = pd.DataFrame({ 'item':['ball','mug','pen','pencil','ashtray'],
'color':['white','rosso','verde','black','yellow'],
'price':[5.56,4.20,1.30,0.56,2.75]})
#                                       to replace the incorrect values in new values
newcolors = {
    'rosso': 'red',
    'verde': 'green'
    }
frame.replace(newcolors)
ser = pd.Series([1,3,np.nan,4,6,np.nan,3])
ser.replace(np.nan,0)
#                                                     Adding Values via Mapping
frame = pd.DataFrame({ 'item':['ball','mug','pen','pencil','ashtray'],
'color':['white','red','green','black','yellow']})
price = {
    'ball' : 5.56,
    'mug' : 4.20,
    'bottle' : 1.30,
    'scissors' : 3.41,
    'pen' : 1.30,
    'pencil' : 0.56,
    'ashtray' : 2.75
    }
frame['price'] = frame['item'].map(prices)
#                                                       Rename the Indexes of the Axes
reindex = {
    0: 'first',
    1: 'second',
    2: 'third',
    3: 'fourth',
    4: 'fifth'
    }
frame.rename(reindex)
recolumn = {
    'item':'object',
    'price': 'value'
    }
frame.rename(index=reindex, columns=recolumn)
frame.rename(index={1:'first'}, columns={'item':'object'})
frame.rename(columns={'item':'object'}, inplace=True)
#                                                           Discretization and Binning
results = [12,34,67,55,28,90,99,12,3,56,74,44,87,23,49,89,87]
bins = [0,25,50,75,100]
cat = pd.cut(results, bins)
cat.levels
cat.labels # occurrences for each bin,
bin_names = ['unlikely','less likely','likely','highly likely']
pd.cut(results, bins, labels=bin_names)
pd.cut(results, 5)
#                          for binning: qcut()
quintiles = pd.qcut(results, 5)
quintiles
pd.value_counts(quintiles)
#                        Detecting and Filtering Outliers
randframe = pd.DataFrame(np.random.randn(1000,3))
randframe.describe()
randframe.std()
randframe[(np.abs(randframe) > (3*randframe.std())).any(1)]
#                                                                                   Pandas - String Manipulation
#                      Built-in Methods
text = '16 Bolton Avenue , Boston'
text.split(',')
tokens = [s.strip() for s in text.split(',')]
address, city = [s.strip() for s in text.split(',')] # array of strings
address + ',' + city'
strings = ['A+','A','A-','B','BB','BBB','C+']';'.join(strings)
text.index('Boston')
text.find('Boston')
text.index('New York')
text.find('New York')
text.count('e')2
text.count('Avenue')
text.replace('Avenue','Street')
text.replace('1','')
#                                                                                          Regular Expressions
# pattern matching. substitution, splitting
import re
text = "This is      an\t odd  \n text!"
re.split('\s+', text)
# Output = ['This', 'is', 'an', 'odd', 'text!']
regex = re.compile('\s+')
regex.split(text)
text = 'This is my address: 16 Bolton Avenue, Boston'
re.findall('A\w+',text) # to find uppercase letter
re.findall('[A,a]\w+',text)
#                                           findall(): match() and search().
re.search('[A,a]\w+',text)
search = re.search('[A,a]\w+',text)
search.start()11
search.end()18
text[search.start():search.end()]
re.match('[A,a]\w+',text) # begining of the statement
re.match('T\w+',text)
match = re.match('T\w+',text)
text[match.start():match.end()]
#                                                                                                 Data Aggregation
#                                           GroupBy
#                       SPLIT-APPLY-COMBINE
#  to calculate the average price1 column using group labels listed in the column color
group = frame['price1'].groupby(frame['color'])
group.groups # each group is listed explicitly
group.mean()
group.sum()
#                             Hierarchical Grouping
ggroup = frame['price1'].groupby([frame['color'],frame['object']])
ggroup.sum()
frame[['price1','price2']].groupby(frame['color']).mean()
frame.groupby(frame['color']).mean()
#                                                                                Group Iteration
# an iteration for generating a sequence of 2-tuples containing the name of the group together with the data portion.
for name, group in frame.groupby('color'):
    print name
    print group
#                                        Chain of Transformations
result1 = frame['price1'].groupby(frame['color']).mean()
type(result1)
result2 = frame.groupby(frame['color']).mean()
type(result2)
frame['price1'].groupby(frame['color']).mean()
frame.groupby(frame['color'])['price1'].mean()
(frame.groupby(frame['color']).mean())['price1']
(frame.groupby(frame['color']).mean())['price1']
means = frame.groupby('color').mean().add_prefix('mean_')
#                                              Functions on Groups
group = frame.groupby('color')
group['price1'].quantile(0.6)
#                                             calculate the range of the values of  each group
def range(series):
    return series.max() - series.min()
group['price1'].agg(range)
group.agg(range)
group['price1'].agg(['mean','std',range])
#                                     transform() and apply() functions
frame = pd.DataFrame({ 'color':['white','red','green','red','green'],
'price1':[5.56,4.20,1.30,0.56,2.75],
'price2':[4.75,4.12,1.60,0.75,3.15]})
sums = frame.groupby('color').sum().add_prefix('tot_')
merge(frame,sums,left_on='color',right_index=True) # add the results of a calculation of aggregation in each line of the data frame to start
frame.groupby('color').transform(np.sum).add_prefix('tot_') # calculation of aggregation
#                             invokes the passage of function on each piece, and then tries to chain together the  various parts
frame = DataFrame( { 'color':['white','black','white','white','black','black'],
'status':['up','up','down','down','down','up'],
'value1':[12.33,14.55,22.34,27.84,23.40,18.33],
'value2':[11.23,31.80,29.99,31.18,18.25,22.44]})
frame.groupby(['color','status']).apply( lambda x: x.max())
frame.rename(index=reindex, columns=recolumn)
temp = date_range('1/1/2015', periods=10, freq= 'H')
temp
timetable = DataFrame( {'date': temp, 'value1' : np.random.rand(10),
'value2' : np.random.rand(10)})
timetable['cat'] = ['up','down','left','left','up','up','down','right','right','up']
#                                                                                            Measuring Central Tendency
# center or distribution of location of values of a data set
# chances of a new input fitting into the existing data set and hence probability of success

# Mean - It is the Average value of the data which is a division of sum of the values with the number of values.This function returns the arithmetic average of the data it operates on. If called on an empty container of data, it raises a StatisticsError.
#           is the most frequently used measure of central tendency and generally considered the best measure of it
# Median - It is the middle value in distribution when the values are arranged in ascending or descending order.For data of odd length, this returns the middle item; for that of even length, it returns the average of the two middle items.
#          There are a few extreme scores in the distribution of the data.(
#          There are some missing or undetermined values in your data. c
#          There is an open ended distribution, You have data measured on an ordinal scale   
# Mode - It is the most commonly occurring value in a distribution.This function returns the most common value in a set of data. This gives us a great idea of where the center lies.
#                                                                  Calculating Mean and Median
import pandas as pd
#                                                                  Create a Dictionary of series
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack',
   'Lee','Chanchal','Gasper','Naviya','Andres']),
   'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])}
#                                                                   Create a DataFrame
df = pd.DataFrame(d)
print ("Mean Values in the Distribution")
df.mean()
print ("*******************************")
print ("Median Values in the Distribution")
df.median()
#                                                   Calculating Mode
#C                                           reate a Dictionary of series
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack',
   'Lee','Chanchal','Gasper','Naviya','Andres']),
   'Age':pd.Series([25,26,25,23,30,25,23,34,40,30,25,46])}
#                                                  Create a DataFrame
df = pd.DataFrame(d)
print df.mode()

#                                                                                                 Measuring Variance()
# Statistics module provides very powerful tools, which can be used to compute anything related to Statistics. 
# variance() is one such function. This function helps to calculate the variance from a sample of data (sample is a subset of populated data).
# pvariance() is used to calculate the variance of an entire population
# variance is the squared deviation of a variable from its mean
#          it measures the spread of random data in a set from its mean or median value.
#          A low value for variance indicates that the data are clustered together and are not spread apart widely,
# whereas a high value would indicate that the data in the given set are much more spread apart from the average value.
# It is measured by using standard deviation. The other method commonly used is skewness.
#                                                          Measuring Standard Deviation
# Standard deviation is square root of variance. variance is the average of squared difference of values in a data set from the mean value
#                                                            Calculate the standard deviation
print df.std()
#                                                             Measuring Skewness
# used to determine whether the data is symmetric or skewed. If the index is between -1 and 1, then the distribution is symmetric.
# If the index is no more than -1 then it is skewed to the left and if it is at least 1, then it is skewed to the right
print df.skew()
# the distribution of  rating is symmetric while the distribution of age is skewed to the right

#                                                         Normal Distribution
# presenting data by arranging the probability distribution of each value in the data
# symmetric.scipy.stats.norm() is a normal continuous random variable. It is inherited from the of generic methods as an instance of the rv_continuous class.
# It completes the methods with details specific for this particular distribution
# probability distribution describes how the values of a random variable is distributed.
# It is a statistical function that describes all the possible values and likelihoods that a random variable can take within a given range.
# A probability distribution can be discrete if the set of possible outcomes consists of discrete values(e.g. toss of a coin where the possible outcome of a toss is either head or tail) or
# continuous if the set of possible outcomes consists of real numbers (e.g. humidity measured on a day)
#                                                                               Parameters :
#       q : lower and upper tail probability
#       x : quantiles
#     loc : [optional]location parameter. Default = 0
#   scale : [optional]scale parameter. Default = 1
#    size : [tuple of ints, optional] shape or random variates.
# moments : [optional] composed of letters [‘mvsk’]; ‘m’ = mean, ‘v’ = variance, ‘s’ = Fisher’s skew and ‘k’ = Fisher’s kurtosis. (default = ‘mv’).

# the Central limit theorem : if you have many independent variables that may be generated by all kinds of distributions,
import matplotlib.pyplot as plt
import numpy as np
mu, sigma = 0.5, 0.1
s = np.random.normal(mu, sigma, 1000)
#                                                     Create the bins and histogram
count, bins, ignored = plt.hist(s, 20, normed=True)
#                                                              Plot the distribution curve
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
    np.exp( - (bins - mu)**2 / (2 * sigma**2) ),       linewidth=3, color='y')
plt.show()

#                                                                                 Binomial Distribution
# finding the probability of success of an event which has only two possible outcomes in a series of experiments
# Discrete Distribution, It describes the outcome of binary scenarios
#    n - number of trials.
#    p - probability of occurence of each trial (e.g. for toss of a coin 0.5 each).
# size - The shape of the returned array.
# Discrete Distribution:The distribution is defined at separate set of events
from scipy.stats import binom
import seaborn as sb

binom.rvs(size=10,n=20,p=0.8)

data_binom = binom.rvs(n=20,p=0.8,loc=0,size=1000)
ax = sb.distplot(data_binom,
                  kde=True,
                  color='blue',
                  hist_kws={"linewidth": 25,'alpha':1})
ax.set(xlabel='Binomial', ylabel='Frequency')

#                                                                              Poisson Distribution
# the event can only be measured as occurring or not as occurring,
# meaning the variable can only be measured in whole numbers.Fractional occurrences of the event are not a part of the model
# independent events which occur at a constant rate within a given interval of time
# It estimates how many times an event can happen in a specified time
from scipy.stats import poisson
import seaborn as sb

data_binom = poisson.rvs(mu=4, size=10000)
ax = sb.distplot(data_binom,
                  kde=True,
                  color='green',
                  hist_kws={"linewidth": 25,'alpha':1})
ax.set(xlabel='Poisson', ylabel='Frequency')

#                                                                                                Bernoulli's Distribution
# only two possible outcomes, namely 11 (success) and 00 (failure), and a single trial
# a coin toss. So the random variable XX which has a Bernoulli distribution can take value 11 
# with the probability of success, pp, and the value 00 with the probability of failure, qq or 1−p1−p.
# The probabilities of success and failure need not be equally likely.
# The Bernoulli distribution is a special case of the binomial distribution where a single trial is conducted (n=1n=1). 
# Its probability mass function is given by : f(k;p) = p^k(1-p)^1-k for k = {0,1}
# generate a bernoulli distributed discrete random variable using scipy.stats module's bernoulli.rvs() method
# which takes pp (probability of success) as a shape parameter. To shift distribution use the loc parameter. 
# size decides the number of times to repeat the trials. 
# If you want to maintain reproducibility, include a random_state argument assigned to a number.
# single experiment is conducted so that the number of observation is 1
from scipy.stats import bernoulli
import seaborn as sb

data_bern = bernoulli.rvs(size=1000,p=0.6)
ax = sb.distplot(data_bern,
                  kde=True,
                  color='crimson',
                  hist_kws={"linewidth": 25,'alpha':1})
ax.set(xlabel='Bernouli', ylabel='Frequency')

#                                                                                                         P Value
# the strength of a hypothesis. We build hypothesis based on some statistical model and compare the model's validity using p-value.
# One way to get the p-value is by using T-test. p-value for a statistical model is the probability that when the null hypothesis is true
#                                                                        Python Decorators
"""The null hypothesis states that two measured phenomena experience no relationship to each other. We denote this as H or H0. 
One such null hypothesis can be that the number of hours spent in the office affects the amount of salary paid. 
For a significance level of 5%, if the p-value falls lower than 5%, the null hypothesis is invalidated. 
Then it is discovered that the number of hours you spend in your office will not affect the amount of salary you will take home. 
Note that p-values can range from 0% to 100% and we write them in decimals. A p-value for 5% will be 0.05."""
# two-sided test for the null hypothesis that the expected value (mean) of a sample of independent observations ‘a’ is equal to the given population mean, popmean
from scipy import stats
rvs = stats.norm.rvs(loc = 5, scale = 10, size = (50,2))
print stats.ttest_1samp(rvs,5.0)

Ttest_1sampResult(statistic = array([-1.40184894, 2.70158009]),
pvalue = array([ 0.16726344, 0.00945234]))

# ttest_ind − Calculates the T-test for the means of two independent samples of scores.
# test assumes that the populations have identical variances by default.
#                                                                         $  Two-Sample T-Test vs. a Paired T-Test (Hypothesis)
# two samples must have come from two completely different populations, if your samples are connected in some way, 
# run a paired samples t-test. “Connected” means that you are collecting data twice from the same group, person, item or thing
from scipy import stats
rvs1 = stats.norm.rvs(loc = 5,scale = 10,size = 500)
rvs2 = stats.norm.rvs(loc = 5,scale = 10,size = 500)
print stats.ttest_ind(rvs1,rvs2)
# You can test the same with a new array of the same length, but with a varied mean. Use a different value in loc and test the same

#                                                                                                     Correlation
# statistical relationships involving dependence between two data sets
# correlation between the price for a product and its supplied quantity.
# Correlation coefficients quantify the association between variables or features of a dataset.
# Correlation values range between -1 and 1
# Useful as a pointer for further, more detailed research
# magnitude – The larger the magnitude (closer to 1 or -1), the stronger the correlation
#      sign – If negative, there is an inverse correlation. If positive, there is a regular correlation.
# Based on the correlation found, a strong model could be created which easily distinguishes one species from another.
import matplotlib.pyplot as plt
import seaborn as sns
df = sns.load_dataset('iris')
#                                       without regression
sns.pairplot(df, kind="scatter")
plt.show()
#                                                                                                 Creating Time Series
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('path_to_file/stock.csv')
df = pd.DataFrame(data, columns = ['ValueDate', 'Price'])

# Set the Date as Index
df['ValueDate'] = pd.to_datetime(df['ValueDate'])
df.index = df['ValueDate']
del df['ValueDate']


df.plot(figsize=(15, 6))
plt.show()

#                                                              Geographical Data & visualization
# mpl_toolkits, cartopy
# Cartopy is a Python package for cartography. It will let you process geospatial data, analyze it, and produce maps
# Object-oriented projection definitions.
# Publication quality maps.
# Ability to transform points, lines, polygons, vectors, and images.
#                     $                                         show a portion of the world map showing parts of Asia and Australia
import matplotlib.pyplot as plt
import cartopy.crs as ccrs

fig = plt.figure(figsize=(15, 10))
ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
ax.set_extent((60, 150, 55, -25))   # make the map global rather than have it zoom in to
#                                     extents of any plotted data
ax.stock_img()
ax.coastlines()
ax.tissot(facecolor='purple', alpha=0.8)
plt.show()

#                                                                                                                 $   sparse Graph
# CSGraph = Compressed Sparse Graph
# sparse graph  = collection of nodes, which have links between them
# where each node is a person and is connected to acquaintances;
# images, where each node is a pixel and is connected to neighbouring pixels; points in a high-dimensional distribution,
# where each node is connected to its nearest neighbours and practically anything else you can imagine.
# The matrix G is of size N x N, and G[i, j] gives the value of the connection between node ‘i' and node ‘j’
#      Isomap                      − A manifold learning algorithm, which requires finding the shortest paths in a graph.
#      Hierarchical clustering     − A clustering algorithm based on a minimum spanning tree.
#      Spectral Decomposition      − A projection algorithm based on sparse graph laplacians.
#                                                                     create graph with three nodes
G_dense = np.array([ [0, 2, 1],
                     [2, 0, 0],          # node 0 and 1 are connected by an edge of weight 2
                     [1, 0, 0] ])         #   nodes 0 and 2 are connected by an edge of weight 1
G_masked = np.ma.masked_values(G_dense, 0)
from scipy.sparse import csr_matrix
G_sparse = csr_matrix(G_dense)
print G_sparse.data 

# nodes 0 and 2 are connected by an edge of zero weight
from scipy.sparse.csgraph import csgraph_from_dense
G2_data = np.array
([
   [np.inf, 2, 0 ],
   [2, np.inf, np.inf],
   [0, np.inf, np.inf]
])
G2_sparse = csgraph_from_dense(G2_data, null_value=np.inf)
print G2_sparse.data
#                                                                 Chi Square Test
# test of statistical significance for categorical variables
# testing relationships between categorical variables
# he Test of Independence assesses whether an association exists between the two variables
# by comparing the observed pattern of responses in the cells to the pattern that would be expected 
# if the variables were truly independent of each other
# fo = the observed frequency (the observed counts in the cells)
# and fe = the expected frequency if NO relationship existed between the variables
# Calculating the Chi-Square statistic and comparing it against a critical value from the Chi-Square distribution allows the researcher to assess whether the observed cell counts are significantly different from the expected cell counts
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
fig,ax = plt.subplots(1,1)

linestyles = [':', '--', '-.', '-']
deg_of_freedom = [1, 4, 7, 6]
for df, ls in zip(deg_of_freedom, linestyles):
  ax.plot(x, stats.chi2.pdf(x, df), linestyle=ls)

plt.xlim(0, 10)
plt.ylim(0, 0.4)

plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Chi-Square Distribution')

plt.legend()
plt.show()



#                                                                             Processing csv Data
data = pd.read_csv('filepath')
print(data)
print(data[0:5]['salary'])                                    # slice the result for first 5 rows, dtype: float64
#                                                                      DictReader class
#                                                              reading specific columns
print(data.loc[:,['salary','name']])                        # multi axes indexing function
# reading specific columns for range of rows
print(data.loc[:,['salary','name']])

# JSON (JavaScript Object Notation)
# create a sample json file .json
"""
{ 
   "ID":["1","2","3","4","5","6","7","8" ],
   "Name":["Rick","Dan","Michelle","Ryan","Gary","Nina","Simon","Guru" ]
   "Salary":["623.3","515.2","611","729","843.25","578","632.8","722.5" ],
   
   "StartDate":[ "1/1/2012","9/23/2013","11/15/2014","5/11/2014","3/27/2015","5/21/2013",
      "7/30/2013","6/17/2014"],
   "Dept":[ "IT","Operations","IT","HR","Finance","IT","Operations","Finance"]
}
""" # .json
#                                                                                                    pd.read_json()
import pandas as pd
data = pd.read_json('path/input.json')
print (data)
#                                                                                            Reading Specific Columns and Rows
data = pd.read_json('path/input.xlsx')                      # Use the multi-axes indexing funtion
print (data.loc[[1,3,5],['salary','name']])
#                                                                          Reading JSON file as Records
data = pd.read_json('path/input.xlsx')
print(data.to_json(orient='records', lines=True))

data = pd.read_excel('path/input.xlsx')                                     # Reading an Excel File
print (data)
# Reading Specific Columns and Rows
data = pd.read_excel('path/input.xlsx')   #                         Use the multi-axes indexing funtion
print (data.loc[[1,3,5],['salary','name']])
#                                                                   Reading Multiple Excel Sheets
with pd.ExcelFile('C:/Users/Rasmi/Documents/pydatasci/input.xlsx') as xls:
    df1 = pd.read_excel(xls, 'Sheet1')
    df2 = pd.read_excel(xls, 'Sheet2')
print("****Result Sheet 1****")
print (df1[0:5]['salary'])
print("")
print("***Result Sheet 2****")
print (df2[0:5]['zipcode'])

#                                                                  Word Tokenization
# Tokenization is the process of replacing sensitive data with 
# unique identification symbols that retain all the essential information about the data.
# booster the security of credit card and e-commerce transactions while minimizing the cost and complexity
# Word tokenization is the process of splitting a large sample of text into words.
# text into a list of tokens. 
# Text into sentences tokenization
# Sentences into words tokenization
# Sentences using regular expressions tokenization
import nltk
word_data = "It originated from the idea that there are readers who prefer learning new skills from the comforts of their drawing rooms"
nltk_tokens = nltk.word_tokenize(word_data)
print (nltk_tokens)

#                                                          Tokenizing Sentences
import nltk
sentence_data = "Sun rises in the east. Sun sets in the west."
nltk_tokens = nltk.sent_tokenize(sentence_data)
print (nltk_tokens)

#                                                       Box Plot
# median, upper quartile, lower quartile, minimum and maximum data values.
import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.rand(10, 5), columns=['A', 'B', 'C', 'D', 'E'])
df.plot.box(grid='True')

#                                                                       Processing Unstructued Data
#                 Reading Data
filename = 'path\input.txt'  

with open(filename) as fn:  

#                                                          Read each line
   ln = fn.readline()

#                                                       Keep count of lines
   lncnt = 1
   while ln:
       print("Line {}: {}".format(lncnt, ln.strip()))
       ln = fn.readline()
       lncnt += 1

#                                            Counting Word Frequency
from collections import Counter

with open(r'pathinput2.txt') as f:
   p = Counter(f.read().split())
   print(p)

#                                                                                           Natural Language Processing
# agreed, agreeing and agreeable have the same root word agree
#                                                 Stemming 
# normalization for words, variation according to the context or sentence are normalized.
#                                                               Lemmatization 
# finding the lemma of a word depending on their meaning
# Text preprocessing includes both stemming as well as lemmatization
"""Stemming algorithm works by cutting the suffix from the word. In a broader sense cuts either the beginning or end of the word.

On the contrary, Lemmatization is a more powerful operation, and it takes into consideration morphological analysis of the words.
 It returns the lemma which is the base form of all its inflectional forms."""
# linguistic knowledge is required to create dictionaries and look for the proper form of the word. Stemming is a general operation
#  while lemmatization is an intelligent operation where the proper form will be looked in the dictionary
# Text Mining is the process of analysis of texts written in natural language and extract high-quality information from text.
# text categorization, text clustering, concept/entity extraction, production of granular taxonomies, sentiment analysis,
# document summarization, and entity relation modeling (i.e., learning relations between named entities)
#                                        Information Retrieval (IR) Environments
#                                                 Sentiment Analysis
# Sentiment Analysis is the analysis of people's reviews and comments about something.
# It is widely used for analysis of product on online retail shops.
# Stemming and Lemmatization is used as part of the text-preparation process before it is analyzed.

#                                                                      Document clustering
# Automatic document organization, topic extraction, and fast information retrieval or filtering
# document is prepared through tokenization, removal of stop words
# and then Stemming and Lemmatization to reduce the number of tokens that carry out the same information and hence speed up the whole process

#                                                        Porter Stemming Algorithm for stemming
import nltk
from nltk.stem.porter import PorterStemmer
porter_stemmer = PorterStemmer()
word_data = "It originated from the idea that there are readers who prefer learning new skills from the comforts of their drawing rooms"
#                                                         First Word tokenization
nltk_tokens = nltk.word_tokenize(word_data)
#                                                          Next find the roots of the word
for w in nltk_tokens:
       print "Actual: %s  Stem: %s"  % (w,porter_stemmer.stem(w))

#                                   Lemmatization = brings context to the words by Linking words with similar meaning to one word.
import nltk
from nltk.stem import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()

word_data = "It originated from the idea that there are readers who prefer learning new skills from the comforts of their drawing rooms"
nltk_tokens = nltk.word_tokenize(word_data)
for w in nltk_tokens:
       print "Actual: %s  Lemma: %s"  % (w,wordnet_lemmatizer.lemmatize(w))



#                                                                                          Relational Databases - SqlAlchemy
# raw sql, SQL Expression Language,
# Orm - Object-relational mapping, translates data between different system types
#                                                                           Reading Relational Tables
"""
1. data replication between a master database and one or more read-only slave instances
2. advanced column types that can efficiently store semi-structured data such as JavaScript Object Notation (JSON)
3. sharding, which allows horizontal scaling of multiple databases that each serve as read-write instances at the cost of latency in data consistency
4. monitoring, statistics and other useful runtime information for database schemas and tables"""
from sqlalchemy import create_engine
engine = create_engine('sqlite:///:memory:')                 # Create the db engine
data = pd.read_csv('/path/input.csv')
data.to_sql('data_table', engine)                            # Store the dataframe as a table
#                                                              Query 1 on the relational table
res1 = pd.read_sql_query('SELECT * FROM data_table', engine)
print('Result 1')
print(res1)
print('')
#                                                             Query 2 on the relational table
res2 = pd.read_sql_query('SELECT dept,sum(salary) FROM data_table group by dept', engine)
print('Result 2')
print(res2)
#                                                                Inserting Data to Relational Tables
from sqlalchemy import create_engine
from pandas.io import sql
import pandas as pd
data = pd.read_csv('C:/Users/Rasmi/Documents/pydatasci/input.csv')
engine = create_engine('sqlite:///:memory:')
data.to_sql('data_table', engine) #        Store the Data in a relational table
# Insert another row
sql.execute('INSERT INTO data_table VALUES(?,?,?,?,?,?)', engine, params=[('id',9,'Ruby',711.20,'2015-03-27','IT')])
#                                       Read from the relational table
res = pd.read_sql_query('SELECT ID,Dept,Name,Salary,start_date FROM data_table', engine)
print(res)
#                                                        Deleting Data from Relational Tables
data = pd.read_csv('C:/Users/Rasmi/Documents/pydatasci/input.csv')
engine = create_engine('sqlite:///:memory:')
data.to_sql('data_table', engine)

sql.execute('Delete from data_table where name = (?) ', engine,  params=[('Gary')])

res = pd.read_sql_query('SELECT ID,Dept,Name,Salary,start_date FROM data_table', engine)
print(res)

#                                                                                                  NoSql Database
#                                                                                        Inserting Data
#                                   Import the python libraries
from pymongo import MongoClient
from pprint import pprint

client = MongoClient()                             # Choose the appropriate client


db=client.test                                     # Connect to the test db 

#                                              Use the employee collection
employee = db.employee
employee_details = {
    'Name': 'Raj Kumar',
    'Address': 'Sears Streer, NZ',
    'Age': '42'
}

#                                                Use the insert method
result = employee.insert_one(employee_details)

#                                                Query for the inserted document.
Queryresult = employee.find_one({'Age': '42'})
pprint(Queryresult)

#                                                                                  Updating Data
# update mode (lock type), cursor type, and cursor location.
# save any changes you have made to the current record of a Recordset object since calling the AddNew method
# or since changing any field values in an existing record. The Recordset object must support updates.
#                                                             Use the condition to choose the record and use the update method                                                
db.employee.update_one(
        {"Age":'42'},
        {
        "$set": {
            "Name":"Srinidhi",
            "Age":'35',
            "Address":"New Omsk, WC"
        }
        }
    )

Queryresult = employee.find_one({'Age':'35'})

pprint(Queryresult)

#                                                                              Deleting Data
#                                             Use the delete method
db.employee.delete_one({"Age":'35'})

Queryresult = employee.find_one({'Age':'35'})

pprint(Queryresult)

#                                                                                        date, time, calendar
#                               Date Time Representation
# Two simple examples of this format = (2007-03-04 20:32:17, 20070304T203217)
import datetime

print 'The Date Today is  :', datetime.datetime.today()

date_today = datetime.date.today()
print date_today
print 'This Year   :', date_today.year
print 'This Month    :', date_today.month
print 'Month Name:',date_today.strftime('%B')
print 'This Week Day    :', date_today.day
print 'Week Day Name:',date_today.strftime('%A')

#                                                             Date Time Arithmetic

day1 = datetime.date(2018, 2, 12)              # Capture the First Date
print 'day1:', day1.ctime()

day2 = datetime.date(2017, 8, 18)             # Capture the Second Date
print 'day2:', day2.ctime()

print 'Number of Days:', day1-day2            # Find the difference between the dates


date_today  = datetime.date.today() 
 
no_of_days = datetime.timedelta(days=4)       # Create a delta of Four Days 

before_four_days = date_today - no_of_days    # Use Delta for Past Date
print 'Before Four Days:', before_four_days 
 
after_four_days = date_today + no_of_days     # Use Delta for future Date
print 'After Four Days:', after_four_days

#                                                                          Date Time Comparison
import datetime
date_today  = datetime.date.today() 
print 'Today is: ', date_today

no_of_days = datetime.timedelta(days=4)  # Create a delta of Four Days 

before_four_days = date_today - no_of_days                                   # Use Delta for Past Date
print 'Before Four Days:', before_four_days 
after_four_days =  date_today + no_of_days
date1 = datetime.date(2018,4,4)
print 'date1:',date1              
if date1 == before_four_days :
    print 'Same Dates'
if date_today > date1:
    print 'Past Date'
if date1 < after_four_days:
    print 'Future Date'

#                                                                                                     Data Wrangling
#                          merging, grouping, concatenating
left = pd.DataFrame({
         'id':[1,2,3,4,5],
         'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
         'subject_id':['sub1','sub2','sub4','sub6','sub5']})
right = pd.DataFrame(
         {'id':[1,2,3,4,5],
         'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
         'subject_id':['sub2','sub4','sub3','sub6','sub5']})
print left
print right
# merge two data frames (datasets) horizontally with the merge function
#                                                                syntax
pd.merge(left, right, how='inner', on=None, left_on=None, right_on=None,
left_index=False, right_index=False, sort=True)

#                                                                          Grouping Data
#                                                              group the data by year and then get the result for a specific year
ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
         'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
         'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
         'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
         'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
df = pd.DataFrame(ipl_data)

grouped = df.groupby('Year')
print grouped.get_group(2014)

#                                                                                Concatenating Data
one = pd.DataFrame({
         'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
         'subject_id':['sub1','sub2','sub4','sub6','sub5'],
         'Marks_scored':[98,90,87,69,78]},
         index=[1,2,3,4,5])
two = pd.DataFrame({
         'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
         'subject_id':['sub2','sub4','sub3','sub6','sub5'],
         'Marks_scored':[89,80,79,97,88]},
         index=[1,2,3,4,5])
print pd.concat([one,two])

#                                                                                  Data Aggregation
# sum(), mean(), median(), min(), and max() = Computing Aggreations
#                                                                              Applying Aggregations on DataFrame
import numpy as np

df = pd.DataFrame(np.random.randn(10, 4),
      index = pd.date_range('1/1/2000', periods=10),
      columns = ['A', 'B', 'C', 'D'])

print df

r = df.rolling(window=3,min_periods=1)
print r

#                                       Apply Aggregation on a Whole Dataframe
df = pd.DataFrame(np.random.randn(10, 4),
      index = pd.date_range('1/1/2000', periods=10),
      columns = ['A', 'B', 'C', 'D'])
print df

r = df.rolling(window=3,min_periods=1)
print r.aggregate(np.sum)

#                                                     Apply Aggregation on a Single Column of a Dataframe
#                          Spark data frames provide an agg() 
# where you can pass a Map [String,String] (of column name and respective aggregate operation ) as input
df = pd.DataFrame(np.random.randn(10, 4),
      index = pd.date_range('1/1/2000', periods=10),
      columns = ['A', 'B', 'C', 'D'])
print df
r = df.rolling(window=3,min_periods=1)
print r['A'].aggregate(np.sum)

#                                                 Apply Aggregation on Multiple Columns of a DataFrame
df = pd.DataFrame(np.random.randn(10, 4),
      index = pd.date_range('1/1/2000', periods=10),
      columns = ['A', 'B', 'C', 'D'])
print df
r = df.rolling(window=3,min_periods=1)
print r[['A','B']].aggregate(np.sum)

#                                                         Reading HTML Pages
#  Beautiful Soup is a library that makes it easy to scrape information from web pages
#                         Reading the HTML file
import urllib2
from bs4 import BeautifulSoup
#                                                                               Fetch the html file
response = urllib2.urlopen('http://kaashiv.com/python/python_overview.htm')
html_doc = response.read()
#                                                                              Parse the html file
soup = BeautifulSoup(html_doc, 'html.parser')
#                                                                              Format the parsed html file
strhtm = soup.prettify()
#                                                                             Print the first few characters
print (strhtm[:225])

#                                                             Extracting Tag Value
import urllib2
from bs4 import BeautifulSoup

response = urllib2.urlopen('http://kaashiv.com/python/python_overview.htm')
html_doc = response.read()

soup = BeautifulSoup(html_doc, 'html.parser')

print (soup.title)
print(soup.title.string)
print(soup.a.string)
print(soup.b.string)

#                                                                 Extracting All Tags
import urllib2
from bs4 import BeautifulSoup

response = urllib2.urlopen('http://kaashiv.com/python/python_overview.htm')
html_doc = response.read()
soup = BeautifulSoup(html_doc, 'html.parser')

for x in soup.find_all('b'): print(x.string)




#                                                                                                        DocStrings
# Doc strings are carried with executing code
# We can use triple-quoting to create doc strings that span multiple lines
def foo():                                                                      # docstring tool
""" """
pass
class Data:
   """ """
print(foo.__doc__)
print(Data.__doc__)                                                          # Accessing docstrings
#                                                $  Working with files
With open("myfile.txt", "w") as myfile:
Print(“Hello!”,file=myfile)

With open(‘myfile.txt’, ‘w’) as myfile:
myfile.write(“Hello!”)

With open(‘myfile.txt’, ‘r’) as myfile:
data = myfile.read()

#                                                                                                                              # Load Iris Datasets
from sklearn.datasets import load_iris

iris = load_iris()
iris
x = iris.data
x[0]
#                                                                                                                        Create Histogram using Iris Data Sets
iris.feature_names  #
iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)                     # create Data-Frames
iris_df['sepal length (cm)'].hist(bins=30)                                        # draw the Histogram
#                                                                                                                         simulated Data for Classification
from sklearn.datasets import make_classification
features, output = make_classification(n_samples=100, n_features=10, n_informative=5, n_redundant=5, n_classes=3, weights=[.2, .3, .8])
pd.DataFrame(features).head()
#                                                                                                                            simulated Data for Clustering
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

X, y = make_blobs(n_samples=200, n_features=2, centers=3, cluster_std=0.5, shuffle=True)
plt.scatter(X[:, 0], X[:, 1])
#                                                                                                                         simulated Data for Regression
from sklearn.datasets import make_regression
from matplotlib import pyplot

X, y = make_regression(n_samples=100, n_features=1, noise=0.1)                       # generate regression datasets
pyplot.scatter(X, y)                                                                 # plot regression datasets
pyplot.show()
#                                                                                                                                 dot product of Matrix
import numpy as np

vector_a = np.array([1, 2, 3])                       # create vector
vector_b = np.array([4, 5, 6])
np.dot[vector_a, vector_b]
vector_a @ vector_b                                  # calculate dot product

# list of values are added & divided by the total no of columns                                                                   mean-Manipulation

import pandas as pd
from scipy import stats
data = {
   'name': ['Abith', '',
            '', 'Abi',                                              # create dataframe with two values
            '', 'Raj'],
   "ID": [6, 1, 9]
   }
df = pd.DataFrame(data)
df                                                                # create mean & trim data
df['ID'].nean()                                                       # calc_non-trimmed mean value
stats.trim_mean(df['score'], proportiontocut=0.2)                                            # trim off the 20 % scores
stats.trimboth(df['score'], proportiontocut=0.2)             # trim off the 20 % scores & view non-trimmed mean values

stats.trim1(df['score'], proportiontocut=0.2, tail="right").mean()                   # trim specific data
stats.trim1(df['name'], proportiontocut=0.2, tail="right")
trim(DataFrameColumn, RemovePercentage, remove(data).mean()                                           # calculate mean
                                                                                                                          # probability mass function
import matplotlib.pyplot as plt;
data = [6,1,9];                                                       # create Dictionary = data + key value pair
count = {}
for observation in data:                                                              # create Dictionary
   count[observation] = count.get(observation, 0) + 1
   n = len(data)
probability_mass_function = {}                                      # initialize the dictionary
for unique_value, count in count.items():                                        # create probability_mass_function
   probability_mass_function[unique_value] = count /n  # loop through unique values of array & calculate probability_mass_function
plt.bar(list(columns), prob.values(), color='g')                       # plot probability_mass_function
plt.show():

#                                                                $ Data Operations using numpy
numpy.array()

a = np.array([[1, 2], [3, 4]])
print (a)
# minimum dimensions
a = np.array([1, 2, 3,4,5], ndmin = 2)
print a
#                                                                     dtype parameter
a = np.array([1, 2, 3], dtype = complex)
print a
#                                              Series in pandas
#
pandas.Series( data, index, dtype, copy)    # series = 1d array's
data = np.array(['a','b','c','d'])
s = pd.Series(data)
print s
# pandas data = series, dataFrame, panel, size-mutable, heterogeneous tabular data
# Labeled axis (rows, columns)
# labels must be hashable type, label-indexing
# axis labels = index
pandas.DataFrame( data, index, columns, dtype, copy)
data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}  #  Data Operations in Pandas
df = pd.DataFrame(data, index=['rank1','rank2','rank3','rank4'])
print df
# panel = 3D container of Data
# transform wide format into long(stacked) as DataFrames
# column = panel items, index = panel's major and minor axis
#pandas - pan(el)-da(ta)-s
pandas.Panel(data, items, major_axis, minor_axis, dtype, copy)
data = {'Item1' : pd.DataFrame(np.random.randn(4, 3)),
       'Item2' : pd.DataFrame(np.random.randn(4, 2))}
p = pd.Panel(data)
print p

#                                                                                              Python Data Cleansing & Missing datas
# using re indexing create dataframe With missing values
# NAN = not an number
df = pd.DataFrame(np.random.randn(5, 3), index=['a', 'c', 'e', 'f',
                                               'h'],columns=['one', 'two', 'three'])
df = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
print df
# check for missing values = isnull(0, NOTNULL()
df = pd.DataFrame(np.random.randn(5, 3), index=['a', 'c', 'e', 'f',                         # Check for Missing Values
                                               'h'],columns=['one', 'two', 'three'])
df = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
print df

df = pd.DataFrame(np.random.randn(5, 3), index=['a', 'c', 'e', 'f',
                                               'h'],columns=['one', 'two', 'three'])
df = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
print df['one'].isnull()
#                                                                                      CLEANING / FILLING MISSING DATA
df = pd.DataFrame(np.random.randn(3, 3), index=['a', 'c', 'e'],columns=['one',
                                                                       'two', 'three'])
df = df.reindex(['a', 'b', 'c'])                             # Replace NaN with a Scalar Value
print df
print ("NaN replaced with '0':")  # replace "NAN" with "0"
print df.fillna(0)  # "fill" in NA values with non-null data
# pad/fill = fill forward
# bfill/backfill = fill backwards
df = pd.DataFrame(np.random.randn(5, 3), index=['a', 'c', 'e', 'f',                    # Fill NA Forward and Backward
                                               'h'],columns=['one', 'two', 'three'])
df = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
print df.fillna(method='pad')
# dropNA()
df = pd.DataFrame(np.random.randn(5, 3), index=['a', 'c', 'e', 'f',                      # Drop Missing Values
                                               'h'],columns=['one', 'two', 'three'])
df = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
print df.dropna()
# replace({1000:6,2000:1,3000:9})
df = pd.DataFrame({'one':[10,20,30,40,50,2000],                     # Replace Missing (or) Generic Values
                  'two':[1000,0,30,40,50,60]})
print df.replace({1000:10,2000:60})
#                                                                                                              Analyze baby name trends with Data Science
Mary,F,7065
Anna,F,2604
Emma,F,2003
Elizabeth,F,1939
Minnie,F,1746
Margaret,F,1578
Ida,F,1472
Alice,F,1414
Bertha,F,1320
Sarah,F,1288
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("darkgrid")
names1880 = pd.read_csv("./babynames/yob1880.txt",
                       names=["name", "sex", "births"])
names1880.head()
names1880.groupby("sex").sum()
years = range(1880, 2019)
pieces = []
columns = ["name", "sex", "births"]
for year in years:
   path = rf"./babynames/yob{year}.txt"
   frame = pd.read_csv(path, names=columns)
   frame['year'] = year
   pieces.append(frame)
names = pd.contact(pieces, ignore_index=True)
names.head()
plt.figure(figsize=(15, 8))_ = sns.barplot(y-names.groupby("year").sum().values[-10:].rave1(), x=list(years)[-10:])
plt.ylabel("number of births")
plt.xlabel("year")_ - plt.title("number of births- (2009-2018)")

#                                                                                                                          Projects
#                                                       GUI Based Encryption & Decryption
from tkinter import *
top=Tk()
L1=Label(top,text="UserName")
L1.grid(column=0,row=0)                           # grid = window

E1=Entry(top,bd=5)
E1.grid(column=1,row=0)
alphabet ='abcdefghijklmnopqrstuvwxyz'
key = 4
newmsg= ''
E2=Entry(top,bd=5)                                # border = 5
E2.grid(column=2,row=0)

def submit():
    messagebox.showinfo( "CONFIRMATION",E1.get()+"- Your Data")     # def messagebox
    global newmsg
    for character in E1.get():
        position = alphabet.find(character)
        newposition = (position+key)%26    # (-) for decryption
        newchar = alphabet[newposition]
        print("Encrypted new character is ",newchar)
        newmsg+=newchar
print(newmsg)
E2.insert(0, newmsg)
redbutton=Button(top,text="Abith Button",fg="red" ,command=submit) # colorbutton
redbutton.grid(column=1,row=1)
top.mainloop()
#                                                                                                                 image Processing
from PIL import image
import glob
image_list = []
for filename in glob.glob("/run/media/abith/Abith/py/my.jpg"):
    im=image.open("/run/media/abith/Abith/py/my.jpg")
    image.show();
#                                                                             tRANSPOSING iMAGE
transposed_img = image.transpose(Image.FLIP_LEFT_RIGHT)
#                                                                              Save  transposed image
transposed_img.save("transposed.jpg")
transposed_img.show()
# 
from PIL import image
image = image.open("my.jpg")  # import image
width, height = image.size  # finding Size
area = (0, 0, width/2, height/2) 
img = image.crop(area)       # cropping
img = image.resize((int(width/4), int(height/4)))                # Resizing the Image
#           Saved in same Relative Location
img.save("cropped_picture.jpg")
img.show();

# 

#                                                                                                                   R programing...
print(sample=(1:3)) # Generate series of sample values in a given rage
print(sample=(1:3, size=3, prob=c(1,3), replace=False))                    # With duplicate values = True
#                                                         prob = probability
#                                                       Already In-Built Datasets
print(head(mtcars))
#                                                         Generating the Datasets
print(matrix(runif(6*3), nrow=6, ncol=3))
input <-mtcars[,c("mpg","disp","hp","wt")]
print(head(input))

input <-mtcars[,c("mpg","disp","hp","wt")]
model <-lm(mpg~disp+hp+wt,data=input) # intercept(mpg)
print(model)
cat("####the co-efficient values are","\n")
a<-coef(model)[1]
print(a)
Xdisp<-coef(model)[2]
Xhp<-coef(model)[3]
Xwt<-coef(model)[4]
print(Xdisp)
print(Xhp)
print(Xwt)
#                                    for a car with disp = 221, hp = 102, wt = 2.91 The predicted Milleage is,,,,,............
Y = a + X1.Xdisp + X2.Xhp + X3.Xwt
Y = 37.105505 + (221*-0.000937) + (102* -0.0.32257) + (2.91* -3.8008g1)
