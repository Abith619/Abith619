for i in range(5):
    for j in range(5, -i, -1):
        print(" ", end=" ")
    for j in range(i+1):
        print(j+1, end=" ")
    print()