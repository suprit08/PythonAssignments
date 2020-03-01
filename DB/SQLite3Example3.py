#SQLite3Example3.py ------------- selection or retriving data from database

import sqlite3

#database connection
conn = sqlite3.connect("db1.db")

#selection query
query = "select * from student"

#query execution
result = conn.execute(query)

print("-"*50)
print("Stno","\t","name","\t","Marks","\t")
print("-"*50)
for rec in result:
    print("%d\t%s\t%f"%(rec[0],rec[1],rec[2]))
print("-"*50)

print("completed...........[OK]")