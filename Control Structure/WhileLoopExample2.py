#While Loop Example ----- to print table of given number

i = 1

n = int(input("Enter the number to create table:"))

while i <= 10:
    print("%d X %d = %d"%(n,i,n*i))
    i = i+1

print("-"*50)