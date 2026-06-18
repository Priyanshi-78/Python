#Create dataset with duplicates
import pandas as pd

data = {
    "Name": ["Rahul", "Priya", "Rahul", "Aman", "Priya"],
    "Marks": [85, 92, 85, 78, 92],
    "City": ["Delhi", "Mumbai", "Delhi", "Lucknow", "Mumbai"]
}

df = pd.DataFrame(data)
#print(df)

# duplicated()
#print(df.duplicated())

# drop_duplicates()
print(df.drop_duplicates())