"""(Assign grades) Write a program that reads student scores, gets the best score, and then assigns grades 
based on the following scheme: Grade is A if score is Ú best - 10 Grade is B if score is Ú best - 20; 
Grade is C if score is Ú best - 30; Grade is D if score is Ú best - 40; Grade is F otherwise. The program 
prompts the user to enter the total number of students, then prompts the user to enter all of the scores, 
and concludes by displaying the grades. Here is a sample run 
Enter the number of students: 4
Enter 4 scores: 40 55 70 58 
Student 0 score is 40 and grade is C 
Student 1 score is 55 and grade is B 
Student 2 score is 70 and grade is A 
Student 3 score is 58 and grade is B"""
a=int(input("Enter the number of students: "))
b=int(input("Enter {} scores: ".format(a)))
def determine_grade(scores):
    if scores >= 90 and scores <= 100:
        return 'A'
    elif scores >= 80 and scores<= 89:
        return 'B'
    elif scores >= 70 and scores<= 79:
        return 'C'
    elif scores >= 60 and scores<= 69:
        return 'D'
    elif scores >= 50 and scores<= 59:
        return 'E'
    else:
        return 'F'
print("Student 1 score is {} and grade is = ".format(b), (determine_grade(b)))