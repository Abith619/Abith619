numgames = {}
numgames[(1,2,4)]=8
numgames[(4,2,1)]=10
numgames[(1,2)]=12

sum = 0 
print(numgames)

for k in numgames:
    print(k)
    sum += numgames[k]
print(len(numgames)+sum)
