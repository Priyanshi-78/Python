#Create Employee Record System
emp_id = input("Enter Employee id: ")
name = input("Enter Employee Name: ")
salary = input("Enter Employee Salary: ")
department = input("Enter Department: ")

file = open("employee.txt", "w")

file.write("Employee ID: " + emp_id + "\n")
file.write("Name: " + name + "\n")
file.write("Salary: " + salary + "\n")
file.write("Department: " + department + "\n")

file.close()
