import pandas as pd
import sqlite3

# Read CSV data
df = pd.read_csv('data.csv')

# Connect to SQLite database
conn = sqlite3.connect('data.db')

# Insert data into a new table
df.to_sql('person', conn, if_exists='replace', index=False)

# Commit and close
conn.commit()
conn.close()