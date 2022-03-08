""" """
n = None    
num = []    
while True:
    n = input("Enter number: ")
    if n == "":
        for i in num:
            print(i)
        break
    else:
        num.append(n)
print(list(sorted(num)))