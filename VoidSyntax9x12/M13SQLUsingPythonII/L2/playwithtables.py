import sqlite3
import pandas as pd

database = "VoidSyntax9x12/M13SQLUsingPythonII/L2/database.sqlite"

conn = sqlite3.connect(database)
if conn:
    print("Opened database successfully")


tables = pd.read_sql("""SELECT * FROM sqlite_master WHERE type='table';""", conn)
print(tables)

teams = pd.read_sql("""SELECT * FROM Team;""", conn)
print(teams)

matches = pd.read_sql("""SELECT * FROM Match;""", conn)
print(matches)

# Check details of all the matches won by Mumbai Indians
MI_wins = pd.read_sql("""SELECT * FROM Match WHERE Match_Winner == 7;""", conn)
print(MI_wins)

# Check details of all the matches won by Mumbai Indians in last two seasons
MI_S8_S9 = pd.read_sql("""SELECT * FROM Match WHERE Match_Winner == 7 and Season_Id IN (8,9);""", conn)
print(MI_S8_S9)

new_teams = pd.read_sql("""SELECT * FROM Team WHERE Team_Name LIKE 'De%';""", conn)
print(new_teams)

# Check the minimum and maximum win_margin of all the matches 
min_max_margin = pd.read_sql("""SELECT MIN(Win_Margin), MAX(Win_Margin) FROM Match;""", conn)
print(min_max_margin)

