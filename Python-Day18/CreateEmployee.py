#Create employee.xlsx
import pandas as pd

#Read file:
df = pd.read_excel("Employee.xlsx")
# print(df)

#Find Average Salary
# average_salary = df["Salary"].mean()
# print(average_salary)

#Export Results
df.to_excel("employee_report.xlsx",index=False)