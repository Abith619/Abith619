"""A palindromic prime is a prime number and also palindromic. For example, 131 is a prime and also a 
palindromic prime, as are 313 and 757. Write a program that displays the first 100 palindromic prime 
numbers. Display 10 numbers per line, separated by exactly one space, as follows:
 2 3 5 7 11 101 131 151 181 191 
313 353 373 383 727 757 787 797 919 929"""
def palindrome(num):
    return str(num) == str(num)[::-1]

def is_prime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  f = 5
  while f <= r:    
    if n%f == 0: return False
    if n%(f+2) == 0: return False
    f +=6
  return True

N = int(input("Enter the start point N: "))
M = int(input("Enter the end point M: "))

for x in range(N, M):

    if palindrome(x) and is_prime(x):

        if abs(x)%2 != 0 and abs(x)%3 != 0 and abs(x)%5 != 0 and  abs(x)%7 != 0:
            
            print(x, end=" ")
