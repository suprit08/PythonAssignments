#OOPExample1.py
 
class Student:
    '''Developed by suprit for demo'''
    def __init__(self):
        self.name="Suprit"
        self.age=23
        self.marks=80

    def talk(self):
        print("hello my name is ",self.name)
        print("My age is ",self.age)
        print("My marks are ",self.marks)

s=Student()
s.talk()

#########################################################################################

print("-----------------------------------------------")

#########################################################################################

class Employee:
    def __init__(self):
        self.id=1
        self.name="Suprit Sonar"
        self.desi="Python Developer"
        self.salary=2000000.00
    
    def talk(self):
        print("MY name is ",self.name)
        print("Employee id is ",self.id)
        print("designation is ",self.desi)
        print("salary is ",self.salary)

e=Employee()
e.talk()