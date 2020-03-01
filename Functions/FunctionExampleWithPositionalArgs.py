#positional parameter

def sq_area(side) : #function defination -------1) Function header
	area = side*side     ######################################### 2) function body -start
	return area          ######################################### -end


#Main program

print("-"*40)
side = float(input("Enter the side of square :"))
print("Square of area having side {0} is {1}".format(side,sq_area(side)))   # Function call in print() function passing position argument
print("-"*40)
