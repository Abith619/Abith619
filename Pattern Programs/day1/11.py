for i in range(5):
    for j in range(5, -1, -1):
        print(" ", end=" ")
    for j in range(0, i+1):
        print(j+1, end="")
    print()