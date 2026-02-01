import sqlite3
import pandas as pd

database = "VoidSyntax9x12/M13SQLUsingPythonII/L3/database.sqlite"

conn = sqlite3.connect(database)
if conn:
    print("Opened database successfully")


tables = pd.read_sql("""SELECT * FROM sqlite_master WHERE type='table';""", conn)
print(tables)

# Display the first five rows of the Player_Match table
player_match = pd.read_sql("""SELECT * FROM Player_Match""", conn)

print(player_match.head())

# Check the presence of null values in the Player_Match table
null_player_match = pd.read_sql("""SELECT * FROM Player_Match WHERE Team_Id IS NULL""", conn)

print(null_player_match)

# Display the first five rows of the Match table
toss_dec = pd.read_sql("""SELECT * FROM Match""", conn)

print(toss_dec.head())

# Check the presence of null values in the Match table
null_match = pd.read_sql("""SELECT * FROM Match WHERE MATCH_Winner IS NULL""", conn)

print(null_match)
