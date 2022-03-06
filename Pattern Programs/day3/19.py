for i in range(5):
    for j in range(i, -1, -1):
        print(" ", end=" ")
    for j in range(i+1):
        print(j**2, end=" ")
    for j in range(i-1, -1, -1):
        print(j+1, end=" ")
    print()
