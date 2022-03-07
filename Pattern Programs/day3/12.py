n=5
for i in range(n):
    for j in range(i+1):
        x=0
        for k in range(j):
            x=x+n-k
        if j%2==0:
            print(x+i-j+1, end=" ")
        else:
            print(x+i+j, end=" ")
    print()