# StaticExample2.py

class Test:
    a=10

    def __init__(self):
        Test.b=20 #Static Variable

    def m1(self):
        Test.c=30

    @classmethod
    def m2(cls):
        cls.d1=40
        Test.d2=400

    @staticmethod
    def m3():
        Test.e=50

print(Test.__dict__)

"""
t=Test()
print(Test.__dict__)

t.m1()
print(Test.__dict__)

Test.m2()
print(Test.__dict__)

Test.m3()
print(Test.__dict__)

Test.f=60
print(Test.__dict__)"""