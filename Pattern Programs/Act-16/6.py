"""Write a program that prompts the user to enter three cities and displays them in ascending order. 
Here is a sample run:
Enter the first city: Chicago
Enter the second city: Los Angeles 
Enter the third city: Atlanta 
The three cities in alphabetical order are Atlanta Chicago Los Angeles"""
city1=input()
city2=input()
city3=input()
a=city1, city2, city3
print(sorted(a))