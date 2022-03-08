""" """
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
    print(sorted(i))
