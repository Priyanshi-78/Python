#Create Student DataFrame
import pandas as pd

data = {
    "Name": ["Priyanshi", "Shambhavi", "Ritika"],
    "Age": [20, 21, 22],
    "Marks": [98, 97, 83]
}

df = pd.DataFrame(data)

#Average:
print(df["Marks"].mean())
#Highest:
print(df["Marks"].max())
#Lowest:
print(df["Marks"].min())

print(df)