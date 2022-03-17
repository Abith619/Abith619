"""A prime number is an integer greater than 1 that is only divisible by one and itself.Write a
function that determines whether or not its parameter is prime, returning True if it is, and 
False otherwise. Write a main program that reads an integer from the user and displays a message 
indicating whether or not it is prime. Ensure that the main program will not run if the file 
containing your solution is imported into another program"""
n=int(input())
if n > 1:
    for i in range(2, int(n/2)+1):
        if (n % i) == 0:
            print(n, "is not prime number")
            break
    else:
        print(n, "is prime number")
else:
    print(n, "is not prime number")