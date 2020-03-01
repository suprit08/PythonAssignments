# Inside Constructor by using self variable

class Employee:
    def __init__(self):
        self.eno=100
        self.name="Suprit"

e=Employee()
print(e.__dict__)