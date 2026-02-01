import sqlite3
import pandas as pd

database = "VoidSyntax9x12/M13SQLUsingPythonII/L6/database.sqlite"

conn = sqlite3.connect(database)
if conn:
    print("Opened database successfully")

tables = pd.read_sql("""SELECT * FROM sqlite_master WHERE type='table';""", conn)
print(tables)

# Aliasing 
match_details = pd.read_sql("""SELECT Season_Id, Match_Id,  
                              v.Venue_Name, c.City_Name, t.Team_Name AS Winner 
                              FROM Match
                              INNER JOIN Venue AS v ON match.Venue_Id == v.Venue_Id
                              INNER JOIN City AS c ON v.City_Id == c.City_Id
                              INNER JOIN Team AS t ON match.Match_Winner == t.Team_Id;""", conn)

print(match_details)
