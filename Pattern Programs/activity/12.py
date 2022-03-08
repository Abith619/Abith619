"""Write a program that reads integers from the user and stores them in a list. 
Use 0 as a sentinel value to mark the end of the input. Once all of the values have been read 
your program should display them (except for the 0) in reverse order, with one value
appearing on each line."""


number = 0
while True:
    i = input()
    if i == "":
        number += 1
        if number == 1:
            break
    else:
        number = 0
        pass
    sorted(i)
