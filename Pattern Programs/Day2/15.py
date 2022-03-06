n=5
for i in range(n-1, -1, -1):
    for j in range(n-i-1):
        print(" ", end=" ")
    for j in range(i, -1, -1):
        print(n-j, end=" ")
    for j in range(i, -1, -1):
        print(n-j, end=" ")
    print()