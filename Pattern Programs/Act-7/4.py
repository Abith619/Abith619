"""Write a simple Python class named Student and display its type. Also, display the __dict__ 
attribute keys and the value of the __module__ attribute of the Student class."""
class Student:
    def student(student_id, student_name, student_class):
        return f'Student ID: {student_id} \n Student Name: {student_name} \n Class: {student_class}'  
    print(student('S619', 'Abith Raj', 'BE'))
print(type(Student))
print(Student.__dict__.keys())
print(Student.__module__)