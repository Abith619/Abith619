"""Write a program that reads numbers from the user until a blank line is entered. Your program
should display the average of all of the values entered by the user. Then the program should 
display all of the below average values, followed by all of the average values (if any), 
followed by all of the above average values. An appropriate label should be displayed before each list of values"""
    
nums = []    
while True:
    n = input("Enter number: ")
    if n == "":
        break
    else:
        nums.append(int(n))
avg = sum(nums)/len(nums)
print(avg)
below = []
equal= []
above = []
for bel in nums:
    if bel < avg:
        below.append(bel)
    elif bel == avg:
        equal.append(bel)
    else:
        above.append(bel)
print("GPAs below Avg:", below)
print("GPAs above Avg:", above)
print("GPAs equal to Avg:", equal)