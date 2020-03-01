# Outside of the class by object reference variable

class Test:

    def __init__(self):
        self.a=10
        self.b=20

    def method1(self):
        self.c=30

t=Test()
t.method1()
t.d=40
print(t.__dict__)