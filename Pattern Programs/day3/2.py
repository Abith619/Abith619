n = 5
for i in range(n):
    for j in range(n):
        x = 0
        for k in range(j):
            x = x + n - k
        if j % 2 == 0:
            print(x + i - j + 1, end=" ")
        else:
            print(x + n - i, end=" ")
    print()