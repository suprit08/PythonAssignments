#ForLoopExample3.py ------pattern
""" 
    *
    **
    ***
    ****
    ***** 
"""

n = int(input("how much lines you required?:"))

i,j=0,0

for i in range(0,n):
    print("")
    for j in range(0,i+1):
        print("*",end="")
