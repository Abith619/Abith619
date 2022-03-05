for i in range(5):
    for j in range(i+2):
        print(j+2, end=" ")
    for j in range(j+2):
        print(i+2, end=" ")
    print()