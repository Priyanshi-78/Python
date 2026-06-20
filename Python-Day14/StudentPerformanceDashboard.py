#Student Performance Dashboard

import pandas as pd

data = {
"Name":["Rahul","Aman","Priya","Rohan","Neha"],
"Course":["Python","SQL","Python","Power BI","SQL"],
"Marks":[78,85,92,65,88]
}

df=pd.dataframe(data)
print(df)

#Topper:
topper = df.sort_values("Marks",ascending=False).head(1)
print(topper)

#Top 3 Students:
top_3 = df.sort_values("Marks",ascending=False).head(3)
print(top_3)

#students above 80:
above_80 = df[df["Marks"] > 80]
print(above_80)

#Python Students:
python_students = df[df["Course"] =="Python"]
print(python_students)

#SQL Students:
sql_students = df[df["Course"] =="SQL"]
print(sql_students)

#Students between 70 and 90:
between_70_90 = df[(df["Marks"] > 70) & (df["Marks"] < 90)]
print(between_70_90)