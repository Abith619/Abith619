n=5
for i in range(0, n):
    for j in range(n-i-1, -1, -1):
        print(j+2, end="")
    for j in range(i):
        print(j+2, end=" ")
    print()