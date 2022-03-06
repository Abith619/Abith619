n=6
for i in range(1, 6):
    for j in range(n-i-1):
        print(j+1, end=" ")
    for j in range(i-1-1):
        print(j+1, end=" ")
    print()