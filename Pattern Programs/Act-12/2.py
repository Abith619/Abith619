"""Create a program that adds line numbers to a file. The name of the input file will be read 
from the user, as will the name of the new file that your program will create. Each line in the 
output file should begin with the line number, followed by a colon and a space, followed by the 
line from the input file"""
with open('123.txt') as fh:
    for i, line in enumerate(fh):
        print('%d) %s'%(i+1, line))