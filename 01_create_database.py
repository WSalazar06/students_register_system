import sqlite3

# Connect to a local SQLite database (creates file if it doesn't exist)
conn = sqlite3.connect('students.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create a table to store student data
cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        major TEXT
    )
''')

# Commit changes and close the connection
conn.commit()
conn.close()