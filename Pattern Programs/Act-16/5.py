"""Write a program that reads the following information and prints a payroll statement: Employee's name 
(e.g., Smith) Number of hours worked in a week (e.g.,10) Hourly pay rate (e.g., 9.75) Federal tax withholding 
rate (e.g., 20%) State tax withholding rate (e.g., 9%) .A sample run is shown below: 
Enter employee's name: Smith 
Enter number of hours worked in a week: 10 
Enter hourly pay rate: 9.75 
Enter federal tax withholding rate: 0.20 
Enter state tax withholding rate: 0.09 
Employee Name: Smith 
Hours Worked: 10.0 
Pay Rate: $9.75 
Gross Pay: $97.5 
Deductions: Federal Withholding (20.0%): $19.5
State Withholding (9.0%): $8.77 
Total Deduction: $28.27 
Net Pay: $69.22 """
Employee_Name = input("Employee Name = ")
Hours_Worked = int(input("Hours Worked = "))
Pay_Rate = float(input("Pay Rate per Hour= "))
Gross_Pay = float(input("Gross_Pay = "))
Federal_Withholding = float(input("Federal_Withholding = "))
State_Withholding = float(input("State_Withholding = "))
Total_Deduction = Federal_Withholding+State_Withholding
Net_Pay = Gross_Pay-Total_Deduction

print("Employee Name = ", Employee_Name)
print("Hours Worked = ", Hours_Worked)
print("Pay Rate per Hour= ", Pay_Rate)
print("Gross_Pay = ", Gross_Pay)
print("Federal_Withholding = ", Federal_Withholding)
print("State_Withholding = ", State_Withholding)
print("Total_Deduction = ", Total_Deduction)
print("Net_Pay = ", Net_Pay)