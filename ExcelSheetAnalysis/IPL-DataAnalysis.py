import pandas as pd


# CSV file ko read karke DataFrame me store karega:
df = pd.read_csv("ipl_data.csv")


# Puri dataset print karna:
#print(df)

# Pehli ke 5 rows ko dekhna
print(df.head())

# Aakhri ke 5 rows ko dekhna
# print(df.tail())

# Dataset ki information dekhna
#print(df.info())

# Saare column ke names dekhna
#print(df.columns)

# Dataset ka size dekhna
#print(df.shape)

# Dataset ka summary dekhna
#print(df.describe())


# Sirf winner wala jo column hai usko dekhna
#print(df["winner"])

# Ek se zyada columns dekhne ke liye:
#print(df[["team1", "team2", "winner"]])


# Har column me kitni missing values hain check krne ke liye:
#print(df.isnull().sum())


# Unique cities dekhne ke liye:
#print(df["city"].unique())

# Total unique cities count karne ke liye:
#print(df["city"].nunique())


# Sirf Mumbai me kitne matches hue :
#print(df[df["city"] == "Mumbai"])

# Sirf 2016 season me kitne matches hue:
#print(df[df["season"] == 2016])

# Sirf Mumbai Indians ke jeete hue matches:
#print(df[df["winner"] == "Mumbai Indians"])


# Chennai Super Kings ya Mumbai Indians ke jeete hue matches:
#print(df[(df["winner"] == "Chennai Super Kings")  (df["winner"] == "Mumbai Indians")])


# Sabse zyada runs se jeete matches:
#print(df.sort_values("win_by_runs", ascending=False))


# Sabse badi run :
#print(df["win_by_runs"].max())

# Sabse badi wicket :
#print(df["win_by_wickets"].max())

# Average runs se jeet:
#print(df["win_by_runs"].mean())


# Sabse zyada runs se jeeta hua match:
#print(df["biggest_run_win"].max())

# Sabse zyada wickets se jeeta hua match:
#print(df["win_by_wickets"].max())


# Har season me kitne matches hue hai(total):
#print(df.groupby("season")["id"].count())

# Har city me kitne matches hue:
#print(df.groupby("city")["id"].count())

# Har team ne kitne matches jeete:
#print(df.groupby("winner")["id"].count())



# Har team ki total wins kya hai:
#print(df["winner"].value_counts())

# Player of the Match awards count:
#print(df["player_of_match"].value_counts())



# Virat Kohli kitni baar Player of the Match bane
#print(df[df["player_of_match"] == "V Kohli"].shape[0])

#mumbai_matches.to_csv("mumbai_matches.csv", index=False)

