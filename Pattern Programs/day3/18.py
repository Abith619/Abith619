n=5
for i in range(n):
    for j in range(n-1, -1, -1):
        print(j-1, end=" ")
    for j in range(i+1):
        print(j+1, end=" ")
    for j in range(i, -1, -1):
        print(j+1, end=" ")
    for j in range(i+1):
        print(j-1, end=" ")
    print()