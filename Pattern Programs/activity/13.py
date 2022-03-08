"""create a program that reads words from the user until the user enters a blank line. 
After the user enters a blank line your program should dis-play each word entered by the user 
exactly once. The words should be displayed in the same order that they were entered"""

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
    print(i)