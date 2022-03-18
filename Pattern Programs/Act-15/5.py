"""Write a program that reads integers from the user and stores them in a list. Use 0 as a sentinel 
value to mark the end of the input. Once all of the values have been read your program should 
display them (except for the 0) in reverse order, with one value appearing on each line"""
x=[]
while True:
    try:
        line = input('enter a number: ')
        if line == '0':
            break
        x.append(line)
    except:
        pass
def Reverse(x):
	x.reverse()
	return x
a=(Reverse(x))
print(*a, sep = "\n")