import pandas as pd

contents_df = pd.read_csv(r"C:\Users\berni\Documents\GitHub\DATA1002-Sports-Analysis\ATP Tennis\data\atp_matches_2024.csv")

#Selects the column, counts the number of times each player ID appears, renames for restructuring (Given a new column)
win_count = contents_df["winner_id"].value_counts().rename("Wins")
loss_count = contents_df["loser_id"].value_counts().rename("Losses")

#Selects two columns, removes duplicate pairings, makes winner_id/loser_id the index column
winner_ages = contents_df[["winner_id", "winner_age"]].drop_duplicates().set_index("winner_id")
loser_ages = contents_df[["loser_id", "loser_age"]].drop_duplicates().set_index("loser_id")

#Renaming to avoid concatenation issues
winner_ages = winner_ages.rename(columns={"winner_age": "Age"})
loser_ages = loser_ages.rename(columns={"loser_age": "Age"})

#Concatenates the two age dataframes together
merged_ages = pd.concat([winner_ages, loser_ages])

#Removes duped pairs after merge - Check the "~" meaning
merged_ages = merged_ages[~merged_ages.index.duplicated(keep='first')]
merged_ages = merged_ages.rename(columns={"winner_age": "Age", "loser_age": "Age"})

merged_ages = pd.concat([win_count, loss_count, merged_ages], axis=1).fillna(0)
merged_ages = merged_ages.reset_index().rename(columns={"index": "PlayerID"})

#Adding and changing relevant column datatypes from float to int
merged_ages["Matches Played"] = (merged_ages["Wins"] + merged_ages["Losses"]).astype(int)
merged_ages["Win Rate"] = merged_ages["Wins"] / merged_ages["Matches Played"]
merged_ages["Wins"] = merged_ages["Wins"].astype(int)
merged_ages["Losses"] = merged_ages["Losses"].astype(int)



#relevant_df = pd.concat([win_count, loss_count], axis=1).fillna(0).astype(int)
#print(relevant_df)
print(merged_ages)

cut_df = merged_ages[merged_ages["Matches Played"] > 2]

age_bins = [16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38]
cut_df["Age group (2 Years)"] = pd.cut(cut_df["Age"], bins = age_bins)

print(cut_df.groupby("Age group (2 Years)")["Win Rate"].mean())