#Map Function
#Celsius to fahrenheit

print("Enter the the list of celsius values :")
clst = [float(x) for x in input().split()]

print("Celsius Values :",clst)

fah = lambda c: c*1.8+32

flist = list(map(fah,clst))

print("Corresponding Fahrenheit Values :",flist)
