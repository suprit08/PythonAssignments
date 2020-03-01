# ConstructorExample1.py

class Student:
    def __init__(self,id,name,marks):
        self.id=id
        self.name=name
        self.marks=marks

    def display(self):
        print("Student Roll :{}\nStudent Name:{}\nStudent Marks:{}".format(self.id,self.name,self.marks))


s1=Student(1,"Suprit",100)
s1.display()

###################################

id=int(input("\nEnter the id of student: "))
name=input("\nEnter the name of student: ")
marks=int(input("\nEnter the total marks of student: "))

s2=Student(id,name,marks)
s2.display()

