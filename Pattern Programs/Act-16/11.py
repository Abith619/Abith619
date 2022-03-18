"""Write a program that prompts the user to enter a string and displays the characters at odd positions. 
Here is a sample run: 
Enter a string: Beijing Chicago 
BiigCiao"""
number_of_strings = int(input("Enter no of strings: "))
for line in range(number_of_strings):
    string = input("Enter string: ")
    even_string = ""
    odd_string = ""
    for i in range(len(string)):
        if i%2==0:
            even_string = even_string  + string[i]
        else:
            odd_string = odd_string + string[i]
    print(even_string, odd_string)