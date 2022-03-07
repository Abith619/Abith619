n=5
for i in range(n):
    for j in range(n, 1, -1):
        if i==j:
            print("*")
        else:
            print(j, end=" ")