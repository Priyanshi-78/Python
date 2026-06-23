import pandas as pd

df = pd.read_csv("Titanic-Data.csv")
print(df)

#Detect Missing Values
print(df.isnull().sum())
#Count missing values:
print(df.isnull().sum().sum())
#Remove missing values:
print(df.dropna())
#permanently remove missing values:
print(df.dropna(inplace=True))
#fill missing values:Fill with 0
print(df.fillna(0))
#fill missing values:Fill with average
print(df.fillna(df.mean()))
#Finding Duplicate records
print(df.duplicated())
#count duplicate records
print(df.duplicated().sum())
#Remove duplicate records
print(df.drop_duplicates())
#permanently remove duplicate records
print(df.drop_duplicates(inplace=True))
#Renaming Columns
print(df.rename(columns={"Pclass":"Passenger_class"}))
#Cleaning text data:Convert to Uppercase
df["Name"] = df["Name"].str.upper()
#Convert to Lowercase
df["Name"] = df["Name"].str.lower()
#Removing Extra spaces:
df["Name"] = df["Name"].str.strip()
#Change Data Type: Cleck data types
print(df.dtypes)
#Convert to integer:
df["Age"] = df["Age"].astype(int)
#Convert to float:
df["Age"] = df["Age"].astype(float)
#Replace values
df["Sex"] = df["Sex"].replace({"Male": "M","Female": "F"})
#Filtering Data: age above 30
df_filtered = df[df["Age"] > 30]
print(df_filtered)
#Age between 20 and 40
df_filtered = df[(df["Age"] >= 20) & (df["Age"] <= 40)]
print(df_filtered)
#Equla to condition:
df[df["Gender"] == "Female"]
#Not Equla to condition
df[df["Gender"] != "Female"]
#Multiple conditions(AND):
df[(df["Gender"] == "Female") & (df["Age"] > 30)]
#Multiple conditions (OR):
df[(df["Gender"] == "Female") | (df["Age"] > 30)]
#Between Range Filtering:(Age between 20 and 40)
df[df["Age"].between(20, 40)]
#Using isin():
df[df["Gender"].isin(["Female","Male"])]
#Filter top record:
df[df["Age"]>50]
#Sorting Data:Ascending order:
df.sort_values("Age")
#Sorting Data:Descending order:
df.sort_values("Age", ascending=False)
#Find highest age:
df.sort_values("Age", ascending=False).head(1)
#Top 3 highest age:
df.sort_values("Age", ascending=False).head(3)
#Sorting multiple columns:
df.sort_values(["Age", "Pclass"])

#Groupby AND Aggrigations:
#Groupby:
df.groupby("Gender")
#Count passengersID age wise:
df.groupby("Age")["PassengerId"].count()
#Average age gender wise:
df.groupby("Gender")["Age"].mean()
#Total Fare gender wise:
df.groupby("Gender")["Fare"].sum()
#Maximum Fare gender wise:
df.groupby("Gender")["Fare"].max()
#Minimum Fare gender wise:
df.groupby("Gender")["Fare"].min()
#Multiple Aggregations:
df.groupby("Gender")["Fare"].agg(['sum', 'mean', 'max', 'min'])
