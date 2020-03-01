#ForLoopExample4.py

""" pattern
   
   *
  **
 ***
****

 """

n = int(input("Enter the nth number:"))

i,j=0,0

for i in range(1,n):
    for j in range(1,i):
        print(" ",end="")
    for k in range(i,1):
        print("*",end="")
    print("\n")



