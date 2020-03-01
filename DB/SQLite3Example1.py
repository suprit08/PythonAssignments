#SQLite3Example1.py  --------  Table creation

import sqlite3

#db connection
conn = sqlite3.connect("db1.db")

#create table student
try:
    query = "create table student2(stno INT, name TEXT, marks REAL)"
    conn.execute(query)
    print("Table creation done successfully!")
except:
    print("table is already exists!")