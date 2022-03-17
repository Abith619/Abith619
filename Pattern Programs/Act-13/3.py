"""(The Location class) Design a class named Location for locating a maximal value and its 
location in a two-dimensional array. The class contains public data fields row , column , and 
maxValue that store the maximal value and its indices in a two-dimensional array with row and 
column as int types and maxValue as a double type.
Write the following method that returns the location of the largest element,The return value is 
an instance of Location . Write a test program that prompts a two-dimensional array and displays 
the location of the largest element in the array. Here is a sample run:
array:
23.5  35  2   10
4.5    3  45  3.5
35    44  5.5  9.6
The location of the largest element is 45 at (1, 2)"""
import array as arr
import numpy as np

class location:
    def loc(self, arr, row , column , maxvalue):
        self.arr=arr
        self.row=row
        self.column=column
        self.maxvalue=maxvalue
arr=[[23.5,  35,  2,   10],
    [4.5,    3,  45,  3.5],
    [35,    44,  5.5,  9.6]]
maxval=np.max(arr)
print(maxval)
import numpy

arr2D=[[23.5,  35,  2,   10],
    [4.5,    3,  45,  3.5],
    [35,    44,  5.5,  9.6]]
result = numpy.where(arr2D == numpy.amax(arr2D))
print('Index of maximum value in array : ')
location = list(zip(result[0], result[1]))
for index in location:
    print(index)