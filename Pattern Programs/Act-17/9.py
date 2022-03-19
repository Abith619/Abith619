"""Write a test program that prompts the user to enter ten numbers, invokes this method to return the 
minimum value, and displays the minimum value. Here is a sample run of the program: 
Enter ten numbers: 1.9 2.5 3.7 2 1.5 6 3 4 5 2 
The minimum number is: 1.5"""
nums = []    
while True:
    n = float(input("Enter float numbers "))
    if n == '':
        break
    else:
        nums.append(int(n))
    print(min(nums))