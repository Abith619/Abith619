n = 5
for i in range(5):
    for j in range(n - i - 1, -1, -1):
        print(n - j, end=" ")
    for j in range(i + i):
        print(" ", end=" ")
    for j in range(n - i):
        print(n - j, end=" ")
    print()


