n=5
for i in range(n):
    for j in range(i, -1, -1):
        print(i+1, end=" ")
        for j in range(n-i):
            print(n-i, end=" ")
    print()