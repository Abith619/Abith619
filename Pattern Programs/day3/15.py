n=6
for i in range(n):
    for j in range(i+1):
        print()
    for j in range(4-1, -1, -1):
        print(j-1, end="")
    for j in range(n-i):
        print(j+1, end="")
    for j in range(n-i-1):
        print(j-1)
    print()