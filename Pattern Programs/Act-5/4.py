"""Words like first, second and third are referred to as ordinal numbers. In this exercise, 
you will write a function that takes an integer as its only parameter and returns a string 
containing the appropriate English ordinal number as its only result. Your function must handle 
the integers between 1 and 12 (inclusive). It should return an empty string if a value outside 
of this range is provided as a parameter. Include a main program that demonstrates your function 
by displaying each integer from 1 to 12 and its ordinal number. Your main program should only 
run when your file has not been imported into another program"""

num=int(input())
SUFFIXES = {1: 'st', 2: 'nd', 3: 'rd'}
def ordinal(num):
    if num <= 12:
        suffix = 'th'
        suffix = SUFFIXES.get(num % 10, 'th')
        output = str(num) + suffix
    else :
        output = "out of range"
    return output
print(ordinal(num))