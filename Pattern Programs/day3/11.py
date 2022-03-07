"""n=5
for i in range(n):
    for j in range(i+1):
        x=0
        for k in range(j):
            x=x+n-k
        if j%2==0:
            print(x+j+i+1, end=" ")
        else:
            print(x+i+j, end=" ")
    print()"""
n=5
num=1
for i in range(1, n+1):
    for j in range(1, i+1):
        print(num, end=" ")
        num=num+1
    print()