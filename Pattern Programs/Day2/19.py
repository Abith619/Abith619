for i in range(5):
    for j in range(i+1):
        if i == j:
            print(i, end=" ")
        else:
            print(0, end=" ")
    print()