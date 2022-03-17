"""Write a Python program to filter a list of integers using Lambda"""
Original = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Even = [2, 4, 6, 8, 10]
Odd = [1, 3, 5, 7, 9]
evenNumbers = list(filter(lambda x: x%2 == 0, Original))
print(evenNumbers)
oddNumbers = list(filter(lambda x: x%2 != 0, Original))
print(oddNumbers)