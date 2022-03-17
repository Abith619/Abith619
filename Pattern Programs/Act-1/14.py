""" """
n = None    
nums = []    
while True:
    n = input("Enter number: ")
    if n == "":
        for i in nums:
            print(i)
        break
    else:
        nums.append(n)
print(list(sorted(nums)))
