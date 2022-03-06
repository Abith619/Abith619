n=5
for i in range(n):
    for j in range(i+1):
        x=0
    for j in range(j):
        x=x+n-j
        if j%2==0:
            print(x+i-j+1, end=" ")
        else:
            print(x+n-i, end=" ")
    print()