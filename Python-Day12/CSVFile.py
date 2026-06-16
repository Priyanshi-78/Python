#Read CSV file
import pandas as pd

df = pd.read_excel("marka_data.xlsx")

#Head():Displays the first 5 rows
print(df.head())

# Tail():Displays the last 5 rows 
#print(df.tail())

#Info():Displays the information
#print(df.info())

#Shape():Displays the number of rows and columns
#print(df.shape())