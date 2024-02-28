import pandas as pd


# a
file_path = "Euro_2012_stats_TEAM.csv"
df = pd.read_csv(file_path)

# b
selected_columns = df[['Team', 'Yellow Cards', 'Red Cards']]
print("Selected columns:")
print(selected_columns)

# c
num_teams = df['Team'].nunique()
print("\nNumber of teams participated in Euro2012:", num_teams)

# d
teams_more_than_6_goals = df[df['Goals'] > 6][['Team', 'Goals']]
print("\nTeams that scored more than 6 goals:")
print(teams_more_than_6_goals)