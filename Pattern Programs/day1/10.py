n = 5
num = 15
for i in range(n):
    for j in range(4-i, 0, -1):
        print(" ", end=" ")
    for j in range(i+1):
        print(num, end=" ")
        num=num-1
        print(" ")