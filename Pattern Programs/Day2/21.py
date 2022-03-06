n=5
for i in range(n):
    for j in range(n-i-1, -1, -1):
        print(n-j, end=" ")
    for j in range(4-i-1, -1, -1):
        print(j+1, end=" ")
    print()