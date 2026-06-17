import pandas as pd


# CSV file ko read karke DataFrame me store karna:
df = pd.read_csv("ipl_data.csv")


# Puri dataset print karna:
#print(df)

# Pehli 5 rows dekhna
print(df.head())

# Aakhri 5 rows dekhna
# print(df.tail())

# Dataset ki information dekhna
# Rows, columns, data types aur missing values pata chalti hain
#print(df.info())

# Saare column names dekhna
#print(df.columns)

# Dataset ka size dekhna
# Output format: (rows, columns)
#print(df.shape)

# Dataset ka statistical summary dekhna
#print(df.describe())


# Sirf winner column dekhna
#print(df["winner"])

# Ek se zyada columns dekhna
#print(df[["team1", "team2", "winner"]])


# Har column me kitni missing values hain
#print(df.isnull().sum())


# Unique cities dekhna
#print(df["city"].unique())

# Total unique cities count karna
#print(df["city"].nunique())


# Sirf Mumbai me hue matches
#print(df[df["city"] == "Mumbai"])

# Sirf 2016 season ke matches
#print(df[df["season"] == 2016])

# Sirf Mumbai Indians ke jeete hue matches
#print(df[df["winner"] == "Mumbai Indians"])


# 2016 me Mumbai me hue matches
#print(df[(df["season"] == 2016) & (df["city"] == "Mumbai")])

# Chennai Super Kings ya Mumbai Indians ke jeete hue matches

#print(df[(df["winner"] == "Chennai Super Kings")  (df["winner"] == "Mumbai Indians")])


# Sabse zyada runs se jeete matches
#print(df.sort_values("win_by_runs", ascending=False))

# Sabse zyada wickets se jeete matches
#print(df.sort_values("win_by_wickets", ascending=False))


# Sabse badi run victory
#print(df["win_by_runs"].max())

# Sabse badi wicket victory
#print(df["win_by_wickets"].max())

# Average runs se jeet
#print(df["win_by_runs"].mean())


# Sabse zyada runs se jeeta hua match
#biggest_run_win = df[df["win_by_runs"] == df["win_by_runs"].max()]
#print(biggest_run_win)

# Sabse zyada wickets se jeeta hua match
#biggest_wicket_win = df[df["win_by_wickets"] == df["win_by_wickets"].max()]
#print(biggest_wicket_win)


# Har season me kitne matches hue
#print(df.groupby("season")["id"].count())

# Har city me kitne matches hue
#print(df.groupby("city")["id"].count())

# Har team ne kitne matches jeete
#print(df.groupby("winner")["id"].count())



# Har team ki total wins
#print(df["winner"].value_counts())

# Player of the Match awards count
#print(df["player_of_match"].value_counts())

# Top 10 players with most Player of the Match awards
#print(df["player_of_match"].value_counts().head(10))



# Mumbai Indians ne kitne matches jeete
#print(df[df["winner"] == "Mumbai Indians"].shape[0])

# Virat Kohli kitni baar Player of the Match bane
#print(df[df["player_of_match"] == "V Kohli"].shape[0])


# Mumbai ke matches ko nayi CSV file me save karna
#mumbai_matches = df[df["city"] == "Mumbai"]
#mumbai_matches.to_csv("mumbai_matches.csv", index=False)