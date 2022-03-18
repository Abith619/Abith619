"""Write a program that prompts the user to enter two characters and displays the major and status 
represented in the characters. The first character indicates the major and the second is number character
1, 2, 3, 4, which indicates whether a student is a freshman, sophomore, junior, or senior. Suppose the 
following characters are used to denote the majors: 
M: Mathematics
 C: Computer Science
 I: Information Technology 
Enter two characters: M1 
Mathematics Freshman 
Enter two characters: C3 
Computer Science Junior 
Enter two characters: T3 
Invalid input """

n=input("Enter a Group ")
a=input("Enter a Number ")
dict1={
    'M':"Mathematics", 'C':"Computer_Science", 'I':"Information_Technology"
}
if n in dict1:
    print(dict1[n], end=" ")
else:
    print("Invalid")
dict={
    '3':"Junior", '1':"Freshman", '2':"sophomore", '4':"Senior", '5':"Intermediate"
}
if a in dict:
    print(dict[a])
else:
    print("Invalid")