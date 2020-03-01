class Employee:
    def dispEmp(self):
        print("-"*40)
        print("Employee Number:",self.eno)
        print("Employee Name:",self.ename)
        print("-"*40)

#main section
print("EMPLOYEES")
        
e1=Employee()
e1.eno=1
e1.ename="Suprit"
e1.dispEmp()

e2=Employee()
e2.eno=2
e2.ename="Akshay"
e2.dispEmp()
