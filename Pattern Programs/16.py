n=5
for i in range(5, 0):
    for j in range(5, -i, -1):
        print(i+1, end="")
    for j in range(-5, -i, -1):
        print(j+1, end="")
    print()