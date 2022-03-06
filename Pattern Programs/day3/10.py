for i in range(5):
    for j in range(5-i):
        print(i+1, end=" ")
    print()
for i in range(0, i, -1):
    for j in range(1, i):
        print(" ", end=" ")
    for j in range(0, j):
        print(i-j, end=" ")