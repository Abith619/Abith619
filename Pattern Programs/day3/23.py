"""n=5
for i in range(n):
    for j in range(i+1):
        if i==j:
            print(" ", end=" ")
        else:
            print(j+i)"""
n=5
for i in range(n):
    for j in range(i, -1, -1):
        print(j+1, end=" ")
    print()
    for j in range(i+1):
        print(j+1, end=" ")
    