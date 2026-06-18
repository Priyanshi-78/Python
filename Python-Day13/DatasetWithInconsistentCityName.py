#Create dataset with inconsistent city names
import pandas as pd

data = {
    "Name": ["Priyanshi", "Priya", "Shambhavi"],
    "City": ["Delhi", "DELHI", "delhi"]
}

df = pd.DataFrame(data)
#print(df)

df["City"] = df["City"].str.upper()
print(df)