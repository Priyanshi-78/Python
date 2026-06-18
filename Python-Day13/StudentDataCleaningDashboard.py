#Student Data Cleaning Dashboard
import pandas as pd

data = {
    "Name": ["Rahul", " Aman ", "Priya", None],
    "Marks": [78, None, 92, 85],
    "City": ["Delhi", "DELHI", "delhi", "Delhi"]
}

df = pd.DataFrame(data)
print(df)

# 1. Check Missing Values
#print(df.isnull().sum())

# 2. Fill Missing Marks with Average Marks
#df["Age"].fillna(df["Age"].mean(), inplace=True)

# 3. Remove Spaces from Name Column
#df["Name"] = df["Name"].str.strip()

# 4. Standardize City Names
#df["City"] = df["City"].str.upper()
#df["City"] = df["City"].str.lower()

# 5. Generate Average Marks
#print(df["Marks"].mean())
