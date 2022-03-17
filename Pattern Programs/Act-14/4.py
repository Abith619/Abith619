"""Create a program that sums all of the numbers entered by the user while ignoring
any lines entered by the user that are not valid numbers. Your program should dis-
play the current sum after each number is entered. It should display an appropriate
error message after any invalid input, and then continue to sum any additional num-
bers entered by the user. Your program should exit when the user enters a blank
line. Ensure that your program works correctly for both integers and floating point
numbers."""
x=[]
while True:
    try:
        line = input('enter a number: ')
        if line == '':
            break
        x.append(float(line))
    except:
        pass
print(sum(x)/len(x))