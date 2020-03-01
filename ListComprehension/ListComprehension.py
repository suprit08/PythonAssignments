#List comprehesion

#list compreshesnion of integer values
print("Enter the list of values:")
lst = [int(x) for x in input().split()]
print(lst)

#list comprehension of string values
print("Enter the strings:")
str_list = [x for x in input().split()]
print(str_list)

#List comprehension of character values
print("Enter the characters:")
char_list = [x for x in input().split()]
print(char_list)

#List comprehension  of float values
print("Enter the float values:")
float_list = [float(x) for x in input().split()]
print(float_list)