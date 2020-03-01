#SQLite3Example2.py  ---------- Insertion of data

import sqlite3

#Database connection
conn = sqlite3.connect("db1.db")

#insertion query
query1 = "insert into student values(1,'suprit',100.0)"
query2 = "insert into student values(2,'sumit',90.0)"
query3 = "insert into student values(3,'ganesh',80.0)"

#query execution
conn.execute(query1)
conn.commit()
conn.execute(query2)
conn.commit()
conn.execute(query3)
conn.commit()

print("Data inserted successfully")

