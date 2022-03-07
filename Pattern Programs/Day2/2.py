n=5
for i in range(n):
    for j in range(n, -1, -1):
        print("", end="")
    print()
    for j in range(0, i+1):
        print(j+1, end=" ")
    for j in range(n-i-1):
        print(j+1, end="")