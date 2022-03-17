# Write a Python program to sum all the items in a dictionary
dict = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def Sum(myDict):
    list = []
    for i in myDict:
        list.append(myDict[i])
    final = sum(list)     
    return final
print("Sum =", Sum(dict))