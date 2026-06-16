#Create Employee DataFrame
import pandas as pd

data = {
    "Employee_ID": [1001, 1002, 1003],
    "Name": ["Priyanshi", "Shambhavi", "Ritika"],
    "Salary": [45000, 62000, 59000]
}

df = pd.DataFrame(data)

#Average:
print(df["Salary"].mean())
#Highest:
print(df["Salary"].max())

print(df)