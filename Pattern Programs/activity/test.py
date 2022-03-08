"""def average():
    # x=a+b+c+d+e
     x=x/5
     print("the average of your numbers is: " +x+ ".")"""
"""
num =input()
average = sum(num) / len(num)

for i in range (5):
    userInput = int(input("Enter a number: "))
    num.append(userInput)
    print(num)
average(num)"""
"""
n=int(input("Enter the number of elements to be inserted: "))
a=[]
for i in range(0,n):
    elem=int(input("Enter element: "))
    a.append(elem)
avg=sum(a)/n
print("Average of elements in the list",round(avg,2))"""

def averages():
    def Average(lst):
        try:
            return (sum(lst)-0)/(len(lst)-1)
        except ZeroDivisionError:
            return 0
    nums=[]
    while 0 not in nums:
        nums.append(int(input("Please input numbers and type 0 when you wish to find the average if the numbers inputted")))
    mean=Average(nums)
    print(nums)
    print(mean)

averages()