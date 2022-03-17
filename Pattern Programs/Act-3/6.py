"""Create a function showEmployee() in such a way that it should accept employee name, 
and its salary and display both. If the salary is missing in the function call assign default 
value 9000 to salary"""
def show_employee():
    return name, salary
name=input("Enter Employee Name : ")
salary=input("Enter your Salary : ") or 9000
print(show_employee())