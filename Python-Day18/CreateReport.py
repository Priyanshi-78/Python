#Create report.xlsx with:
# Students Sheet
# Employees Sheet
# Attendance Sheet

import pandas as pd

# Students Data:
students = pd.DataFrame({
    "Student_ID": ["S101", "S102", "S103", "S104", "S105"],
    "Name": ["Rahul", "Priya", "Aman", "Neha", "Rohan"],
    "Course": ["Python", "SQL", "Python", "Power BI", "SQL"],
    "Marks": [78, 92, 85, 88, 75]
})

# Employees Data:
employees = pd.DataFrame({
    "Employee_ID": ["E101", "E102", "E103", "E104", "E105"],
    "Employee_Name": ["Anjali", "Vivek", "Pooja", "Karan", "Sneha"],
    "Department": ["HR", "IT", "Finance", "Sales", "Marketing"],
    "Salary": [45000, 60000, 55000, 50000, 48000]
})

# Attendance Data:
attendance = pd.DataFrame({
    "Student_ID": ["S101", "S102", "S103", "S104", "S105"],
    "Name": ["Rahul", "Priya", "Aman", "Neha", "Rohan"],
    "Attendance_Percentage": [90, 95, 88, 92, 85]
})

# Create Report:
with pd.ExcelWriter("report.xlsx") as writer:
 students.to_excel(writer, sheet_name="Students", index=False)
 employees.to_excel(writer, sheet_name="Employees", index=False)
 attendance.to_excel(writer, sheet_name="Attendance", index=False)