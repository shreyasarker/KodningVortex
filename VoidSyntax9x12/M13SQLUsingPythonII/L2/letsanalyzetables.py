import sqlite3
import pandas as pd

database = "VoidSyntax9x12/M13SQLUsingPythonII/L2/database.sqlite"

conn = sqlite3.connect(database)

if conn:
    print("Opened database successfully")


tables = pd.read_sql("""SELECT * FROM sqlite_master WHERE type='table';""", conn)
print(tables)

matches = pd.read_sql("""SELECT * FROM Match;""", conn)
print(matches)
