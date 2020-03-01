#dbprogram1.py  ------- validating username and password

import sqlite3
from getpass import getpass
import sys

#Database connection
conn = sqlite3.connect("user.db")

#creating table
try:
    query1 = "create table user1(username TEXT, password TEXT)"
    conn.execute(query1)
except:
    print("Table is already exists")
    print("-"*50)


#inserting data
msg = input("Are you new user (y/n):")
if((msg=='y') or (msg=='Y')):
    uname = input("Enter Username :")
    passw = getpass()
    cpassw = getpass("Confirm Password:")
    if(passw==cpassw):
        query2 = "insert into user1 values('%s','%s')"%(uname,passw)
        conn.execute(query2)
        print("Registration Successfull.......[Ok]")
        #Login Module
    else:
        print("Password not matching, try again")
        sys.exit()
elif((msg=='n') or (msg=='N')):
    #Login Module
    print("Your are logged in!")
else:
    print("Invalid input please try again")
