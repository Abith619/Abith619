for i in range(5):
    for j in range(i-1, -1, -1):
        print(j-1, end=" ")
    for j in range(4):
        print(j-1, end=" ")
    for j in range(i-2, -1, -1):
        print(i-j, end=" ")
    for j in range(4-i-1):
        print(j+1, end=" ")
    print()