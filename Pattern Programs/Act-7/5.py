"""Write a Python class named Student with two attributes student_id, student_name. Add a new 
attribute student_class. Create a function to display the entire attribute and their values 
in Student class"""

import inspect

class student():
    student_id = 'S619'
    student_name = 'Abith Raj'
    def display():
        return f'Student id: {student.student_id}\nStudent Name: {student.student_name}'
    print("Original attributes and their values of the Student class:")
print(type(student))
print(inspect.signature(student))