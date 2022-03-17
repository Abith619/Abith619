"""Unix-based operating systems usually include a tool named head. It displays the first 10 lines 
of a file whose name is provided as a command line parameter. Write a Python program that provides 
the same behavior. Display an appropriate error message if the file requested by the user does 
not exist or if the command line parameter is omitted"""
with open("123.txt") as myfile:
    head = [next(myfile) for x in range(0, 10)]
print(head)