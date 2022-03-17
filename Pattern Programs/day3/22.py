n=5
for i in range(0, n):
    for j in range(i, -1, -1):
        print(n-j, end=" ")
    print()
    for j in range(i+1):
        print(n-j, end=" ")
    