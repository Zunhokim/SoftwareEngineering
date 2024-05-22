import sqlite3
conn = sqlite3.connect('student.db')
print("Opened database successfully")

conn.execute('CREATE TABLE students (name TEXT, addr TEXT, phone TEXT, id TEXT)')
print("Table created successfully")
conn.close()