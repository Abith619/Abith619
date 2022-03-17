# Write a program in python to calculate matrix of addition
matrix1 = [[12,7,3],
		[4 ,5,6],
		[7 ,8,9]]
matrix2 = [[5,8,1],
		[6,7,3],
		[4,5,9]]
result = [[matrix1[i][j] + matrix2[i][j]  for j in range
(len(matrix1[0]))] for i in range(len(matrix1))]
for r in result:
    print(r)