"""Write a program that reads numbers from the user until a blank line is entered. Your program
 should display the average of all of the values entered by the user. Then the program should display all of the below average values, followed by all of the average values (if any), followed by all of the above average values. An appropriate
label should be displayed before each list of values"""

def averages():
    def Average(lst):
        try:
            return (sum(lst)-0)/(len(lst)-1)
        except ZeroDivisionError:
            return 0
    nums=[]
    while 0 not in nums:
        nums.append(int(input("Please input numbers and type 0 to find the average")))
    mean=Average(nums)
    print(nums)
    print(mean)
averages()