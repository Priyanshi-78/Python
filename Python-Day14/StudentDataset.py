#Create Student Dataset
import pandas as pd

data = {
    "Student": ["Priyanshi", "Shambhavi", "Ritika", "Muskan", "Madhavi"],
    "Course": ["Python", "Java", "C++", "JavaScript", "SQL"],
    "Marks": [85, 92, 68, 76, 59]
}

df = pd.DataFrame(data)
# print(df)

# Above 80:
print(above_80 = df[df["Marks"] > 80])

# # #Below 70:
print(df[df["Marks"] < 70])

#Topper:
print(df.sort_values("Marks",ascending=False).head(1))
