#OOPFuncExample1.py

class Details:
    age = 22
    name = "shruti"

details = Details()
print("Name is : ",getattr(details,"name"))
print("Age is : ",getattr(details,"age"))

print("---------------------------------------")

print("Name is ",details.name)
print("age is ",details.age)
