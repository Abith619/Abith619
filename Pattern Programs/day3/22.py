n=5
for i in range(n):
    for j in range(n, -i, -1):
        print(j+i, end=" ")
    for j in range(i+1):
        print(j+i, end=" ")
    print()