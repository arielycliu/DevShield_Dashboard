import pandas as pd
import sqlite3

# Read CSV data
df_hours_by_type = pd.read_csv('hours_by_type.csv')
df_meeting_cost = pd.read_csv('meeting_cost.csv')
df_person = pd.read_csv('person.csv')
df_productive_hours = pd.read_csv('productive_hours.csv')

# Connect to SQLite database
conn = sqlite3.connect('data.db')

# Insert data into a new table
df_hours_by_type.to_sql('hours_by_type', conn, if_exists='replace', index=False)
df_meeting_cost.to_sql('meeting_cost', conn, if_exists='replace', index=False)
df_person.to_sql('person', conn, if_exists='replace', index=False)
df_productive_hours.to_sql('productive_hours', conn, if_exists='replace', index=False)

# Commit and close
conn.commit()
conn.close()