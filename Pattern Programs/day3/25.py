i=0
while i<5:
    print(" " * (4 - i), end=" ")
    j=0
    k=0
    while j-1 < i*2:
        if j>i:
            print(i-k, end=" ")
            k+=1
        else:
            print(j+i+1, end=" ")
        j+=1
    print()
    i+=1