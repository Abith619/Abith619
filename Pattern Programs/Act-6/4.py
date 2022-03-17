"""Write a function that takes two positive integers that represent the numerator and
denominator of a fraction as its only two parameters. The body of the function
should reduce the fraction to lowest terms and then return both the numerator and
denominator of the reduced fraction as its result. For example, if the parameters
passed to the function are 6 and 63 then the function should return 2 and 21.
Include a main program that allows the user to enter a numerator and denominator.
Then your program should display the reduced fraction."""
from functools import reduce
def gcd(n,m):
   d =  min (n,m)
   while  n%d!= 0 or m%d!=0:
      d = d-1
   return d
def reduce(num,den):
   if num == 0:
      return  (0,   1)
   g =  gcd(num,den)
   return  (num//g,den//g)
num = int(input("Enter a numerator:"))
den = int(input("Enter a denomenator:"))
(n,d) = reduce(num,den)
print ("%d/%d can be reduced to  %d/%d." % (num,den,n,d))