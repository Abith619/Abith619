"""write a python program for this pattern:
                                                            1
                                                         1 2 1
                                                      1 2 4 2 1  
                                                  1 2 4 8 4 2 1 
                                               1 2 4 8 16 8 4 2 1
                                           1 2 4 8 16 32 16 8 4 2 1
                                      1 2 4 8 16 32 64 32 16 8 4 2 1
                                 1 2 4 8 16 32 64 128 64 32 16 8 4 2 1 """
def palindromicPyramid(rows):
    for i in range(0,rows+1):
        for j in range(i,rows+1):
                print(" ", end=" ")
        for j in range(1,i+1):
            print(j**2,end=" ")
        for j in range(i-1,0,-1):
            print(j**2,end=" ")
        print()
n=int(input("Enter the number of rows :"))
palindromicPyramid(n)