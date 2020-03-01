# Inside instance method by using Self variable

class Test:

    def __init__(self):
        self.a=10
        self.b=20

    def method1(self):
        self.c=30

t=Test()
t.method1()
print(t.__dict__)