"""Write a program that prompts the user to enter a letter grade A, B, C, D, or F and displays 
its corresponding numeric value 4, 3, 2, 1, or 0. Here is a sample run
Enter a letter grade: B 
The numeric value for grade B is 3 
Enter a letter grade: T 
T is an invalid grade"""
n=input("Enter a letter grade: ")
dict={
    "A":4, "B":3, "C":2, "D":1, "F":0
}
if n in dict:
    print(dict.get(n))
else:
    print("Invalid Grade")