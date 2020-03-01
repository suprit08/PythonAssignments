# OOPExample2.py

class Test:

    def __init__(self):
        print("Constructor Executed")
    
    def method1(self):
        print("Method executed")

t1=Test() #Constructor executed at time of creation
t2=Test() #----  
t3=Test() #----
t1.method1() #method called by object t1