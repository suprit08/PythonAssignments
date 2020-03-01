#lamex1------Lambda Function
big=lambda a,b: a if a>b else b

#Main Program
num1 = int(input("Enter First number:"))
num2 = int(input("Enter Second number:"))

print("{0} is bigger".format(big(num1,num2)))