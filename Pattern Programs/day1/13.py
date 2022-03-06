k=65
for i in range(0, k+1):
    for j in range(0, i, 1):
        print(" ", end=" ")
    for j in range(0, k*2-i, 1):
        if k%2==0:
            print(chr(k+i))
        else:
            print(k-i)