# Write a Python program to get the maximum and minimum value in a dictionary
dic1 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

temp = max(dic1.values())
res = [key for key in dic1 if dic1[key] == temp]
print("Keys with maximum value is : " + str(res))

temp = min(dic1.values())
res = [value for value in dic1 if dic1[value] == temp]
print("Keys with minimum value is : " + str(res))