#ForLoopExample2.py -------- To print the table of given number.

i = 1
n = int(input("Enter the number to create table:"))

print("-"*50)

for i in range(i,n+1):
    print("%d X %d = %d"%(n,i,n*i))
