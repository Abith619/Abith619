n = 7
for i in range(5):
    for j in range(5-i):
        print(i+1)
    k=n-j
    for i in range(0, i+1):
        for j in range(0, i):
            print("*")
        for j in range(0, k):
            print(n-j)