""" Write a function that takes three numbers as parameters, and returns the median
value of those parameters as its result. Include a main program that reads three
values from the user and displays their median."""
import statistics

n=float(input())
n1=float(input())
n2=float(input())
print(statistics.median([n, n1, n2, 18]))