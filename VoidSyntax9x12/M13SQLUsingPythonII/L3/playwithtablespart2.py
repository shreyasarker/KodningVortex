import sqlite3
import pandas as pd

database = "VoidSyntax9x12/M13SQLUsingPythonII/L3/database.sqlite"

conn = sqlite3.connect(database)
if conn:
    print("Opened database successfully")


tables = pd.read_sql("""SELECT * FROM sqlite_master WHERE type='table';""", conn)
print(tables)

matches = pd.read_sql("""SELECT * FROM Match;""", conn)
print(matches.head())

# Get the Average Win Margin of all the winning teams for Season 9
result1 = pd.read_sql("""SELECT AVG(Win_Margin), Match_Winner FROM Match WHERE Season_Id = 9 GROUP BY Match_Winner ORDER BY AVG(Win_Margin);""", conn)
print(result1)

# Get the count of the venues for Season 9
result2 = pd.read_sql("""SELECT COUNT(DISTINCT Venue_Id) FROM Match WHERE Season_Id = 9;""", conn)
print(result2)

# Get the Minimum, Maximum and Average Win Margin
# Also get the total number of players who have received man of the match throughout all the seasons
result3 = pd.read_sql("""SELECT MIN(Win_Margin), Max(Win_Margin), Avg(Win_Margin), COUNT(DISTINCT(Man_of_the_Match)) FROM Match;""", conn)
print(result3)

# Return total of win_margins for all the winners in season 9
result4 = pd.read_sql("""SELECT SUM(Win_Margin) FROM Match WHERE Season_Id = 9;""", conn)
print(result4)

